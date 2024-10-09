class HinhChuNhat:
    def __init__(self):
        self.canh_a = 0
        self.canh_b = 0

    def nhap_du_lieu(self):
        self.canh_a = float(input("Nhập độ dài cạnh a: "))
        self.canh_b = float(input("Nhập độ dài cạnh b: "))

    def tinh_chu_vi(self):
        return 2 * (self.canh_a + self.canh_b)

    def tinh_dien_tich(self):
        return self.canh_a * self.canh_b

    def in_thong_tin(self):
        chu_vi = self.tinh_chu_vi()
        dien_tich = self.tinh_dien_tich()
        print(f"Cạnh a: {self.canh_a}")
        print(f"Cạnh b: {self.canh_b}")
        print(f"Chu vi: {chu_vi}")
        print(f"Diện tích: {dien_tich}")

if __name__ == "__main__":
    hcn = HinhChuNhat()
    hcn.nhap_du_lieu()
    hcn.in_thong_tin()
