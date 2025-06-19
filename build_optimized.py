#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Script for Kuroblock
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_version_info():
    """Create version info for the executable"""
    version_info = '''
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Kuroblock Team'),
         StringStruct(u'FileDescription', u'Wuthering Waves Server Blocker'),
         StringStruct(u'FileVersion', u'1.0.0'),
         StringStruct(u'InternalName', u'kuroblock'),
         StringStruct(u'LegalCopyright', u'MIT License'),
         StringStruct(u'OriginalFilename', u'Kuroblock.exe'),
         StringStruct(u'ProductName', u'Kuroblock'),
         StringStruct(u'ProductVersion', u'1.0.0')])
    ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(version_info)
    return 'version_info.txt'

def create_optimized_spec():
    """Create PyInstaller spec file"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['kuroblock_menu_optimized.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'scipy', 'PIL', 'tkinter', 'PyQt5', 'PySide2'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Kuroblock',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.txt',
    icon='kuroblock.ico',
    uac_admin=True,
    uac_uiaccess=False,
)
'''
    with open('Kuroblock_optimized.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    return 'Kuroblock_optimized.spec'

def build_executable():
    """Build the executable"""
    print("🔧 Building Kuroblock executable...")
    
    # Create version info
    version_file = create_version_info()
    print(f"✅ Created version info: {version_file}")
    
    # Create spec
    spec_file = create_optimized_spec()
    print(f"✅ Created spec: {spec_file}")
    
    # Clean previous builds
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    print("✅ Cleaned previous builds")
    
    # Build with PyInstaller
    try:
        cmd = [
            'pyinstaller',
            '--clean',
            '--noconfirm',
            '--log-level=WARN',
            spec_file
        ]
        
        print("🚀 Running PyInstaller...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Build successful!")
            
            # Check if exe was created
            exe_path = Path('dist/Kuroblock.exe')
            if exe_path.exists():
                size = exe_path.stat().st_size / (1024 * 1024)  # MB
                print(f"📦 Executable created: {exe_path}")
                print(f"📏 Size: {size:.1f} MB")
                
                # Create installer script
                create_installer()
                
                return True
            else:
                print("❌ Executable not found in dist folder")
                return False
        else:
            print("❌ Build failed!")
            print("Error output:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False

def create_installer():
    """Create installer batch script"""
    installer_content = '''@echo off
echo ========================================
echo    KUROBLOCK INSTALLER
echo ========================================
echo.
echo This will install Kuroblock to your system.
echo.
pause

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as Administrator - OK
) else (
    echo ERROR: Please run as Administrator!
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

REM Copy executable to Program Files
set "INSTALL_DIR=C:\\Program Files\\Kuroblock"
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

copy "Kuroblock.exe" "%INSTALL_DIR%\\" >nul
if %errorLevel% == 0 (
    echo ✅ Kuroblock installed successfully!
    echo.
    echo Location: %INSTALL_DIR%\\Kuroblock.exe
    echo.
    echo You can now run Kuroblock from:
    echo - Desktop shortcut (if created)
    echo - Start menu
    echo - Or directly from: %INSTALL_DIR%\\Kuroblock.exe
) else (
    echo ❌ Installation failed!
)

echo.
pause
'''
    
    with open('install_kuroblock.bat', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    print("✅ Created installer: install_kuroblock.bat")

def create_readme():
    """Create README for the release"""
    readme_content = '''# Kuroblock v1.0.0

## What is Kuroblock?
Kuroblock is a tool to block Wuthering Waves game servers for offline play.

## Files Included:
- `Kuroblock.exe` - Main executable
- `install_kuroblock.bat` - Installer script
- `README.md` - This file

## Installation:
1. Run `install_kuroblock.bat` as Administrator
2. Or run `Kuroblock.exe` directly (requires admin rights)

## Features:
- ✅ Block/unblock Wuthering Waves servers
- ✅ Automatic hosts file backup
- ✅ Multi-language support (English/Vietnamese)
- ✅ Clean and efficient code

## Version: 1.0.0
- Optimized code structure
- Added proper version information
- Reduced executable size

## License: MIT
'''
    
    with open('README_RELEASE.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✅ Created release README: README_RELEASE.md")

def main():
    """Main build process"""
    print("🚀 KUROBLOCK BUILD")
    print("=" * 40)
    
    # Check if source file exists
    if not os.path.exists('kuroblock_menu_optimized.py'):
        print("❌ Source file not found: kuroblock_menu_optimized.py")
        return
    
    # Check if icon exists
    if not os.path.exists('kuroblock.ico'):
        print("⚠️  Icon file not found: kuroblock.ico")
        print("   Building without icon...")
    
    # Build executable
    if build_executable():
        create_readme()
        
        print("\n🎉 BUILD COMPLETED SUCCESSFULLY!")
        print("=" * 40)
        print("📁 Files created:")
        print("   - dist/Kuroblock.exe")
        print("   - install_kuroblock.bat")
        print("   - README_RELEASE.md")
        print("\n📦 Ready for release!")
        
        # Clean up temporary files
        if os.path.exists('version_info.txt'):
            os.remove('version_info.txt')
        if os.path.exists('Kuroblock_optimized.spec'):
            os.remove('Kuroblock_optimized.spec')
        print("✅ Cleaned up temporary files")
        
    else:
        print("\n❌ BUILD FAILED!")
        print("Please check the error messages above.")

if __name__ == "__main__":
    main() 