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
