#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuroblock Menu - Main interface for Wuthering Waves blocking
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime

class KuroblockMenu:
    def __init__(self):
        self.hosts_file = r"C:\Windows\System32\drivers\etc\hosts"
        self.backup_dir = Path(r"C:\Windows\System32\drivers\etc\backups")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self.wuwa_servers = [
            "as-datareceiver.aki-game.net",
            "eu-datareceiver.aki-game.net",
            "us-datareceiver.aki-game.net",
            "hk-datareceiver.aki-game.net",
            "jp-datareceiver.aki-game.net",
            "sea-datareceiver.aki-game.net",
            "tw-datareceiver.aki-game.net",
            "cn-datareceiver.aki-game.net",
            "sentry.aki.kuro.com"
        ]
        self.block_ip = "0.0.0.0"
        self.language = "en"  # Default language
        
        # Language texts
        self.texts = {
            "en": {
                "title": "KUROBLOCK - WUTHERING WAVES",
                "check_status": "Check current status",
                "block_servers": "Block servers (for cheats)",
                "unblock_servers": "Unblock servers (for online play)",
                "exit": "Exit",
                "select_option": "Select option (1-4): ",
                "invalid_choice": "Invalid choice! Please select 1-4.",
                "goodbye": "Goodbye!",
                "press_enter": "Press Enter to continue...",
                "status_title": "WUTHERING WAVES BLOCK STATUS",
                "checking": "Checking domain blocking status...",
                "blocked": "BLOCKED",
                "not_blocked": "NOT BLOCKED",
                "summary": "Summary:",
                "domains_blocked": "domains blocked",
                "all_blocked": "ALL DOMAINS ARE BLOCKED!",
                "can_use_cheats": "You can use cheats safely.",
                "partially_blocked": "PARTIALLY BLOCKED",
                "some_not_blocked": "Some domains are not blocked.",
                "no_domains_blocked": "NO DOMAINS BLOCKED",
                "can_play_online": "You can play online normally.",
                "hosts_not_found": "Hosts file not found!",
                "error_reading": "Error reading hosts file:",
                "block_title": "BLOCKING WUTHERING WAVES SERVERS",
                "unblock_title": "UNBLOCKING WUTHERING WAVES SERVERS",
                "need_admin": "Please run as Administrator!",
                "backup_created": "Created backup:",
                "backup_failed": "Backup failed:",
                "all_already_blocked": "All domains are already blocked!",
                "added_blocks": "Added",
                "new_blocks": "new blocks",
                "blocked_successfully": "Wuthering Waves servers blocked successfully!",
                "error_writing": "Error writing hosts file:",
                "removed": "Removed:",
                "removed_blocks": "Successfully removed",
                "unblocked_successfully": "Wuthering Waves servers unblocked!",
                "language_menu": "Language / Ngôn ngữ:",
                "english": "English",
                "vietnamese": "Vietnamese"
            },
            "vi": {
                "title": "KUROBLOCK - WUTHERING WAVES",
                "check_status": "Kiểm tra trạng thái hiện tại",
                "block_servers": "Chặn server (để dùng cheat)",
                "unblock_servers": "Bỏ chặn server (để chơi online)",
                "exit": "Thoát",
                "select_option": "Chọn tùy chọn (1-4): ",
                "invalid_choice": "Lựa chọn không hợp lệ! Vui lòng chọn 1-4.",
                "goodbye": "Tạm biệt!",
                "press_enter": "Nhấn Enter để tiếp tục...",
                "status_title": "TRẠNG THÁI CHẶN WUTHERING WAVES",
                "checking": "Đang kiểm tra trạng thái chặn domain...",
                "blocked": "ĐÃ CHẶN",
                "not_blocked": "CHƯA CHẶN",
                "summary": "Tóm tắt:",
                "domains_blocked": "domain đã chặn",
                "all_blocked": "TẤT CẢ DOMAIN ĐÃ ĐƯỢC CHẶN!",
                "can_use_cheats": "Bạn có thể dùng cheat an toàn.",
                "partially_blocked": "CHẶN MỘT PHẦN",
                "some_not_blocked": "Một số domain chưa được chặn.",
                "no_domains_blocked": "KHÔNG CÓ DOMAIN NÀO BỊ CHẶN",
                "can_play_online": "Bạn có thể chơi online bình thường.",
                "hosts_not_found": "Không tìm thấy file hosts!",
                "error_reading": "Lỗi đọc file hosts:",
                "block_title": "CHẶN SERVER WUTHERING WAVES",
                "unblock_title": "BỎ CHẶN SERVER WUTHERING WAVES",
                "need_admin": "Vui lòng chạy với quyền Administrator!",
                "backup_created": "Đã tạo backup:",
                "backup_failed": "Tạo backup thất bại:",
                "all_already_blocked": "Tất cả domain đã được chặn!",
                "added_blocks": "Đã thêm",
                "new_blocks": "block mới",
                "blocked_successfully": "Đã chặn server Wuthering Waves thành công!",
                "error_writing": "Lỗi ghi file hosts:",
                "removed": "Đã xóa:",
                "removed_blocks": "Đã xóa thành công",
                "unblocked_successfully": "Đã bỏ chặn server Wuthering Waves!",
                "language_menu": "Language / Ngôn ngữ:",
                "english": "English",
                "vietnamese": "Vietnamese"
            }
        }

    def check_admin(self):
        try:
            return os.getuid() == 0
        except AttributeError:
            try:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

    def t(self, key):
        """Get translated text"""
        return self.texts[self.language].get(key, key)

    def select_language(self):
        """Select language"""
        print("=" * 50)
        print("   " + self.t("language_menu"))
        print("=" * 50)
        print("1. " + self.t("english"))
        print("2. " + self.t("vietnamese"))
        
        choice = input("\nSelect language / Chọn ngôn ngữ (1-2): ").strip()
        if choice == "2":
            self.language = "vi"
        else:
            self.language = "en"

    def show_status(self):
        """Check current blocking status"""
        print("\n" + "=" * 50)
        print("   " + self.t("status_title"))
        print("=" * 50)
        
        if not os.path.exists(self.hosts_file):
            print("❌ " + self.t("hosts_not_found"))
            return
        
        try:
            with open(self.hosts_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print("❌ " + self.t("error_reading") + f" {e}")
            return
        
        print("\n🔍 " + self.t("checking") + "\n")
        
        blocked_count = 0
        for server in self.wuwa_servers:
            if f"{self.block_ip} {server}" in content:
                print(f"✅ {server} - " + self.t("blocked"))
                blocked_count += 1
            else:
                print(f"❌ {server} - " + self.t("not_blocked"))
        
        print(f"\n📊 {self.t('summary')}")
        print(f"   {self.t('blocked')}: {blocked_count}/{len(self.wuwa_servers)} {self.t('domains_blocked')}")
        
        if blocked_count == len(self.wuwa_servers):
            print("\n🎉 " + self.t("all_blocked"))
            print("   " + self.t("can_use_cheats"))
        elif blocked_count > 0:
            print("\n⚠️  " + self.t("partially_blocked"))
            print("   " + self.t("some_not_blocked"))
        else:
            print("\n❌ " + self.t("no_domains_blocked"))
            print("   " + self.t("can_play_online"))

    def block_domains(self):
        """Block Wuthering Waves domains"""
        print("\n" + "=" * 50)
        print("   " + self.t("block_title"))
        print("=" * 50)
        
        if not self.check_admin():
            print("❌ " + self.t("need_admin"))
            return
        
        # Create backup
        if not os.path.exists(self.hosts_file):
            print("❌ " + self.t("hosts_not_found"))
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"kuroblock_backup_{timestamp}.bak"
        try:
            shutil.copy2(self.hosts_file, backup_file)
            print("✅ " + self.t("backup_created") + f" {backup_file}")
        except Exception as e:
            print("❌ " + self.t("backup_failed") + f" {e}")
            return
        
        # Check current status
        try:
            with open(self.hosts_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print("❌ " + self.t("error_reading") + f" {e}")
            return
        
        # Check which domains need blocking
        new_entries = []
        for server in self.wuwa_servers:
            entry = f"{self.block_ip} {server}"
            if entry not in content:
                new_entries.append(entry)
        
        if not new_entries:
            print("✅ " + self.t("all_already_blocked"))
            return
        
        # Add missing blocks
        try:
            with open(self.hosts_file, 'a', encoding='utf-8') as f:
                f.write('\n' + '\n'.join(new_entries) + '\n')
            print("✅ " + self.t("added_blocks") + f" {len(new_entries)} " + self.t("new_blocks"))
            print("🎉 " + self.t("blocked_successfully"))
            print("   " + self.t("can_use_cheats"))
        except Exception as e:
            print("❌ " + self.t("error_writing") + f" {e}")

    def unblock_domains(self):
        """Unblock Wuthering Waves domains"""
        print("\n" + "=" * 50)
        print("   " + self.t("unblock_title"))
        print("=" * 50)
        
        if not self.check_admin():
            print("❌ " + self.t("need_admin"))
            return
        
        # Create backup
        if not os.path.exists(self.hosts_file):
            print("❌ " + self.t("hosts_not_found"))
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"kuroblock_unblock_backup_{timestamp}.bak"
        try:
            shutil.copy2(self.hosts_file, backup_file)
            print("✅ " + self.t("backup_created") + f" {backup_file}")
        except Exception as e:
            print("❌ " + self.t("backup_failed") + f" {e}")
            return
        
        # Remove Wuthering Waves blocks
        try:
            with open(self.hosts_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print("❌ " + self.t("error_reading") + f" {e}")
            return
        
        # Filter out Wuthering Waves blocks
        cleaned_lines = []
        removed_count = 0
        
        for line in lines:
            should_keep = True
            for server in self.wuwa_servers:
                if f"{self.block_ip} {server}" in line:
                    should_keep = False
                    removed_count += 1
                    print("🗑️  " + self.t("removed") + f" {line.strip()}")
                    break
            
            if should_keep:
                cleaned_lines.append(line)
        
        # Write cleaned content back
        try:
            with open(self.hosts_file, 'w', encoding='utf-8') as f:
                f.writelines(cleaned_lines)
            print("\n✅ " + self.t("removed_blocks") + f" {removed_count} " + self.t("new_blocks"))
            print("🎉 " + self.t("unblocked_successfully"))
            print("   " + self.t("can_play_online"))
        except Exception as e:
            print("❌ " + self.t("error_writing") + f" {e}")

    def show_menu(self):
        while True:
            print("\n" + "=" * 50)
            print("   " + self.t("title"))
            print("=" * 50)
            print("1. " + self.t("check_status"))
            print("2. " + self.t("block_servers"))
            print("3. " + self.t("unblock_servers"))
            print("4. " + self.t("exit"))
            
            choice = input("\n" + self.t("select_option")).strip()
            
            if choice == "1":
                self.show_status()
            elif choice == "2":
                self.block_domains()
            elif choice == "3":
                self.unblock_domains()
            elif choice == "4":
                print("👋 " + self.t("goodbye"))
                break
            else:
                print("❌ " + self.t("invalid_choice"))
            
            if choice in ["1", "2", "3"]:
                input("\n" + self.t("press_enter"))

def main():
    menu = KuroblockMenu()
    
    if not menu.check_admin():
        print("=" * 50)
        print("   " + menu.t("title"))
        print("=" * 50)
        print("❌ " + menu.t("need_admin"))
        print("Right-click and select 'Run as administrator'")
        input("\nPress Enter to exit...")
        return
    
    # Select language first
    menu.select_language()
    
    # Show main menu
    menu.show_menu()

if __name__ == "__main__":
    main() 