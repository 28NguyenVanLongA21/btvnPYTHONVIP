class Date:
    def __init__(self, day=1, month=1, year=1900):

        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")

    def is_leap_year(self, year):

        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month, year):

        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        return 0

    def next(self):
   
        self.day += 1
        if self.day > self.days_in_month(self.month, self.year):
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

# Ví dụ sử dụng
if __name__ == "__main__":
    date = Date(28, 2, 2024)  # Ngày 28 tháng 2 năm 2024 (năm nhuận)
    
    date.display()  # In thông tin ngày hiện tại
    date.next()     # Tính ngày tiếp theo
    date.display()  # In thông tin ngày tiếp theo
