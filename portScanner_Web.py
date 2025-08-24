#Follow the 'eshwargit2' github page
#Link: https://github.com/eshwargit2/Port_Scanner.git
import socket
import time
import os
from colorama import Fore, Style, init
from flask import Flask, render_template_string, request

init(autoreset=True)  

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Port Scanner by Eshwar</title>
    <style>
        body { font-family: monospace; background: #0d1117; color:green; padding: 20px; }
        h1 { color: green; }
        input, button { padding: 8px; margin: 5px; border-radius: 5px; }
        .open { color: green; }
        .closed { color: green; }
        .summary { color: green; }
    </style>
</head>
<body>
    <h1>Port Scanner by Eshwar</h1>
    <form method="POST">
        <label>Enter Target IP:</label>
        <input type="text" name="target_ip" placeholder="192.168.100.1" required>
        <button type="submit">Scan</button>
    </form>
    {% if results %}
        <h2>Results for {{ target_ip }}</h2>
        <pre>
{% for port, service, version in results %}
Port {{ port }}: <span class="open">OPEN</span> | Service: {{ service }} | Version: {{ version }}
{% endfor %}
        </pre>
        <p class="summary">Total open ports: {{ results|length }}</p>
    {% endif %}
</body>
</html>
"""


def ascii_banner():
    os.system("clear")
    animation = [
        Fore.CYAN + r"   ____              _             ____                                  ",
        Fore.CYAN + r"  |  _ \ ___   ___ | |_ ___ _ __ / ___|  ___ __ _ _ __  _ __   ___ _ __ ",
        Fore.CYAN + r"  | |_) / _ \ / _ \| __/ _ \ '__| |  _  / __/ _` | '_ \| '_ \ / _ \ '__|",
        Fore.CYAN + r"  |  __/ (_) | (_) | ||  __/ |  | |_| | (_| (_| | | | | | | |  __/ |    ",
        Fore.CYAN + r"  |_|   \___/ \___/ \__\___|_|   \____| \___\__,_|_| |_|_| |_|\___|_|   ",
        r"                                                                        ",
        Fore.YELLOW + r"--------------------  Port Scanner by Eshwar  --------------------------"
    ]
    for line in animation:
        print(line)
        time.sleep(0.05)
    print("\n")


def port_scanner(target_ip):
    open_ports = []

    for port in range(1, 1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))

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

            open_ports.append((port, service, version))

        sock.close()

    return open_ports

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    target_ip = None
    if request.method == "POST":
        target_ip = request.form["target_ip"]
        results = port_scanner(target_ip)
    return render_template_string(HTML_TEMPLATE, results=results, target_ip=target_ip)


if __name__ == "__main__":
    

    mode = input(Fore.GREEN +"Choose One: \n   1. Terminal \n  " " \n   2. Web UI \n  "" \n Enter Option : ")

    if mode == "1":
        ascii_banner()
        target = input(Fore.BLUE + "Enter target IP address: ")
        results = port_scanner(target)
        print(Fore.GREEN + f"\nTotal open ports found: {len(results)}")
        for port, service, version in results:
            print(Fore.GREEN + f"Port {port} -> {service} ({version})")

    else:
        print(Fore.CYAN + "[*] Starting Web UI at http://127.0.0.1:5000/")
        app.run(host="0.0.0.0", port=5000, debug=False)
