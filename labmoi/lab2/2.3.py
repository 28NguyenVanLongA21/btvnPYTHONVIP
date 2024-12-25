import numpy as np

# Đọc dữ liệu từ file efficiency.txt
with open('efficiency.txt', 'r') as file:
    efficiency = [int(line.strip()) for line in file]

# Đọc dữ liệu từ file shifts.txt
with open('shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]

# In ra dữ liệu đã đọc
print("Dữ liệu hiệu suất sản xuất:", efficiency)
print("Dữ liệu ca làm việc:", shifts)

# Tạo numpy array từ list shifts
np_shifts = np.array(shifts)

# Kiểm tra kiểu dữ liệu của np_shifts
print("Kiểu dữ liệu của np_shifts:", np_shifts.dtype)

# Tạo numpy array từ list efficiency
np_efficiency = np.array(efficiency)

# Kiểm tra kiểu dữ liệu của np_efficiency
print("Kiểu dữ liệu của np_efficiency:", np_efficiency.dtype)

# Tính hiệu suất sản xuất trung bình của những nhân viên làm việc vào ca 'Morning'
morning_efficiency = np_efficiency[np_shifts == 'Morning']
average_morning_efficiency = np.mean(morning_efficiency)
print(f"Hiệu suất sản xuất trung bình của ca 'Morning': {average_morning_efficiency:.2f}")

# Tính hiệu suất sản xuất trung bình của những nhân viên làm việc trong các ca khác
other_shifts_efficiency = np_efficiency[np_shifts != 'Morning']
average_other_shifts_efficiency = np.mean(other_shifts_efficiency)
print(f"Hiệu suất sản xuất trung bình của các ca khác: {average_other_shifts_efficiency:.2f}")
