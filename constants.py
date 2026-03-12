<?php
$data = array("message" => "Hello from API", "status" => 200);
echo json_encode($data);
?>
<?php
// Khởi tạo một mảng liên kết (associative array) chứa dữ liệu muốn phản hồi
$data = array(
    "message" => "Hello from API", // Nội dung thông báo gửi đi
    "status" => 200                // Mã trạng thái (200 thường đại diện cho thành công - OK)
);

// json_encode: Hàm chuyển đổi mảng của PHP sang định dạng chuỗi JSON
// echo: Xuất kết quả trả về để các ứng dụng khác (Frontend, Mobile) có thể đọc được
echo json_encode($data);
?>
