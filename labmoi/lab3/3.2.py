import pandas as pd

# Đọc file CSV vào DataFrame
stocks1 = pd.read_csv('D:\Download\labmoi\lab3\stocks1.csv')

# Kiểm tra dữ liệu Null trong stocks1
null_data = stocks1.isnull().sum()
print("Số lượng dữ liệu Null trong mỗi cột:")
print(null_data)

# Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
stocks1['high'] = stocks1['high'].fillna(stocks1['high'].mean())

# Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
stocks1['low'] = stocks1['low'].fillna(stocks1['low'].mean())

# Hiển thị thông tin tổng quan của stocks1 để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
print(stocks1.info())
