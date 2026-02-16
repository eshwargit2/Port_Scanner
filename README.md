# 🔍 Port Scanner Tool

A powerful and modern network security tool for scanning open ports on target IP addresses or domain names. Built with Python and Flask, featuring both a beautiful web interface and a terminal-based mode with fast multi-threaded scanning.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🚀 **Fast Multi-threaded Scanning** - Scans 1024 ports in seconds using 100 concurrent threads
- 🌐 **Dual Interface** - Choose between Web UI or Terminal mode
- 🎯 **Flexible Input** - Accepts IP addresses, domain names, or full URLs
- 🔄 **Auto DNS Resolution** - Automatically resolves domain names to IP addresses
- 📊 **Real-time Results** - See open ports as they're discovered
- 💎 **Beautiful UI** - Modern, responsive web interface with gradient design
- ⚡ **Service Detection** - Identifies services running on open ports
- 📈 **Version Detection** - Attempts to grab service banners for version info
- 🎨 **Clean Terminal UI** - Color-coded ASCII art interface for terminal mode

## 📋 Requirements

- Python 3.7 or higher
- Flask
- colorama
- concurrent.futures (included in Python 3.2+)

## 🚀 Installation

1. **Clone or download this repository**

```bash
git clone <repository-url>
cd python_tool
```

2. **Install required packages**

```bash
pip install flask colorama
```

## 💻 Usage

### Running the Application

```bash
python portScanner_Web.py
```

### Mode Selection

When you run the application, you'll be prompted to choose a mode:

```
╔══════════════════════════════════════╗
║        PORT SCANNER TOOL         ║
╚══════════════════════════════════════╝

  Select Mode:
    [1] Terminal Mode
    [2] Web UI Mode

  Enter your choice (1 or 2):
```

### Terminal Mode

**Perfect for quick scans and command-line enthusiasts**

1. Select option `1`
2. Enter target IP address or domain name:
   - IP: `192.168.1.1`
   - Domain: `google.com`
   - URL: `https://github.com`
3. Watch real-time scanning progress
4. View results with scan duration

**Example:**
```bash
🎯 Enter target IP or website URL: google.com

⚡ Fast scanning ports on google.com...

  🔍 Resolving google.com → 142.250.185.46
  ⚡ Fast scanning 1024 ports...
  ✓ Found open port: 80 (http)
  ✓ Found open port: 443 (https)

╔══════════════════════════════════════════════════════════════╗
║  Scan Complete! Found 2 open port(s)
║  Scan Duration: 3.45 seconds
╚══════════════════════════════════════════════════════════════╝
```

### Web UI Mode

**Best for detailed analysis and visual experience**

1. Select option `2`
2. Open your browser and navigate to:
   - Local: `http://127.0.0.1:5000/`
   - Network: `http://YOUR_LOCAL_IP:5000/`
3. Enter target IP or domain in the web form
4. Click "🚀 Start Scanning"
5. View beautifully formatted results

**Features:**
- Responsive design (works on mobile!)
- Gradient purple theme
- Animated port results
- Service and version information for each port
- Total open ports summary
- DNS resolution display

## 📊 Supported Input Formats

| Format | Example | Description |
|--------|---------|-------------|
| IPv4 Address | `192.168.1.1` | Direct IP address |
| Domain Name | `google.com` | Will be resolved to IP |
| Subdomain | `mail.google.com` | Subdomains supported |
| Full URL | `https://github.com` | Protocol and path stripped automatically |
| Personal Domain | `soundharesh.me` | Any valid domain |

## 🔧 Configuration

### Adjust Scanning Parameters

Edit `portScanner_Web.py` to customize:

**Port Range:**
```python
ports_to_scan = range(1, 1025)  # Change to scan more/fewer ports
```

**Thread Count:**
```python
with ThreadPoolExecutor(max_workers=100) as executor:  # Adjust worker count
```

**Timeout:**
```python
sock.settimeout(0.2)  # Increase for slower networks
```

**Web Server Port:**
```python
app.run(host="0.0.0.0", port=5000, debug=False)  # Change port number
```

## 📁 Project Structure

```
python_tool/
├── portScanner_Web.py          # Main application file
├── templates/
│   └── index.html              # Web UI template
└── README.md                   # This file
```

## 🎨 Web UI Screenshots

**Main Interface:**
- Modern gradient background (purple to violet)
- Clean input form with placeholder text
- Info box showing scan mode details

**Results Display:**
- Color-coded port items
- Hover effects on port cards
- Status badges for open ports
- Summary card with total count

## ⚡ Performance

- **Sequential Scanning:** ~8-10 minutes for 1024 ports
- **Multi-threaded Scanning:** ~10-30 seconds for 1024 ports
- **Speed Improvement:** ~50-100x faster!

## 🛡️ Legal & Ethical Considerations

⚠️ **Important Notice:**

This tool is designed for **educational purposes** and **authorized security testing only**.

**You should only scan:**
- Your own systems and networks
- Systems you have explicit written permission to test
- Networks where you are the administrator

**Unauthorized port scanning may be:**
- Illegal in your jurisdiction
- Violation of computer fraud laws
- Against terms of service of hosting providers

**Use responsibly and ethically!**

## 🐛 Troubleshooting

### Common Issues

**Issue:** "No module named 'flask'"
```bash
Solution: pip install flask
```

**Issue:** "No module named 'colorama'"
```bash
Solution: pip install colorama
```

**Issue:** Web UI not accessible from other devices
```bash
Solution: Check firewall settings and ensure port 5000 is open
```

**Issue:** Scanning is slow
```bash
Solution: Reduce port range or increase timeout value
```

**Issue:** DNS resolution fails
```bash
Solution: Check internet connection and DNS settings
```

## 🚀 Future Enhancements

- [ ] Export results to CSV/JSON
- [ ] Scan history and saved results
- [ ] Custom port range selection in UI
- [ ] OS detection
- [ ] Vulnerability database integration
- [ ] Multiple target scanning
- [ ] Scheduled scans
- [ ] Email notifications
- [ ] API endpoint for automation

## 👨‍💻 Developer

**Developed by Eshwar**

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

If you have any questions or need help, feel free to open an issue.

---

**Happy Scanning! 🔍✨**
