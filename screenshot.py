#!/usr/bin/env python3
"""
screenshot.py — take a full-page screenshot of the Caldwell site.
Usage:
  python3 screenshot.py            → hero viewport (1440x900)
  python3 screenshot.py full       → full page scroll
  python3 screenshot.py <label>    → saves as screenshot-N-label.png
"""
import os, sys, subprocess, glob, time, signal

SITE_DIR  = os.path.dirname(os.path.abspath(__file__))
SHOT_DIR  = os.path.join(SITE_DIR, "temporary screenshots")
CHROME    = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT      = 4000
BASE_URL  = f"http://localhost:{PORT}/?screenshot"

os.makedirs(SHOT_DIR, exist_ok=True)

# Next auto-incremented filename
existing = glob.glob(os.path.join(SHOT_DIR, "screenshot-*.png"))
nums = [int(os.path.basename(f).split("-")[1].split(".")[0].split("-")[0])
        for f in existing if os.path.basename(f).split("-")[1][0].isdigit()]
n = max(nums, default=0) + 1

label = sys.argv[1] if len(sys.argv) > 1 else ""
filename = f"screenshot-{n}-{label}.png" if label else f"screenshot-{n}.png"
out = os.path.join(SHOT_DIR, filename)

# Start server if not already running
server = None
try:
    import urllib.request
    urllib.request.urlopen(f"http://localhost:{PORT}", timeout=1)
except Exception:
    server = subprocess.Popen(
        ["python3", "-m", "http.server", str(PORT)],
        cwd=SITE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(1.5)

# Take screenshot
subprocess.run([
    CHROME,
    "--headless=new",
    "--disable-gpu",
    f"--screenshot={out}",
    "--window-size=1440,900",
    "--hide-scrollbars",
    "--virtual-time-budget=2000",
    BASE_URL
], capture_output=True)

if server:
    server.terminate()

print(out)
