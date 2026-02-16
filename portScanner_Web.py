import socket
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from flask import Flask, render_template, request

init(autoreset=True)  

app = Flask(__name__)


def ascii_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = [
        "",
        Fore.CYAN + "╔═══════════════════════════════════════════════════════════════════╗",
        Fore.CYAN + "║                                                                   ║",
        Fore.CYAN + "║   " + Fore.YELLOW + "██████╗  ██████╗ ██████╗ ████████╗" + Fore.CYAN + "                        ║",
        Fore.CYAN + "║   " + Fore.YELLOW + "██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝" + Fore.CYAN + "                        ║",
        Fore.CYAN + "║   " + Fore.YELLOW + "██████╔╝██║   ██║██████╔╝   ██║   " + Fore.CYAN + "                        ║",
        Fore.CYAN + "║   " + Fore.YELLOW + "██╔═══╝ ██║   ██║██╔══██╗   ██║   " + Fore.CYAN + "                        ║",
        Fore.CYAN + "║   " + Fore.YELLOW + "██║     ╚██████╔╝██║  ██║   ██║   " + Fore.CYAN + "                        ║",
        Fore.CYAN + "║   " + Fore.YELLOW + "╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   " + Fore.CYAN + "                        ║",
        Fore.CYAN + "║                                                                   ║",
        Fore.CYAN + "║   " + Fore.GREEN + "███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗" + Fore.CYAN + "  ║",
        Fore.CYAN + "║   " + Fore.GREEN + "██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗" + Fore.CYAN + " ║",
        Fore.CYAN + "║   " + Fore.GREEN + "███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝" + Fore.CYAN + " ║",
        Fore.CYAN + "║   " + Fore.GREEN + "╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗" + Fore.CYAN + " ║",
        Fore.CYAN + "║   " + Fore.GREEN + "███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║" + Fore.CYAN + " ║",
        Fore.CYAN + "║   " + Fore.GREEN + "╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝" + Fore.CYAN + " ║",
        Fore.CYAN + "║                                                                   ║",
        Fore.CYAN + "║" + Fore.MAGENTA + "                    Network Security Tool                      " + Fore.CYAN + "║",
        Fore.CYAN + "║" + Fore.WHITE + "                    Developed by Eshwar                        " + Fore.CYAN + "║",
        Fore.CYAN + "║                                                                   ║",
        Fore.CYAN + "╚═══════════════════════════════════════════════════════════════════╝",
        ""
    ]
    for line in banner:
        print(line)
        time.sleep(0.03)
    print(Fore.YELLOW + "\n⚡ Starting port scan... Please wait...\n")


