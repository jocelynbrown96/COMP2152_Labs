# Lab 05: Recursion and Functions
# Student Name: Jocelyn Brown
# Date: Friday February 13th, 2026

# ============================================
# Question 1: Fibonacci Numbers (LeetCode #509)
# ============================================

def fibonacci(n):
    # Base cases:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case:
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases:
test_n = [0, 1, 2, 3, 4, 5, 10]
for n in test_n:
    result = fibonacci(n)
    print("Fibonacci(" + str(n) + ") = " + str(result))

# ============================================
# Question 2: FizzBuzz (LeetCode #412)
# ============================================

def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test case:
n = 15
print("\nFizzBuzz up to " + str(n) + ":")
print(fizz_buzz(n))

# ============================================
# Question 3: Binary Search (LeetCode #704)
# ============================================

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test cases:
test_cases = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5], 6),
    ([-1, 0, 3, 5, 9, 12], 9)
]
for nums, target in test_cases:
    result = binary_search(nums, target)
    print("\nArray: " + str(nums) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()