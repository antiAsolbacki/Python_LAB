import math

# (a + b)
def add(a,b):
     return a + b
# a/b
def divide(a,b):
    if b == 0:
        return "cannot divide for 0"
    return a / b 
#a^b
def power (a,b):
    return a**b
# Tính diện tích hình chữ nhật khi biết bán kính
def dt_hcn (r):
    return(2*r)**2
# xuat tat ca cac so nguyen to  
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# tìm tất cả số nguyên tố trong một khoảng
def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

# Hàm kiểm tra một số có phải là số Fibonacci hay không
def is_fibonacci(n):
    def perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    return perfect_square(5 * n * n + 4) or perfect_square(5 * n * n - 4)

# Hàm tìm số Fibonacci thứ n bằng đệ quy
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# Hàm tìm số Fibonacci thứ n không dùng đệ quy
def fibonacci_non_recursive(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# Hàm tính tổng n số Fibonacci đầu tiên bằng đệ quy
def sum_fibonacci_recursive(n):
    if n <= 0:
        return 0
    return fibonacci_recursive(n) + sum_fibonacci_recursive(n - 1)

# Hàm tính tổng n số Fibonacci đầu tiên không dùng đệ quy
def sum_fibonacci_non_recursive(n):
    a, b, total = 0, 1, 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

# Hàm tính tổng căn bậc 2 của n số nguyên đầu tiên
def sum_square_roots(n):
    return sum(math.sqrt(i) for i in range(1, n + 1))

# Hàm giải phương trình bậc 2 ax^2 + bx + c = 0
def solve_quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

# Hàm tính giai thừa của một số nguyên n
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

#In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
def print_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
# Hàm đổi số giây thành giờ:phút:giây
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{hours}:{minutes}:{sec}"

if __name__ == "__main__":
    print("Tổng 5 + 3:", add(5, 3))
    print("Chia 10 / 2:", divide(10, 2))
    print("Lũy thừa 2^3:", power(2, 3))
    print("Diện tích hình chữ nhật có bán kính đường tròn ngoại tiếp 5:", rectangle_area_from_radius(5))
    print("Số nguyên tố trong khoảng 10-50:", primes_in_range(10, 50))
    print("Số 21 có phải là số Fibonacci không?", is_fibonacci(21))
    print("Số Fibonacci thứ 10 (đệ quy):", fibonacci_recursive(10))
    print("Số Fibonacci thứ 10 (không đệ quy):", fibonacci_non_recursive(10))
    print("Tổng 10 số Fibonacci đầu tiên (đệ quy):", sum_fibonacci_recursive(10))
    print("Tổng 10 số Fibonacci đầu tiên (không đệ quy):", sum_fibonacci_non_recursive(10))
    print("Tổng căn bậc 2 của 5 số nguyên đầu tiên:", sum_square_roots(5))
    print("Giải phương trình bậc 2 x^2 - 3x + 2 = 0:", solve_quadratic(1, -3, 2))
    print("Giai thừa của 5:", factorial(5))
    print("In tam giác * với n = 5:")
    print_triangle(5)
    print("Chuyển đổi 4690 giây thành giờ:phút:giây:", convert_seconds(4690))