def scan_port(ip, port):
    """Scan a single port and return results if open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)  # Fast timeout
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            service = "Unknown"
            version = "Unknown"
            
            try:
                service = socket.getservbyport(port)
            except:
                pass
            
            try:
                sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
                if banner:
                    version = banner.split("\n")[0]
            except:
                pass
            
            sock.close()
            return (port, service, version)
        
        sock.close()
    except:
        pass
    return None


def port_scanner(target_ip):
    # Handle URL/domain name input
    target = target_ip.strip()
    
    # Remove http:// or https:// if present
    if target.startswith('http://'):
        target = target[7:]
    elif target.startswith('https://'):
        target = target[8:]
    
    # Remove trailing slash and path
    target = target.split('/')[0]
    
    # Try to resolve domain name to IP
    try:
        resolved_ip = socket.gethostbyname(target)
        print(Fore.YELLOW + f"  🔍 Resolving {target} → {resolved_ip}")
    except socket.gaierror:
        print(Fore.RED + f"  ❌ Could not resolve hostname: {target}")
        return []
    
    open_ports = []
    ports_to_scan = range(1, 1025)
    
    # Use ThreadPoolExecutor for parallel scanning
    print(Fore.CYAN + f"  ⚡ Fast scanning {len(list(ports_to_scan))} ports...")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Submit all port scan tasks
        future_to_port = {executor.submit(scan_port, resolved_ip, port): port for port in ports_to_scan}
        
        # Collect results as they complete
        for future in as_completed(future_to_port):
            result = future.result()
            if result:
                open_ports.append(result)
                port, service, version = result
                print(Fore.GREEN + f"  ✓ Found open port: {port} ({service})")
    
    # Sort results by port number
    open_ports.sort(key=lambda x: x[0])
    
    return open_ports

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    target_ip = None
    resolved_ip = None
    if request.method == "POST":
        target_ip = request.form["target_ip"]
        
        # Resolve domain to IP
        target = target_ip.strip()
        if target.startswith('http://'):
            target = target[7:]
        elif target.startswith('https://'):
            target = target[8:]
        target = target.split('/')[0]
        
        try:
            resolved_ip = socket.gethostbyname(target)
            results = port_scanner(target_ip)
        except socket.gaierror:
            results = []
            
    return render_template('index.html', results=results, target_ip=target_ip, resolved_ip=resolved_ip)


if __name__ == "__main__":
    print(Fore.CYAN + "\n╔══════════════════════════════════════╗")
    print(Fore.CYAN + "║        " + Fore.YELLOW + "PORT SCANNER TOOL" + Fore.CYAN + "         ║")
    print(Fore.CYAN + "╚══════════════════════════════════════╝\n")
    
    print(Fore.GREEN + "  Select Mode:")
    print(Fore.YELLOW + "    [1] " + Fore.WHITE + "Terminal Mode")
    print(Fore.YELLOW + "    [2] " + Fore.WHITE + "Web UI Mode\n")
    
    mode = input(Fore.CYAN + "  Enter your choice (1 or 2): " + Fore.WHITE)

    if mode == "1":
        ascii_banner()
        target = input(Fore.CYAN + "🎯 Enter target IP or website URL: " + Fore.WHITE)
        print(Fore.YELLOW + f"\n⚡ Fast scanning ports on {target}...\n")
        
        start_time = time.time()
        results = port_scanner(target)
        end_time = time.time()
        
        scan_duration = end_time - start_time
        
        scan_duration = end_time - start_time
        
        print(Fore.GREEN + "╔══════════════════════════════════════════════════════════════╗")
        print(Fore.GREEN + f"║  Scan Complete! Found {len(results)} open port(s)")
        print(Fore.GREEN + f"║  Scan Duration: {scan_duration:.2f} seconds")
        print(Fore.GREEN + "╚══════════════════════════════════════════════════════════════╝\n")
        
        for port, service, version in results:
            print(Fore.GREEN + f"  ✓ Port {port:5d} → " + Fore.YELLOW + f"{service:15s}" + Fore.CYAN + f" ({version})")
        
        print(Fore.GREEN + "\n╔══════════════════════════════════════════════════════════════╗")
        print(Fore.GREEN + f"║  Total Open Ports: {len(results)}")
        print(Fore.GREEN + "╚══════════════════════════════════════════════════════════════╝\n")

    else:
        print(Fore.CYAN + "\n╔══════════════════════════════════════════════════════════════╗")
        print(Fore.CYAN + "║  🌐 Starting Web UI Server...                                ║")
        print(Fore.CYAN + "║                                                              ║")
        print(Fore.GREEN + "║  ✓ Server running at: " + Fore.YELLOW + "http://127.0.0.1:5000/" + Fore.CYAN + "         ║")
        print(Fore.GREEN + "║  ✓ Access from network: " + Fore.YELLOW + "http://0.0.0.0:5000/" + Fore.CYAN + "       ║")
        print(Fore.CYAN + "║                                                              ║")
        print(Fore.CYAN + "║  Press CTRL+C to stop the server                            ║")
        print(Fore.CYAN + "╚══════════════════════════════════════════════════════════════╝\n")
        app.run(host="0.0.0.0", port=5000, debug=False)
