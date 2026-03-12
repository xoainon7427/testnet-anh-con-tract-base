import datetime
def get_current_time():
    return datetime.datetime.now()
print("Current time:", get_current_time())
# Nhập (import) thư viện datetime tích hợp sẵn của Python để xử lý ngày tháng và thời gian
import datetime

# Định nghĩa một hàm có tên là get_current_time để tái sử dụng khi cần lấy thời gian
def get_current_time():
    # Sử dụng phương thức .now() của lớp datetime để lấy mốc thời gian chính xác tại thời điểm gọi hàm
    # Giá trị trả về bao gồm: Năm, tháng, ngày, giờ, phút, giây và phần triệu giây (microsecond)
    return datetime.datetime.now()

# Gọi hàm get_current_time() để lấy kết quả và in ra màn hình console cùng với thông báo
print("Current time:", get_current_time())
