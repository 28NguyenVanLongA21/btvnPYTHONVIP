import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Ellipse(Point):
    def __init__(self, x, y, semi_major_axis, semi_minor_axis):
        super().__init__(x, y)
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

class Circle(Ellipse):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)

def main():
    x = float(input("Nhập hoành độ của tâm elip: "))
    y = float(input("Nhập tung độ của tâm elip: "))
    semi_major_axis = float(input("Nhập bán trục lớn của elip: "))
    semi_minor_axis = float(input("Nhập bán trục nhỏ của elip: "))

    ellipse = Ellipse(x, y, semi_major_axis, semi_minor_axis)
    print(f"Diện tích của elip: {ellipse.area()}")

    radius = float(input("Nhập bán kính của đường tròn: "))
    circle = Circle(x, y, radius)
    print(f"Diện tích của đường tròn: {circle.area()}")

if __name__ == "__main__":
    main()
