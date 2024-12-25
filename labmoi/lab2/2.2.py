import numpy as np

# Đọc dữ liệu từ file CSV
data = np.genfromtxt('diem_hoc_phan.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)

# In ra dữ liệu để kiểm tra cấu trúc
print("Dữ liệu đọc được:")
print(data)

# Kiểm tra nếu data là mảng 1D, chúng ta cần phải xử lý lại
if data.ndim == 1:
    print("Dữ liệu là mảng 1D. Kiểm tra lại file CSV.")
else:
    # Nếu dữ liệu là mảng 2D, tiến hành tách cột
    ids = data[:, 0]  # ID sinh viên (cột đầu tiên)
    names = data[:, 1]  # Tên sinh viên (cột thứ hai)
    scores = data[:, 2:].astype(float)  # Điểm học phần (các cột còn lại)

    print("Dữ liệu điểm số:")
    print(scores)
