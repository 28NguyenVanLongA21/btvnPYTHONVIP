import pandas as pd

# Đọc file stocks1.csv vào DataFrame stocks1
stocks1 = pd.read_csv('D:\Download\labmoi\lab3\stocks1.csv')

# Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv('D:\Download\labmoi\lab3\stocks2.csv')

# Gộp stocks1 và stocks2 thành DataFrame mới
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Đọc file companies.csv vào DataFrame companies
companies = pd.read_csv('D:\Download\labmoi\lab3\companies.csv')

# Hiển thị 5 dòng đầu tiên của companies
print("5 dòng đầu tiên của companies:")
print(companies.head())

# Kết hợp stocks và companies dựa trên cột 'name' (công ty) và 'symbol' (mã chứng khoán)
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name', how='inner')

# Hiển thị 5 dòng đầu tiên của dữ liệu đã kết hợp
print("\n5 dòng đầu tiên của dữ liệu đã kết hợp:")
print(merged_data.head())

# Tính giá đóng cửa trung bình cho mỗi công ty
average_close = merged_data.groupby('name')['close'].mean().reset_index()

# Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình cho 5 công ty đầu tiên:")
print(average_close.head())
