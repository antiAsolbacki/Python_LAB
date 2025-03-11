import math
from itertools import groupby

def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci(limit):
    fibs = [0, 1]
    while fibs[-1] + fibs[-2] < limit:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
# Danh sách số nguyên
numbers = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

# Xuất tất cả số lẻ không chia hết cho 5
odd_not_div_by_5 = [x for x in numbers if x % 2 == 1 and x % 5 != 0]
print("Số lẻ không chia hết cho 5:", odd_not_div_by_5)

# Xuất tất cả số Fibonacci
fib_numbers = [x for x in numbers if is_fibonacci(x)]
print("Số Fibonacci:", fib_numbers)

# Tìm số nguyên tố lớn nhất
prime_numbers = [x for x in numbers if is_prime(x)]
print("Số nguyên tố lớn nhất:", max(prime_numbers) if prime_numbers else None)

# Tìm số Fibonacci bé nhất
print("Số Fibonacci bé nhất:", min(fib_numbers) if fib_numbers else None)

# Tính trung bình các số lẻ
odd_numbers = [x for x in numbers if x % 2 == 1]
print("Trung bình số lẻ:", sum(odd_numbers) / len(odd_numbers) if odd_numbers else None)

# Tính tích các số lẻ không chia hết cho 3
def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

odd_not_div_by_3 = [x for x in numbers if x % 2 == 1 and x % 3 != 0]
print("Tích các số lẻ không chia hết cho 3:", product(odd_not_div_by_3))

# Đảo ngược danh sách
numbers.reverse()
print("Danh sách đảo ngược:", numbers)

# Xuất số lớn thứ nhì
print("Số lớn thứ nhì:", sorted(set(numbers))[-2] if len(set(numbers)) > 1 else None)

# Tính tổng chữ số của danh sách
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

total_digits_sum = sum(sum_of_digits(x) for x in numbers)
print("Tổng các chữ số:", total_digits_sum)

# Đếm số lần xuất hiện của một số
count_map = {x: numbers.count(x) for x in numbers}
print("Số lần xuất hiện:", count_map)

# Xuất các số xuất hiện n lần
n = 2  # Giả sử muốn tìm các số xuất hiện 2 lần
numbers_appearing_n_times = [k for k, v in count_map.items() if v == n]
print("Số xuất hiện n lần:", numbers_appearing_n_times)

# Xuất số xuất hiện nhiều nhất
max_occurrences = max(count_map.values())
numbers_most_frequent = [k for k, v in count_map.items() if v == max_occurrences]
print("Số xuất hiện nhiều nhất:", numbers_most_frequent)

# Bài tập hàm đệ quy

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def sum_fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + sum_fibonacci(n - 1)

def sum_sqrt_n(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n) + sum_sqrt_n(n - 1)

print("2.1. Tổng n số nguyên đầu tiên:", sum_n(10))
print("2.2. Giai thừa n:", factorial(5))
print("2.3. Tổng n số Fibonacci đầu tiên:", sum_fibonacci(5))
print("2.4. Tổng căn bậc 2 của n số nguyên đầu tiên:", sum_sqrt_n(5))
