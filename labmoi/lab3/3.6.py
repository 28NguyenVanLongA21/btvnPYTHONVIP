import pandas as pd

# Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('D:\Download\labmoi\lab3\stocks1.csv')
stocks2 = pd.read_csv('D:\Download\labmoi\lab3\stocks2.csv')

# Gộp stocks1 và stocks2 thành DataFrame mới
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Tạo Pivot Table với 'date' làm chỉ mục, 'symbol' làm cột và giá trị trung bình của 'close' làm giá trị
pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')

# Tính tổng volume giao dịch cho mỗi mã chứng khoán
volume_by_symbol = stocks.groupby('symbol')['volume'].sum()

# Thêm cột tổng volume vào Pivot Table
pivot_table['total_volume'] = pivot_table.columns.map(volume_by_symbol)

# Sắp xếp Pivot Table theo tổng volume giao dịch, từ cao xuống thấp
pivot_table_sorted = pivot_table['total_volume'].sort_values(ascending=False)

# Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(pivot_table_sorted.head(5))
