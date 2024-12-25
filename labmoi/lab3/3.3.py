import pandas as pd

# Đọc file CSV vào DataFrame
stocks1 = pd.read_csv('D:\Download\labmoi\lab3\stocks1.csv')
stocks2 = pd.read_csv('D:\Download\labmoi\lab3\stocks2.csv')

# Gộp stocks1 và stocks2 thành DataFrame mới
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Tính giá trung bình (open, high, low, close) cho mỗi ngày
stocks['average'] = stocks[['open', 'high', 'low', 'close']].mean(axis=1)

# Hiển thị 5 dòng đầu tiên của kết quả
print("5 dòng đầu tiên của kết quả với giá trung bình:")
print(stocks[['date', 'open', 'high', 'low', 'close', 'average']].head())
