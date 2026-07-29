import subprocess
import tkinter as tk
import re
from tkinter import ttk

# Define your service name
SERVICE_NAME = None


def find_postgres_service():
    """Dynamically detects the installed PostgreSQL service name on Windows."""
    try:
        # Run sc query state= all to scan all services
        result = subprocess.run(
            ["sc", "query", "state=", "all"],
            capture_output=True,
            text=True,
            creationflags=0x08000000,
        )

        # Look for service names matching 'postgresql-x64-XX'
        matches = re.findall(r"SERVICE_NAME:\s*(postgresql-[^\s]+)", result.stdout)

        if matches:
            return matches[0]
        
    except Exception as e:
        print(f"Error querying services: {e}")

    return None


def run_command(command_args):
    """Executes a system command and updates the status display."""
    if not SERVICE_NAME:
        status_text.delete("1.0", tk.END)
        status_text.insert(
            tk.END, "Error: No PostgreSQL service detected on this machine."
        )
        return

    # Replace placeholder with dynamic service name
    full_command = [
        SERVICE_NAME if arg == "{SERVICE}" else arg for arg in command_args
    ]

    status_text.delete("1.0", tk.END)
    status_text.insert(tk.END, f"Running: {' '.join(full_command)}\n\n")
    window.update_idletasks()

    try:
        result = subprocess.run(
            full_command, capture_output=True, text=True, creationflags=0x08000000
        )

        output = result.stdout or result.stderr
        status_text.insert(tk.END, output.strip())
    except Exception as e:
        status_text.insert(tk.END, f"Error: {e}")


def start_service():
    run_command(["net", "start", "{SERVICE}"])


def stop_service():
    run_command(["net", "stop", "{SERVICE}"])


def check_status():
    run_command(["sc", "query", "{SERVICE}"])


#----------------------------- GUI Layout -----------------------------
window = tk.Tk()
window.title("Postgres Control Panel")
window.geometry("450x300")
window.resizable(False, False)

#--- Startup Detection and Header ---

# Detect PostgreSQL service on launch
SERVICE_NAME = find_postgres_service()

# Service Header Label
version_label_text = (
    f"PostgreSQL Server Console"
    if SERVICE_NAME
    else "Status: PostgreSQL Service Not Found"
)
header = tk.Label(
    window, text=version_label_text, font=("Arial", 10, "bold"), fg="#2c3e50"
)
header.pack(pady=(10, 0))
#---

#---
# Initialize the style manager
style = ttk.Style()

# Configure the global TButton style with a sunken relief
style.configure('green.TButton', foreground="#169139")
style.configure('red.TButton', foreground="#d60d0d")
# [flat, groove, raised, ridge, solid, sunken]
#---

# Button Frame
button_frame = tk.Frame(window, pady=10)
button_frame.pack()

start_btn = ttk.Button(
    button_frame,
    text="Start Postgres",
    style='green.TButton',
    width=15,
    command=start_service,
)
start_btn.pack(side=tk.LEFT, padx=5)

stop_btn = ttk.Button(
    button_frame,
    text="Stop Postgres",
    style='red.TButton',
    width=15,
    command=stop_service,
)
stop_btn.pack(side=tk.LEFT, padx=5)

status_btn = ttk.Button(
    button_frame,
    text="Check Status",
    width=15,
    command=check_status
)
status_btn.pack(side=tk.LEFT, padx=5)

# Output Display
status_text = tk.Text(window, height=12, width=52, wrap=tk.WORD)
status_text.pack(padx=10, pady=10)

# Welcome Message
welcome_message = (
    "Welcome to the PostgreSQL Control Panel\n"
    "---------------------------------------\n\n"
    "console version \t:1.0.0\n"
    f"postgre version \t:{SERVICE_NAME}\n\n\n"
    "Made with ♡ by Sandaru \nFOC, University of Sri Jayewardenepura\n"
)
status_text.insert(tk.END, welcome_message)

window.mainloop()