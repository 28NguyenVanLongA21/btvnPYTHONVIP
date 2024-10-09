import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class RightTriangle(Triangle):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__(base, height, math.sqrt(base**2 + height**2))

    def area(self):
        return 0.5 * self.base * self.height

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.a = self.b = math.sqrt((base / 2) ** 2 + height ** 2)
        super().__init__(self.a, self.a, base)

class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side_length):
        super().__init__(side_length, (math.sqrt(3) / 2) * side_length)

def main():
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))
    
    triangle = Triangle(a, b, c)
    print(f"Chu vi tam giác: {triangle.perimeter()}")
    print(f"Diện tích tam giác: {triangle.area()}")

    base = float(input("Nhập đáy của tam giác vuông: "))
    height = float(input("Nhập chiều cao của tam giác vuông: "))
    
    right_triangle = RightTriangle(base, height)
    print(f"Diện tích tam giác vuông: {right_triangle.area()}")

    base_isosceles = float(input("Nhập đáy của tam giác cân: "))
    height_isosceles = float(input("Nhập chiều cao của tam giác cân: "))
    
    isosceles_triangle = IsoscelesTriangle(base_isosceles, height_isosceles)
    print(f"Diện tích tam giác cân: {isosceles_triangle.area()}")

    side_length = float(input("Nhập cạnh của tam giác đều: "))
    
    equilateral_triangle = EquilateralTriangle(side_length)
    print(f"Diện tích tam giác đều: {equilateral_triangle.area()}")

if __name__ == "__main__":
    main()
