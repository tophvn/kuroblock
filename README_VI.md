# Kuroblock - Công cụ chặn server Wuthering Waves

Một công cụ để chặn các server của game Wuthering Waves bằng cách chỉnh sửa file hosts, giúp giảm thiểu khả năng bị phát hiện khi sử dụng cheat hoặc mod.

## Tính năng

- 🔒 Chặn tất cả server data receiver của Wuthering Waves
- 💾 Tự động tạo backup file hosts
- ✅ Kiểm tra và báo cáo trạng thái từng domain
- 🗑️ Xóa các entry trùng lặp
- 🛡️ Yêu cầu quyền Administrator để bảo mật
- 🌍 **Hỗ trợ đa ngôn ngữ (Tiếng Anh - Tiếng Việt)**

## Cài đặt

### Cách 1: Chạy với quyền Administrator
1. Chuột phải `kuroblock_menu.py` → "Run as administrator"
2. Chọn ngôn ngữ và tùy chọn từ menu

### Cách 2: Build file exe
1. Chạy: `python build_kuroblock.py`
2. Sử dụng file `dist/Kuroblock.exe` với quyền admin

## Cách sử dụng

### Menu tương tác (MỚI!)
Khi chạy chương trình, bạn sẽ thấy menu với 4 tùy chọn:

```
==================================================
   KUROBLOCK - WUTHERING WAVES
==================================================
1. Kiểm tra trạng thái hiện tại
2. Chặn server (để dùng cheat)
3. Bỏ chặn server
4. Thoát
```


### Sử dụng dòng lệnh
```bash
# Chạy script Python
python kuroblock_menu.py

# Hoặc chạy file exe (với quyền Administrator)
.\dist\Kuroblock.exe
```

## Domain bị chặn

Các domain sau đây bị chặn để ngăn game gửi dữ liệu về server:

- **as-datareceiver.aki-game.net** - Server nhận dữ liệu khu vực Châu Á
- **eu-datareceiver.aki-game.net** - Server nhận dữ liệu khu vực Châu Âu  
- **us-datareceiver.aki-game.net** - Server nhận dữ liệu khu vực Bắc Mỹ
- **hk-datareceiver.aki-game.net** - Server nhận dữ liệu Hong Kong
- **jp-datareceiver.aki-game.net** - Server nhận dữ liệu Nhật Bản
- **sea-datareceiver.aki-game.net** - Server nhận dữ liệu Đông Nam Á
- **tw-datareceiver.aki-game.net** - Server nhận dữ liệu Đài Loan
- **cn-datareceiver.aki-game.net** - Server nhận dữ liệu Trung Quốc
- **sentry.aki.kuro.com** - Server ghi log lỗi và báo cáo (Sentry)

**Mục đích chặn:**
- Các domain `datareceiver` nhận dữ liệu từ game client (bao gồm thông tin cheat/mod)
- Domain `sentry` ghi log lỗi và gửi báo cáo về server
- Chặn các domain này giúp ngăn server nhận được thông tin về hoạt động bất thường

## Vị trí backup

Backup được lưu tại: `C:\Windows\System32\drivers\etc\backups\`

## Cách hoạt động

### Tại sao cần chặn server?
- Khi bạn dùng cheat trong game, game sẽ gửi dữ liệu về server để kiểm tra
- Kuroblock chặn các domain này bằng cách redirect về `0.0.0.0` (không kết nối được)
- Server không nhận được báo cáo về cheat → giảm thiểu khả năng bị ban

### Tại sao chỉ cần chạy một lần?
- File hosts là file hệ thống, thay đổi sẽ được lưu vĩnh viễn
- Các entry block sẽ tồn tại cho đến khi bạn xóa thủ công
- Không cần chạy lại mỗi khi khởi động máy

## Lưu ý quan trọng

- ⚠️ **Chỉ chặn được server báo cáo**, không chặn được anti-cheat local
- ⚠️ **Một số game có anti-cheat mạnh** (Vanguard, BattlEye) vẫn phát hiện được
- ⚠️ **Sử dụng có rủi ro** - Vẫn có thể bị ban nếu bị phát hiện
- ⚠️ **Không đảm bảo 100%** - Chỉ giảm thiểu khả năng bị phát hiện
