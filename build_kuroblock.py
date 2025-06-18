#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for Kuroblock.exe
"""

import os
import sys
import subprocess
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✅ PyInstaller already installed")
        return True
    except ImportError:
        print("📦 Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install PyInstaller")
            return False

def build_kuroblock():
    """Build kuroblock.exe"""
    print("🔨 Building Kuroblock.exe...")
    
    # PyInstaller command for kuroblock
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable
        "--console",                    # Console application
        "--name=Kuroblock",             # Output name
        "--icon=kuroblock.ico",         # Icon file
        "--distpath=dist",              # Output directory
        "--workpath=build",             # Build directory
        "--clean",                      # Clean cache
        "--noconfirm",                  # Don't ask for confirmation
        "kuroblock_menu.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Kuroblock.exe built successfully!")
        print("Output: dist/Kuroblock.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

def create_installer_script():
    """Create installer script for Kuroblock.exe"""
    installer_content = '''@echo off
title Kuroblock Installer
color 0A

echo.
echo ========================================
echo    KUROBLOCK INSTALLER
echo ========================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %%errorLevel%% == 0 (
    echo [INFO] Running as Administrator
) else (
    echo [ERROR] Please run as Administrator!
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo [INFO] Installing Kuroblock...

REM Create installation directory
if not exist "C:\\Program Files\\Kuroblock" mkdir "C:\\Program Files\\Kuroblock"

REM Copy executable
copy "Kuroblock.exe" "C:\\Program Files\\Kuroblock\\"

REM Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%%USERPROFILE%%\\Desktop\\Kuroblock.lnk'); $Shortcut.TargetPath = 'C:\\Program Files\\Kuroblock\\Kuroblock.exe'; $Shortcut.Save()"

REM Create start menu shortcut
if not exist "%%APPDATA%%\\Microsoft\\Windows\\Start Menu\\Programs\\Kuroblock" mkdir "%%APPDATA%%\\Microsoft\\Windows\\Start Menu\\Programs\\Kuroblock"
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%%APPDATA%%\\Microsoft\\Windows\\Start Menu\\Programs\\Kuroblock\\Kuroblock.lnk'); $Shortcut.TargetPath = 'C:\\Program Files\\Kuroblock\\Kuroblock.exe'; $Shortcut.Save()"

echo.
echo [SUCCESS] Kuroblock installed successfully!
echo You can now run Kuroblock from:
echo - Desktop shortcut
echo - Start Menu
echo - C:\\Program Files\\Kuroblock\\Kuroblock.exe
echo.
pause
'''
    
    with open("install_kuroblock.bat", "w") as f:
        f.write(installer_content)
    
    print("✅ Installer script created: install_kuroblock.bat")

def create_readme():
    """Create README for the built executable"""
    readme_content = '''# Kuroblock.exe

## Description
Kuroblock is a Python-based tool that blocks Wuthering Waves game servers by modifying the hosts file. This allows you to use cheats or mods without being detected by the game's anti-cheat system.

## Features
- Blocks all Wuthering Waves data receiver servers
- Creates automatic backup of hosts file
- Checks and reports status of each domain
- Removes duplicate entries
- Requires administrator privileges for security

## Installation
1. Run `install_kuroblock.bat` as Administrator
2. The executable will be installed to `C:\\Program Files\\Kuroblock\\`
3. Desktop and Start Menu shortcuts will be created

## Usage
1. Right-click on Kuroblock.exe and select "Run as administrator"
2. The tool will automatically:
   - Create a backup of your hosts file
   - Check current blocking status
   - Add missing domain blocks
   - Remove duplicates
   - Report completion

## Blocked Domains
- as-datareceiver.aki-game.net
- eu-datareceiver.aki-game.net
- us-datareceiver.aki-game.net
- hk-datareceiver.aki-game.net
- jp-datareceiver.aki-game.net
- sea-datareceiver.aki-game.net
- tw-datareceiver.aki-game.net
- cn-datareceiver.aki-game.net
- sentry.aki.kuro.com

## Backup Location
Backups are stored in: `C:\\Windows\\System32\\drivers\\etc\\backups\\`

## Warning
This tool modifies system files. Always run as Administrator.
Use at your own risk. Modifying game files may violate terms of service.
Keep backups of your hosts file before using.

## Build Information
- Built with PyInstaller
- Python version: 3.12
- Single file executable
- No external dependencies required
'''
    
    with open("README_Kuroblock.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ README created: README_Kuroblock.txt")

def main():
    print("🚀 Kuroblock Build Script")
    print("=" * 40)
    
    # Install PyInstaller
    if not install_pyinstaller():
        return
    
    # Build executable
    if build_kuroblock():
        # Create installer
        create_installer_script()
        
        # Create README
        create_readme()
        
        print("\nBuild completed successfully!")
        print("Files created:")
        print("  - dist/Kuroblock.exe (Main executable)")
        print("  - install_kuroblock.bat (Installer script)")
        print("  - README_Kuroblock.txt (Documentation)")
        print("\nTo install:")
        print("  1. Run install_kuroblock.bat as Administrator")
        print("  2. Or copy Kuroblock.exe to desired location")
        print("\nTo use:")
        print("  Right-click Kuroblock.exe and 'Run as administrator'")
    else:
        print("\n❌ Build failed!")

if __name__ == "__main__":
    main() 