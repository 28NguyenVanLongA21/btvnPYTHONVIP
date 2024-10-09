class TS:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

def main():
    danh_sach_thi_sinh = []
    so_thi_sinh = int(input("Nhập số lượng thí sinh: "))

    for _ in range(so_thi_sinh):
        ts = TS()
        ts.nhap_thong_tin()
        danh_sach_thi_sinh.append(ts)

    diem_chuan = 20
    thi_sinh_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]
    thi_sinh_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in thi_sinh_trung_tuyen:
        ts.in_thong_tin()
        print(f"Tổng điểm: {ts.tinh_tong_diem()}\n")

if __name__ == "__main__":
    main()
