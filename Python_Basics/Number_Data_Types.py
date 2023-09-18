
# # Integer
# x = 42
# print(abs(x))           # Output: 42
# print(bool(x))          # Output: True
# print(int(x))           # Output: 42
# print(float(x))         # Output: 42.0
# print(complex(x))       # Output: (42+0j)
# print(round(x, -1))     # Output: 40
# print(hash(x))          # Output: 42
# print(x.bit_length())  # Output: 6
# # print(x.hex())         # Output: '0x2a'
# print(x.to_bytes(2, byteorder='big'))  # Output: b'\x00*'
# print(int('1010', 2))  # Output: 10
# print()

# # Float
# y = 3.14
# print(abs(y))           # Output: 3.14
# print(bool(y))          # Output: True
# print(int(y))           # Output: 3
# print(float(y))         # Output: 3.14
# print(complex(y))       # Output: (3.14+0j)
# print(round(y, 1))      # Output: 3.1
# print(hash(y))          # Output: 1152921504606847031
# print(y)
# print(y.as_integer_ratio())  # Output: (7070651414971679, 2251799813685248)
# print(y.hex())               # Output: '0x1.91eb851eb851fp+1'
# print(y.is_integer())        # Output: False
# print(y.real)
# print()

# # Complex
# z = 1 + 2j
# print(abs(z))           # Output: 2.23606797749979
# print(bool(z))          # Output: True
# # print(int(z))           # Output: TypeError: can't convert complex to int
# # print(float(z))         # Output: TypeError: can't convert complex to float
# print(complex(z))       # Output: (1+2j)
# # print(round(z, 1))      # Output: TypeError: type complex doesn't define __round__ method
# # print(hash(z))          # Output: TypeError: unhashable type: 'complex'
# print(z.real)        # Output: 1.0
# print(z.imag)        # Output: 2.0
# print(z.conjugate()) # Output: (1-2j)

# print(max([1, 5, 3]))  # Output: 5
# print(min([1, 5, 3]))  # Output: 1
# print(sum([1, 2, 3]))  # Output: 6

# print(int(y))  # Output: 3
# print(float(x))  # Output: -10.0
# print(complex(2, 3))  # Output: (2+3j)

# print(bin(10))  # Output: '0b1010'
# print(hex(255))  # Output: '0xff'
# print(oct(64))  # Output: '0o100'
# print(chr(65))  # Output: 'A'
# print(ord('A'))  # Output: 65

# # ''''''''''''''''''''''Numeric Types  Advanced Concepts for competitive programming''''''''''''''''''
# # ''''''''''''''''1.Fast I/O''''''''''''''
# import sys

# # Using sys.stdin.readline() for fast input
# n = int(sys.stdin.readline().strip())

# # Using sys.stdout.write() for fast output
# sys.stdout.write(str(n) + "\n")

# # ''''''''''''''''''2. Modular Arithmatics'''''''''''''''''''''
# MOD = 10**9 + 7

# # Fast modular exponentiation
# def power(base, exp):
#     result = 1
#     while exp > 0:
#         if exp % 2 == 1:
#             result = (result * base) % MOD
#         base = (base * base) % MOD
#         exp //= 2
#     return result

# # Example: Compute (a^b) % MOD
# a=5
# b=2
# result = power(a , b)
# print(result)

# # '''''''''''''''''3.Bitwise Operations'''''''''''''''''
# # Example: Count the number of set bits in a number
# def count_set_bits(n):
#     count = 0
#     while n:
#         count += n & 1
#         n >>= 1
#     return count

# num = 42
# print(count_set_bits(num))

# # '''''''''''''''''''''''4. Prime Number Generation:'''''''''''''''''''''''
# # Sieve of Eratosthenes to find prime numbers up to a given limit
# def sieve(limit):
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False

#     for num in range(2, int(limit**0.5) + 1):
#         if is_prime[num]:
#             for multiple in range(num * num, limit + 1, num):
#                 is_prime[multiple] = False

#     primes = [num for num in range(2, limit + 1) if is_prime[num]]
#     return primes

# primes_up_to_20 = sieve(20)
# print(primes_up_to_20)

# # ''''''''''''''''''''''''''5. Number Theory'''''''''''''''''''''''
# import math

# # Using math.gcd() to find the GCD of two numbers
# a = 42
# b = 56
# gcd_ab = math.gcd(a, b)
# print(gcd_ab)

# # ''''''''''''''''''''''''6. Two Pointers Technique:''''''''''''''''''
# # Using the two pointers technique to find if there exists a pair with a given sum in a sorted array
# def has_pair_with_sum(arr, target_sum):
#     left, right = 0, len(arr) - 1
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_sum:
#             return True
#         elif current_sum < target_sum:
#             left += 1
#         else:
#             right -= 1
#     return False

