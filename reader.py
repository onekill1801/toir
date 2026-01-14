import os
import struct

def read_memory(pid, address):
    # Đường dẫn đến file bộ nhớ của tiến trình
    mem_path = f"/proc/{pid}/mem"
    
    try:
        # Mở file ở chế độ đọc nhị phân (binary)
        with open(mem_path, "rb") as mem_file:
            # Nhảy đến đúng địa chỉ RAM
            mem_file.seek(address)
            
            # Đọc 4 byte (vì kiểu int trong C++ thường là 4 byte)
            chunk = mem_file.read(4)
            
            # Giải mã byte thành số nguyên (Little-endian)
            # 'i' đại diện cho kiểu int
            value = struct.unpack("<f", chunk)[0]
            return value
            
    except PermissionError:
        print("LỖI: Bạn phải chạy script bằng 'sudo' để có quyền đọc RAM của tiến trình khác.")
    except Exception as e:
        print(f"LỖI: {e}")

if __name__ == "__main__":
    # Nhập thông tin từ màn hình của chương trình C++
    target_pid = int(input("Nhập PID của chương trình C++: "))
    # Chuyển địa chỉ từ chuỗi Hex (0x...) sang số nguyên
    target_address = int(input("Nhập địa chỉ Hex (ví dụ: 0x7ffd...): "), 16)
    
    result = read_memory(target_pid, target_address)
    
    if result is not None:
        print(f"--- KẾT QUẢ ---")
        print(f"Giá trị đọc được từ RAM: {result}")
        if result == 123456:
            print("THÀNH CÔNG! Bạn đã đọc đúng giá trị bí mật.")