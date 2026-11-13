import os
import subprocess
import time

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

screens = [
    ('http://localhost:3000', 'docs/screenshots/real_browser_landing.png', 1280, 900),
    ('http://localhost:3000/?modal=true', 'docs/screenshots/real_browser_post_ride_modal.png', 1280, 900),
    ('http://localhost:3000/?chat=true', 'docs/screenshots/real_browser_chat_drawer.png', 1280, 900),
    ('http://localhost:3000/?tab=users', 'docs/screenshots/real_browser_user_records.png', 1280, 950),
    ('http://localhost:3000/?tab=microservices', 'docs/screenshots/real_browser_microservices_console.png', 1280, 1050),
]

for url, out_path, w, h in screens:
    abs_out = os.path.abspath(out_path)
    if os.path.exists(abs_out):
        os.remove(abs_out)
    cmd = f'"{edge_path}" --headless --disable-gpu --virtual-time-budget=4000 --window-size={w},{h} --screenshot="{abs_out}" "{url}"'
    subprocess.run(cmd, shell=True, capture_output=True)
    if os.path.exists(abs_out):
        print(f"Captured {out_path} ({os.path.getsize(abs_out)} bytes)")
    else:
        print(f"Failed to capture {out_path}")

print("All real browser screenshots captured.")
