class PS:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1 

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        while True:
            self.mau_so = int(input("Nhập mẫu số (khác 0): "))
            if self.kiem_tra_hop_le():
                break
            else:
                print("Mẫu số không hợp lệ. Vui lòng nhập lại.")

    def in_phan_so(self):
        """In phân số ra màn hình"""
        if self.kiem_tra_hop_le():
            print(f"Phân số: {self.tu_so}/{self.mau_so}")
        else:
            print("Phân số không hợp lệ.")

if __name__ == "__main__":
    ps = PS()
    ps.nhap_phan_so()
    ps.in_phan_so()
