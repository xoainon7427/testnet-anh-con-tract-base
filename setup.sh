using System;
class Program {
    static void Main() {
        Console.WriteLine("C# Program Running");
    }
}
using System; // Khai báo sử dụng không gian tên (namespace) System, nơi chứa các lớp cơ bản như Console

// Định nghĩa một lớp (class) có tên là Program để bao bọc mã nguồn
class Program {
    
    // Hàm Main là điểm bắt đầu (entry point) của mọi ứng dụng C#
    // static: Giúp hàm có thể chạy ngay mà không cần khởi tạo đối tượng từ lớp Program
    // void: Thông báo rằng hàm này không trả về giá trị nào sau khi chạy xong
    static void Main() {
        
        // Console.WriteLine: Lệnh dùng để in nội dung ra màn hình console và tự động xuống dòng
        Console.WriteLine("C# Program Running");
    }
}
