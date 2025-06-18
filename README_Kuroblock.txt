# Kuroblock.exe

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
2. The executable will be installed to `C:\Program Files\Kuroblock\`
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
Backups are stored in: `C:\Windows\System32\drivers\etc\backups\`

## Warning
This tool modifies system files. Always run as Administrator.
Use at your own risk. Modifying game files may violate terms of service.
Keep backups of your hosts file before using.

## Build Information
- Built with PyInstaller
- Python version: 3.12
- Single file executable
- No external dependencies required
