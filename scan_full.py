import re

def scan_process_memory(pid, target_value_bytes):
    # 1. Đọc file maps để biết các vùng nhớ hợp lệ
    maps_path = f"/proc/{pid}/maps"
    mem_path = f"/proc/{pid}/mem"
    
    found_addresses = []

    with open(maps_path, 'r') as f_maps:
        for line in f_maps:
            # Chỉ quét các vùng nhớ có quyền đọc (r) và không phải là vùng nhớ hệ thống đặc biệt
            if 'r' in line.split()[1]:
                # Lấy địa chỉ bắt đầu và kết thúc (ví dụ: 00400000-0040c000)
                res = re.match(r'([0-9a-f]+)-([0-9a-f]+)', line)
                start = int(res.group(1), 16)
                end = int(res.group(2), 16)
                size = end - start

                try:
                    with open(mem_path, 'rb') as f_mem:
                        f_mem.seek(start)
                        chunk = f_mem.read(size)
                        
                        # Tìm kiếm chuỗi byte trong vùng nhớ này
                        index = chunk.find(target_value_bytes)
                        if index != -1:
                            found_addresses.append(hex(start + index))
                except Exception:
                    continue # Bỏ qua các vùng nhớ bị hệ thống chặn
    
    return found_addresses

# Ví dụ tìm số 123456 (dạng 4-byte little endian)
pid_to_scan = 3602376 # Thay bằng PID thực tế
target = (123456).to_bytes(4, byteorder='little')

results = scan_process_memory(pid_to_scan, target)
print(f"Tìm thấy giá trị tại: {results}")