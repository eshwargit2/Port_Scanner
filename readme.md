# Port Scanner by Eshwar

A simple Python-based port scanner with both terminal and web UI, created by Eshwar.

## Features

- Scans ports 1-1024 on a target IP address.
- Displays open ports, detected service, and version banner (if available).
- Two modes:
  - **Terminal Mode**: Interactive CLI with colored output.
  - **Web UI**: Flask-powered web interface for easy scanning from your browser.

## Requirements

- Python 3.x
- [Flask](https://pypi.org/project/Flask/)
- [colorama](https://pypi.org/project/colorama/)

Install dependencies with:
```sh
pip install flask colorama
```

## Usage

Run the script:
```sh
python "portScanner_Web copy.py"
```

Choose your mode:
- Enter `1` for Terminal mode.
- Enter `2` for Web UI mode.

### Terminal Mode

- Enter the target IP address when prompted.
- The script will display open ports and their details.

### Web UI Mode

- The script will start a web server at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- Open the URL in your browser.
- Enter the target IP and click "Scan" to view results.

## Disclaimer

This tool is for educational