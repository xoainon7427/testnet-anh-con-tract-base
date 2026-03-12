version: '3'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
# Khai báo phiên bản định dạng của file Docker Compose (phiên bản 3)
version: '3'

# Định nghĩa danh sách các dịch vụ (containers) sẽ chạy trong hệ thống
services:
  # Tên của dịch vụ, ở đây đặt tên là 'web'
  web:
    # Chỉ định Image (hình ảnh mẫu) để khởi tạo container
    # nginx:latest nghĩa là sử dụng phần mềm máy chủ web Nginx phiên bản mới nhất
    image: nginx:latest

    # Cấu hình ánh xạ cổng (port mapping)
    ports:
      # "Cổng_Máy_Host : Cổng_Container"

