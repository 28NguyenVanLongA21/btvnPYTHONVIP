class Date:
    def __init__(self, day=1, month=1, year=1900):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")

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

class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    def display_info(self):
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.start_date.display()

if __name__ == "__main__":
    name = input("Nhập họ tên nhân viên: ")
    
    day_birth = int(input("Nhập ngày sinh: "))
    month_birth = int(input("Nhập tháng sinh: "))
    year_birth = int(input("Nhập năm sinh: "))
    birth_date = Date(day_birth, month_birth, year_birth)

    day_start = int(input("Nhập ngày vào công ty: "))
    month_start = int(input("Nhập tháng vào công ty: "))
    year_start = int(input("Nhập năm vào công ty: "))
    start_date = Date(day_start, month_start, year_start)

    employee = Employee(name, birth_date, start_date)

    print("\nThông tin nhân viên:")
    employee.display_info()
