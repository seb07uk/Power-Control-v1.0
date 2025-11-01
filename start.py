# Created by Sebastian Januchowski
# polsoft.its@fastservice.com
# https://github.com/seb07uk
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os
import webbrowser

# 🔒 Blokada ekranu
def lock():
    subprocess.run(os.path.expandvars(r"%systemroot%\system32\rundll32.exe user32.dll,LockWorkStation"), shell=True)

# 😴 Uśpienie systemu
def sleep():
    cmds = [
        "powercfg -h off",
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
        "powercfg -h on"
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)

# 🔁 Restart systemu
def restart():
    subprocess.run(os.path.expandvars(r"%systemroot%\system32\shutdown.exe /r /t 0"), shell=True)

# 🌙 Hibernacja
def hibernate():
    subprocess.run(os.path.expandvars(r"%systemroot%\system32\rundll32.exe powrprof.dll,SetSuspendState 0,1,0"), shell=True)

# ⏹ Pełne wyłączenie
def shutdown_full():
    subprocess.run(os.path.expandvars(r"%systemroot%\system32\shutdown.exe /s /t 0"), shell=True)

# ⚡ Hybrydowe wyłączenie
def shutdown_hybrid():
    subprocess.run(os.path.expandvars(r"%systemroot%\system32\shutdown.exe /s /hybrid /t 0"), shell=True)

# ℹ️ Okno „O programie”
def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About Power Control 1.0")
    about_window.geometry("300x220")
    about_window.resizable(False, False)

    tk.Label(about_window, text="2025© Sebastian Januchowski", font=("Arial", 10), justify="center").pack(pady=(15, 5))
    tk.Label(about_window, text="polsoft.ITS London", font=("Arial", 10), justify="center").pack(pady=2)
    tk.Label(about_window, text="email: polsoft.its@fastservice.com", font=("Arial", 10), justify="center").pack(pady=2)
    tk.Label(about_window, text="GitHub: https://github.com/seb07uk", font=("Arial", 10), justify="center").pack(pady=2)
    tk.Label(about_window, text="Repo: https://chomikuj.pl/polsoft-its/seb07uk", font=("Arial", 10), justify="center").pack(pady=2)

    tk.Button(about_window, text="Zamknij", command=about_window.destroy).pack(pady=10)

# 🖥️ Tworzenie GUI
root = tk.Tk()
root.title("Power Control")
root.geometry("300x360")

button_font = ("Arial", 12, "bold")

tk.Frame(root, height=20).pack()

tk.Button(root, text="🔒 Lock", command=lock, font=button_font, width=20).pack(pady=5)
tk.Button(root, text="😴 Sleep", command=sleep, font=button_font, width=20).pack(pady=5)
tk.Button(root, text="🔁 Restart", command=restart, font=button_font, width=20).pack(pady=5)
tk.Button(root, text="🌙 Hibernate", command=hibernate, font=button_font, width=20).pack(pady=5)
tk.Button(root, text="⏹ Shutdown (Full)", command=shutdown_full, font=button_font, width=20).pack(pady=5)
tk.Button(root, text="⚡ Shutdown (Hybrid)", command=shutdown_hybrid, font=button_font, width=20).pack(pady=5)

tk.Button(root, text="ℹ️ About", command=show_about, font=("Arial", 10, "bold"), width=10).pack(pady=(20, 5))

tk.Label(root, text="2025© Sebastian Januchowski", font=("Arial", 9), justify="center").pack(pady=(8, 10))

root.mainloop()