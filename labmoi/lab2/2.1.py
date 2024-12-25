import numpy as np

# Tạo dữ liệu nhiệt độ hàng ngày trong một tháng (30 ngày)
np.random.seed(0)  # Để kết quả tái hiện được
temperatures = np.round(np.random.uniform(15, 35, size=30), 2)  # Nhiệt độ từ 15 đến 35 độ C

# Tính nhiệt độ trung bình
average_temp = np.mean(temperatures)
print("Nhiệt độ hàng ngày:", temperatures)
print("Nhiệt độ trung bình trong tháng:", round(average_temp, 2))
# Xác định ngày có nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
day_max_temp = np.argmax(temperatures) + 1  # Ngày bắt đầu từ 1
day_min_temp = np.argmin(temperatures) + 1

print(f"Nhiệt độ cao nhất: {max_temp}°C, vào ngày thứ {day_max_temp}")
print(f"Nhiệt độ thấp nhất: {min_temp}°C, vào ngày thứ {day_min_temp}")

# Chênh lệch nhiệt độ giữa các ngày
temp_diff = np.abs(np.diff(temperatures))  # Hiệu nhiệt độ giữa các ngày liên tiếp
max_diff = np.max(temp_diff)
day_max_diff = np.argmax(temp_diff) + 1  # Ngày đầu tiên trong khoảng chênh lệch

print(f"Ngày có sự biến đổi nhiệt độ cao nhất là ngày {day_max_diff} với chênh lệch {round(max_diff, 2)}°C")
# Các ngày có nhiệt độ cao hơn 20°C
days_above_20 = np.where(temperatures > 20)[0] + 1
print("Các ngày có nhiệt độ cao hơn 20°C:", days_above_20)

# Lấy nhiệt độ của ngày 5, 10, 15, 20, và 25
specific_days = [5, 10, 15, 20, 25]
specific_temps = temperatures[np.array(specific_days) - 1]
print("Nhiệt độ của ngày 5, 10, 15, 20, và 25:", specific_temps)

# Nhiệt độ của các ngày có nhiệt độ trên trung bình
above_average_temps = temperatures[temperatures > average_temp]
print("Nhiệt độ của các ngày trên trung bình:", above_average_temps)

# Lấy nhiệt độ của các ngày chẵn và lẻ
even_days_temps = temperatures[1::2]  # Ngày chẵn
odd_days_temps = temperatures[0::2]   # Ngày lẻ

print("Nhiệt độ của các ngày chẵn:", even_days_temps)
print("Nhiệt độ của các ngày lẻ:", odd_days_temps)
