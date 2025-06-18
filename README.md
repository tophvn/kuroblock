# Kuroblock - Wuthering Waves Server Blocker

A tool to block Wuthering Waves game servers by modifying the hosts file, helping to minimize the risk of detection when using cheats or mods.

## Features

- 🔒 Blocks all Wuthering Waves data receiver servers
- 💾 Creates automatic backup of hosts file
- ✅ Checks and reports status of each domain
- 🗑️ Removes duplicate entries
- 🛡️ Requires administrator privileges for security
- 🧹 Includes hosts file cleaner for FitGirl entries
- 🌍 **NEW: Interactive menu with 3 options**

## Files

- `kuroblock_menu.py` - Main menu script with 3 options
- `clean_hosts.py` - FitGirl entries cleaner
- `build_kuroblock.py` - Build script for executable
- `kuroblock.ico` - Icon for the executable
- `dist/Kuroblock.exe` - Built executable (after running build script)

## Installation

### Option 1: Run as Administrator
1. Right-click `kuroblock_menu.py` → "Run as administrator"
2. Choose from the interactive menu

### Option 2: Build Executable
1. Run: `python build_kuroblock.py`
2. Use the generated `dist/Kuroblock.exe` with admin privileges

## Usage

### Interactive Menu (NEW!)
When you run the program, you'll see a menu with 4 options:

```
==================================================
   KUROBLOCK - WUTHERING WAVES
==================================================
1. Check current status
2. Block servers (for cheats)
3. Unblock servers (for online play)
4. Exit
```

### Command Line Usage
```bash
# Run Python script
python kuroblock_menu.py

# Or run executable (as Administrator)
.\dist\Kuroblock.exe
```

### Clean FitGirl Entries
```bash
# Run cleaner script
python clean_hosts.py

# Or use batch file (as Administrator)
clean_hosts.bat
```

## Blocked Domains

The following domains are blocked to prevent the game from sending data to servers:

- **as-datareceiver.aki-game.net** - Data receiver server for Asia region
- **eu-datareceiver.aki-game.net** - Data receiver server for Europe region
- **us-datareceiver.aki-game.net** - Data receiver server for North America region
- **hk-datareceiver.aki-game.net** - Data receiver server for Hong Kong
- **jp-datareceiver.aki-game.net** - Data receiver server for Japan
- **sea-datareceiver.aki-game.net** - Data receiver server for Southeast Asia
- **tw-datareceiver.aki-game.net** - Data receiver server for Taiwan
- **cn-datareceiver.aki-game.net** - Data receiver server for China
- **sentry.aki.kuro.com** - Error logging and reporting server (Sentry)

**Blocking purpose:**
- `datareceiver` domains receive data from game client (including cheat/mod information)
- `sentry` domain logs errors and sends reports to server
- Blocking these domains helps prevent servers from receiving information about unusual activities

## Backup Location

Backups are stored in: `C:\Windows\System32\drivers\etc\backups\`

## How it works

### Why block servers?
- When you use cheats in game, the game sends data to servers for verification
- Kuroblock blocks these domains by redirecting to `0.0.0.0` (no connection)
- Servers don't receive cheat reports → minimizes risk of ban

### Why run once?
- Hosts file is a system file, changes are permanent
- Block entries persist until manually removed
- No need to run again on each boot

## Important Notes

- ⚠️ **Only blocks reporting servers**, doesn't block local anti-cheat
- ⚠️ **Some games have strong anti-cheat** (Vanguard, BattlEye) that can still detect
- ⚠️ **Use at your own risk** - Still possible to get banned if detected
- ⚠️ **No 100% guarantee** - Only minimizes detection risk

