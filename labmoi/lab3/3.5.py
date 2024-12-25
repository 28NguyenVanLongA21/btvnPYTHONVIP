import pandas as pd

# Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('D:\Download\labmoi\lab3\stocks1.csv')
stocks2 = pd.read_csv('D:\Download\labmoi\lab3\stocks2.csv')

# Gộp stocks1 và stocks2 thành DataFrame mới
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Tạo MultiIndex với cột 'date' và 'symbol'
stocks.set_index(['date', 'symbol'], inplace=True)

# Sử dụng GroupBy để tính giá trung bình cho các cột 'open', 'high', 'low', 'close' và 'volume'
grouped_data = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',
    'high': 'mean',
    'low': 'mean',
    'close': 'mean',
    'volume': 'mean'
}).reset_index()

# Sắp xếp dữ liệu theo 'date' và 'symbol'
grouped_data.sort_values(by=['date', 'symbol'], inplace=True)

# Hiển thị kết quả cho 5 ngày đầu tiên
print("5 ngày đầu tiên:")
print(grouped_data.head())
