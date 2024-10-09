class Stack:
    def __init__(self, size):

        self.size = size
        self.stack = []  # Dữ liệu là một danh sách
        self.top = -1  # Vị trí của phần tử trên cùng

    def is_empty(self):

        return self.top == -1

    def is_full(self):

        return self.top == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
        else:
            self.stack.append(value)
            self.top += 1

    def pop(self):

        if self.is_empty():
            print("Ngăn xếp rỗng. Không thể lấy phần tử.")
            return None
        else:
            value = self.stack.pop()
            self.top -= 1
            return value

    def count(self):

        return self.top + 1

    def __del__(self):
    
        self.stack.clear()
        print("Ngăn xếp đã được giải phóng.")

# Ví dụ sử dụng
if __name__ == "__main__":
    size = int(input("Nhập kích thước ngăn xếp: "))
    stack = Stack(size)

    while True:
        print("\n1. Đưa phần tử vào ngăn xếp (push)")
        print("2. Lấy phần tử ra từ ngăn xếp (pop)")
        print("3. Kiểm tra ngăn xếp rỗng (isEmpty)")
        print("4. Kiểm tra ngăn xếp đầy (isFull)")
        print("5. Đếm số phần tử trong ngăn xếp (count)")
        print("6. Thoát")

        choice = int(input("Chọn hành động: "))
        
        if choice == 1:
            value = float(input("Nhập giá trị để thêm vào ngăn xếp: "))
            stack.push(value)
        elif choice == 2:
            value = stack.pop()
            if value is not None:
                print(f"Phần tử lấy ra: {value}")
        elif choice == 3:
            print("Ngăn xếp rỗng." if stack.is_empty() else "Ngăn xếp không rỗng.")
        elif choice == 4:
            print("Ngăn xếp đầy." if stack.is_full() else "Ngăn xếp không đầy.")
        elif choice == 5:
            print(f"Số phần tử trong ngăn xếp: {stack.count()}")
        elif choice == 6:
            break
        else:
            print("Lựa chọn không hợp lệ.")
