# 🐘 PostgreSQL Server Console

A lightweight, zero-dependency Python GUI tool designed to start, stop, and inspect the local PostgreSQL service on Windows with a single click.

Created as a utility tool while learning PostgreSQL to prevent the database daemon from unnecessarily consuming background resources.

## ✨ Features
- **Auto-Detection:** Automatically scans Windows services (`sc query`) to detect your installed PostgreSQL service name and version dynamically at startup.
- **1-Click Control:** Quickly start and stop the PostgreSQL service without opening Command Prompt.
- **Live Output:** View real-time service status outputs directly within the application window.

## 🚀 How to Run

### Option 1: Running with Python
1. Ensure Python 3.x is installed.
2. Open Command Prompt **as Administrator** (required for system service controls).
3. Run the script:
   ```cmd
   python postgres_gui.py
   ```

### Option 2: Build as a Standalone `.exe`
If you want to run this as a 1-click desktop app without needing Python open:

1. Install PyInstaller:
   ```cmd
   pip install pyinstaller
   ```
2. Build the app:
   ```cmd
   python -m PyInstaller --noconfirm --onedir --windowed postgres_gui.py
   ```
3. Navigate to `dist/postgres_gui/`, right-click `postgres_gui.exe`, go to **Properties > Compatibility**, and check **Run this program as an administrator**.

## 🛠️ Built With
- **Python 3**
- **Tkinter** (Built-in GUI Library)
- **Subprocess & Regex** (Windows CLI execution and service parsing)