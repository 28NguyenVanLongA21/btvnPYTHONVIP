import math

class Polygon:
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        return self.num_sides * self.side_length

    def area(self):
        return (self.num_sides * self.side_length ** 2) / (4 * math.tan(math.pi / self.num_sides))

class Parallelogram(Polygon):
    def __init__(self, base, height):
        super().__init__(4, base)
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

def main():
    side_length = float(input("Nhập độ dài cạnh của hình vuông: "))
    square = Square(side_length)
    print(f"Chu vi hình vuông: {square.perimeter()}")
    print(f"Diện tích hình vuông: {square.area()}")

    width = float(input("Nhập chiều rộng của hình chữ nhật: "))
    height = float(input("Nhập chiều cao của hình chữ nhật: "))
    rectangle = Rectangle(width, height)
    print(f"Chu vi hình chữ nhật: {rectangle.perimeter()}")
    print(f"Diện tích hình chữ nhật: {rectangle.area()}")

    base = float(input("Nhập độ dài đáy của hình bình hành: "))
    height = float(input("Nhập chiều cao của hình bình hành: "))
    parallelogram = Parallelogram(base, height)
    print(f"Diện tích hình bình hành: {parallelogram.area()}")

    num_sides = int(input("Nhập số cạnh của đa giác: "))
    side_length = float(input("Nhập độ dài cạnh của đa giác: "))
    polygon = Polygon(num_sides, side_length)
    print(f"Chu vi đa giác: {polygon.perimeter()}")
    print(f"Diện tích đa giác: {polygon.area()}")

if __name__ == "__main__":
    main()
