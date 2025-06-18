@echo off
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
if not exist "C:\Program Files\Kuroblock" mkdir "C:\Program Files\Kuroblock"

REM Copy executable
copy "Kuroblock.exe" "C:\Program Files\Kuroblock\"

REM Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%%USERPROFILE%%\Desktop\Kuroblock.lnk'); $Shortcut.TargetPath = 'C:\Program Files\Kuroblock\Kuroblock.exe'; $Shortcut.Save()"

REM Create start menu shortcut
if not exist "%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\Kuroblock" mkdir "%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\Kuroblock"
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\Kuroblock\Kuroblock.lnk'); $Shortcut.TargetPath = 'C:\Program Files\Kuroblock\Kuroblock.exe'; $Shortcut.Save()"

echo.
echo [SUCCESS] Kuroblock installed successfully!
echo You can now run Kuroblock from:
echo - Desktop shortcut
echo - Start Menu
echo - C:\Program Files\Kuroblock\Kuroblock.exe
echo.
pause
