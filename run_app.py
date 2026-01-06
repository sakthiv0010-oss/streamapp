import subprocess
import webbrowser
import time
import os
import sys
import socket
import atexit
# 🔧 Fix: prevents exe from restarting multiple times
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

PORT = 8501
APP_FILE = "app.py"

def is_port_in_use(port):
    """Check if a port is already in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0
process = None
def run_app():
    global process
    if getattr(sys, "frozen", False):
        os.chdir(sys._MEIPASS)
    if is_port_in_use(PORT):
        # If already running, just open browser
        webbrowser.open(f"http://localhost:{PORT}")
        return
    cmd = [
        sys.executable, "-m", "streamlit", "run", APP_FILE,
        "--server.port", str(PORT),
        "--server.address", "127.0.0.1",
        "--server.headless", "true",
        "--server.runOnSave", "false"   # 🚫 disable auto-reload
    ]

    # Start Streamlit without blocking
    subprocess.Popen(cmd)
    atexit.register(lambda: process and process.terminate())

    # Give server a moment to start, then open browser
    time.sleep(2)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    # ✅ Only run once
      run_app()

