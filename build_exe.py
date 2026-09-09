import os
import sys
import subprocess
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def build():
    print("Building Quantum-AI.exe...")
    
    # Path separators for Windows add-data
    add_data_args = [
        "--add-data", f"{os.path.join(BASE_DIR, 'index.html')};.",
        "--add-data", f"{os.path.join(BASE_DIR, 'src')};src",
        "--add-data", f"{os.path.join(BASE_DIR, 'public')};public",
    ]

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconsole",
        "--onefile",
        "--name", "Quantum-AI",
        "--clean",
        *add_data_args,
        os.path.join(BASE_DIR, "app.py")
    ]

    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd, cwd=BASE_DIR)
    
    if res.returncode == 0:
        dist_exe = os.path.join(BASE_DIR, "dist", "Quantum-AI.exe")
        target_exe = os.path.join(BASE_DIR, "Quantum-AI.exe")
        if os.path.exists(dist_exe):
            shutil.copy2(dist_exe, target_exe)
            print(f"\n✅ SUCCESS! Quantum-AI.exe created at:\n{target_exe}")
    else:
        print("\n❌ Build failed!")

if __name__ == "__main__":
    build()
