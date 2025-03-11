# Hàm xử lý danh sách số nguyên

def odd_numbers_not_divisible_by_5(lst):
    return [x for x in lst if x % 2 != 0 and x % 5 != 0]

def fibonacci_numbers(lst):
    return [x for x in lst if is_fibonacci(x)]

def max_prime(lst):
    primes = [x for x in lst if is_prime(x)]
    return max(primes) if primes else None

def min_fibonacci(lst):
    fibs = fibonacci_numbers(lst)
    return min(fibs) if fibs else None

def avg_odd(lst):
    odds = [x for x in lst if x % 2 != 0]
    return sum(odds) / len(odds) if odds else 0

def product_odd_not_div_3(lst):
    result = 1
    for x in lst:
        if x % 2 != 0 and x % 3 != 0:
            result *= x
    return result

def swap_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def reverse_list(lst):
    return lst[::-1]

def second_largest_numbers(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def sum_digits(lst):
    return sum(sum(int(digit) for digit in str(abs(x))) for x in lst)

def count_occurrences(lst, num):
    return lst.count(num)

def numbers_appearing_n_times(lst, n):
    return [x for x in set(lst) if lst.count(x) == n]

def most_frequent_numbers(lst):
    max_count = max(map(lst.count, lst))
    return [x for x in set(lst) if lst.count(x) == max_count]

# Chạy thử các hàm
if __name__ == "__main__":
    sample_list = [1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    print("Số lẻ không chia hết cho 5:", odd_numbers_not_divisible_by_5(sample_list))
    print("Số Fibonacci:", fibonacci_numbers(sample_list))
    print("Số nguyên tố lớn nhất:", max_prime(sample_list))
    print("Số Fibonacci bé nhất:", min_fibonacci(sample_list))
    print("Trung bình các số lẻ:", avg_odd(sample_list))
    print("Tích các số lẻ không chia hết cho 3:", product_odd_not_div_3(sample_list))
    print("Đổi chỗ phần tử:", swap_elements(sample_list, 1, 3))
    print("Đảo ngược danh sách:", reverse_list(sample_list))
    print("Số lớn thứ nhì:", second_largest_numbers(sample_list))
    print("Tổng các chữ số trong danh sách:", sum_digits(sample_list))
    print("Số xuất hiện 2 lần:", numbers_appearing_n_times(sample_list, 2))
    print("Số xuất hiện nhiều nhất:", most_frequent_numbers(sample_list))