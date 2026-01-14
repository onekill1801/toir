#include <iostream>
#include <unistd.h>

int main() {
    int secret_value = 123456; // Đây là giá trị chúng ta sẽ đọc
    
    std::cout << "--- CHƯƠNG TRÌNH MỤC TIÊU ---" << std::endl;
    std::cout << "PID của chương trình: " << getpid() << std::endl;
    std::cout << "Địa chỉ của secret_value: " << &secret_value << std::endl;
    std::cout << "Giá trị hiện tại: " << secret_value << std::endl;
    
    std::cout << "Đang chờ bạn chạy script Python..." << std::endl;
    
    // Giữ chương trình chạy mãi để RAM không bị giải phóng
    while(true) {
        sleep(1);
    }
    
    return 0;
}