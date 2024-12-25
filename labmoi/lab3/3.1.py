import pandas as pd

# Đọc file CSV vào DataFrame
stocks1 = pd.read_csv('D:\Download\labmoi\lab3\stocks1.csv')

# Hiển thị 5 dòng đầu tiên của stocks1
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

# Hiển thị kiểu dữ liệu của mỗi cột trong stocks1
print("\nKiểu dữ liệu của mỗi cột trong stocks1:")
print(stocks1.dtypes)

# Hiển thị thông tin tổng quan của stocks1
print("\nThông tin tổng quan của stocks1:")
print(stocks1.info())
