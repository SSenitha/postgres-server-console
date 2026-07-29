# 🐘 PostgreSQL Server Console

[![Build Status](https://img.shields.io/github/actions/workflow/status/SSenitha/postgres-server-console/build.yml?label=build&logo=github)](https://github.com/SSenitha/postgres-server-console/actions)
[![Release](https://img.shields.io/github/v/release/SSenitha/postgres-server-console?color=blue&logo=github)](https://github.com/SSenitha/postgres-server-console/releases/latest)
[![Platform](https://img.shields.io/badge/platform-Windows-0078D6?logo=windows)](https://github.com/SSenitha/postgres-server-console)
[![Python Version](https://img.shields.io/badge/python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/SSenitha/postgres-server-console?color=green)](https://github.com/SSenitha/postgres-server-console/blob/main/LICENSE)

A lightweight, zero-dependency Python GUI tool designed to start, stop, and inspect the local PostgreSQL service on Windows with a single click.

Created as a utility tool while learning PostgreSQL to prevent the database daemon from unnecessarily consuming background resources.

<br>

## ✨ Features
- **Auto-Detection:** Automatically scans Windows services (`sc query`) to detect your installed PostgreSQL service name and version dynamically at startup.

- **1-Click Control:** Quickly start and stop the PostgreSQL service without opening Command Prompt.

- **Live Output:** View real-time service status outputs directly within the application window.

<br>

## 🚀 Installation & Usage

### Option 1: Download Pre-built Binary (Recommended)
   No Python installation required.

   1. Go to the **[Releases](../../releases)** page on GitHub and download the latest `Postgres-Control-Panel-Windows.zip`.

   2. Extract the `.zip` archive to your preferred folder.

   3. Right-click `postgres_gui.exe`, select **Run as Administrator** (required to control Windows services).

   <br>

   > **Tip:** You can right-click `postgres_gui.exe` > **Properties** > **Compatibility**, and check **Run this program as an administrator** so it always launches with required permissions.

---

### Option 2: Run from Source Code
   1. Ensure Python 3.x is installed.

   2. Open Command Prompt **as Administrator** (required for system service controls).

   3. Run the script:

      ```
      python postgres_gui.py
      ```

---

### Option 3: Build locally with PyInstaller

   If you want to build the `.exe` manually from source:

   1. Install PyInstaller:
      ```
      pip install pyinstaller
      ```


   2. Build the executable:
      ```
      python -m PyInstaller --noconfirm --onedir --windowed postgres_gui.py
      ```


   3. Your executable will be located inside `dist/postgres_gui/postgres_gui.exe`. Remember to run it as Administrator!

<br>

## 🛠️ Built With

   * **Python 3**
   * **Tkinter** (Built-in GUI Library)
   * **Subprocess & Regex** (Windows CLI execution and service parsing)
   * **GitHub Actions** (Automated CI/CD build releases)