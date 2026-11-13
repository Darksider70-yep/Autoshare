import os
import subprocess
import glob

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
svg_files = glob.glob('docs/screenshots/*.svg')
print(f"Found {len(svg_files)} SVG files")

for svg_file in svg_files:
    base_name = os.path.splitext(os.path.basename(svg_file))[0]
    png_file = os.path.join('docs/screenshots', f"{base_name}.png")
    svg_abs = os.path.abspath(svg_file).replace('\\', '/')
    png_abs = os.path.abspath(png_file)
    
    cmd = f'"{edge_path}" --headless --disable-gpu --window-size=1200,800 --screenshot="{png_abs}" "file:///{svg_abs}"'
    subprocess.run(cmd, shell=True, capture_output=True)
    if os.path.exists(png_abs):
        print(f"Generated {png_file} ({os.path.getsize(png_abs)} bytes)")
    else:
        print(f"Failed to generate {png_file}")

print("All done.")