# sorted_array = [1, 3, 5, 7, 9]
# target = 12
# print(has_pair_with_sum(sorted_array, target))

# # '''''''''''''''''''''''''''7. Modular Arithmetic and Fast Exponentiation:''''''''''''''''''''''''''''''''''''''''''
# # Modular Arithmetic (a * b) % mod
# def multiply_mod(a, b, mod):
#     return (a % mod * b % mod) % mod

# # Fast Exponentiation (a^b) % mod
# def power_mod(a, b, mod):
#     res = 1
#     while b > 0:
#         if b & 1:
#             res = multiply_mod(res, a, mod)
#         a = multiply_mod(a, a, mod)
#         b >>= 1
#     return res % mod

# # Example usage
# a = 2
# b = 5
# mod = 10**9 + 7
# result = power_mod(a, b, mod)
# print(result)

# # ''''''''''''''''''''''''''8. Sieve of Eratosthenes for Prime Numbers:'''''''''''''''''''''''''''''''''''
# def sieve_of_eratosthenes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False
#     p = 2
#     while p * p <= n:
#         if is_prime[p]:
#             for i in range(p * p, n + 1, p):
#                 is_prime[i] = False
#         p += 1
#     primes = [i for i in range(n + 1) if is_prime[i]]
#     return primes

# # Example usage
# n = 20
# primes = sieve_of_eratosthenes(n)
# print(primes)

# # '''''''''''''''''''''''''''9. Extended Euclidean Algorithm for Modular Inverse:''''''''''''''''''''''''
# def extended_euclidean(a, b):
#     if b == 0:
#         return a, 1, 0
#     gcd, x1, y1 = extended_euclidean(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     return gcd, x, y

# def modular_inverse(a, m):
#     gcd, x, _ = extended_euclidean(a, m)
#     if gcd == 1:
#         return (x + m) % m
#     return None

# # Example usage
# a = 7
# m = 11
# inverse = modular_inverse(a, m)
# print(inverse)

# # ''''''''''''''''''''''''''''10. Binary Search''''''''''''''''''''''''''''''''''''
# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# # Example usage
# arr = [2, 4, 6, 8, 10]
# target = 8
# index = binary_search(arr, target)
# print(index)

# # '''''''''''''''''''''''''''''''''11. Kadane's Algorithm for Maximum Subarray Sum:'''''''''''''''''''''''''
# def max_subarray_sum(arr):
#     max_sum = float('-inf')
#     curr_sum = 0
#     for num in arr:
#         curr_sum = max(curr_sum + num, num)
#         max_sum = max(max_sum, curr_sum)
#     return max_sum

# # Example usage
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum = max_subarray_sum(arr)
# print(max_sum)

# # ''''''''''''''''''''''''''''''''''12. Modular Arithmetic for large numbers using pow():''''''''''''''''''''''
# MOD = 10**9 + 7

# def fast_pow(base, exp, mod):
#     return pow(base, exp, mod)

# result = fast_pow(5, 4, MOD)
# print("Result (modulo 10^9 + 7):", result)

# result2=pow(5,2)
# print(result2)

# # ''''''''''''''''''''''''''''''''13. Bitwise Operations for setting and unsetting bits:'''''''''''''''''''''
# # Set the 2nd bit of a number to 1
# num = 5
# num |= (1 << 2)
# print(num)

# # Unset the 3rd bit of a number to 0
# num &= ~(1 << 3)
# print(num)
# # ''''''''''''''''''''''''''''''''''14. Fast Matrix Exponentiation:'''''''''''''''''''''''''''''''''''''''''
# def matrix_mult(A, B):
#     rows_A, cols_A = len(A), len(A[0])
#     cols_B = len(B[0])
#     result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

#     for i in range(rows_A):
#         for j in range(cols_B):
#             for k in range(cols_A):
#                 result[i][j] += A[i][k] * B[k][j]

#     return result

# def matrix_pow(matrix, n):
#     if n == 1:
#         return matrix

#     half_pow = matrix_pow(matrix, n // 2)
#     result = matrix_mult(half_pow, half_pow)

#     if n % 2 == 0:
#         return result
#     else:
#         return matrix_mult(result, matrix)

# matrix = [[1, 1], [1, 0]]
# n = 10
# result_matrix = matrix_pow(matrix, n)
# print("Fibonacci number at index 10:", result_matrix[0][1])

# '''''''''''''''''''''''''''''''Prefix Sum / Cumulative Sum:''''''''''''''''''''''
def calculate_prefix_sum(nums):
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum

# Example Usage:
numbers = [1, 2, 3, 4, 5]
prefix_sums = calculate_prefix_sum(numbers)
print(prefix_sums)
