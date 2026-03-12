interface User {
    id: number;
    name: string;
}
const newUser: User = { id: 1, name: "Admin" };
console.log(newUser);
// Định nghĩa một Interface để quy định cấu trúc (khuôn mẫu) cho đối tượng User
interface User {
    id: number;   // Trường id bắt buộc phải là kiểu số
    name: string; // Trường name bắt buộc phải là kiểu chuỗi (văn bản)
}

// Khởi tạo một biến hằng (const) có tên là newUser
// Biến này được chỉ định kiểu dữ liệu là interface User đã định nghĩa ở trên
const newUser: User = { 
    id: 1, 
    name: "Admin" 
};

