"""
''''''''''''''''''''''1. Numeric Types:'''''''''''''''''''''''''''''''

int: Integer values (e.g., 1, -20, 1000).
float: Floating-point values (e.g., 3.14, -2.5, 0.1).
complex: Complex number data type, e.g., 1 + 2j, 3 - 4j.

''''''''''''''''''''''''2. Sequence Types:''''''''''''''''''''''''''

 str: Strings of characters (e.g., "hello", 'Python', "123").'''''''''''''''''''''''
list: Ordered, mutable sequences (e.g., [1, 2, 3], ['apple', 'banana']).
tuple: Ordered, immutable sequences (e.g., (1, 2, 3), ('a', 'b')).

''''''''''''''''''''''''''3. Mapping Type:''''''''''''''''''''''''''''''''''
dict: Dictionaries, unordered key-value pairs (e.g., {'name': 'John', 'age': 30}).
''''''''''''''''''''''''''4. Set Types:''''''''''''''''''''''''''''''

set: Unordered, mutable collection of unique elements (e.g., {1, 2, 3}).
frozenset: Unordered, immutable collection of unique elements (e.g., frozenset({1, 2})).
''''''''''''''''''''''''''5.  Boolean Type:'''''''''''''''''''''''''''''''''''

bool: Represents either True or False.
'''''''''''''''''''''''''6. Binary Types:''''''''''''''''''''''''''''

bytes: Immutable sequence of bytes (e.g., b'hello').
bytearray: Mutable sequence of bytes (e.g., bytearray([65, 66, 67])).
memoryview: Represents a memory view of objects supporting the buffer protocol.
'''''''''''''''''''''''''''7. NoneType:''''''''''''''''''''''''''''''''''''''

None: Represents the absence of a value or a null value.
'''''''''''''''''''''''''''8.Other Types:''''''''''''''''''''''''

range: Represents an immutable sequence of numbers, e.g., range(0, 5).
complex: Represents complex numbers, e.g., 2 + 3j.
ellipsis: Represents an ellipsis object used in slicing.
NotImplemented: Represents a special value returned by some binary operators when the operation is not implemented.
    """
# # *********************************************Python Data Type''''''''''''''''''''''''''''''''''''''''
# # Numeric Types
# num_integer = 42
# num_float = 3.14
# num_complex = 1 + 2j

# # Sequence Types
# str_text = "Hello, World!"
# list_numbers = [1, 2, 3]
# tuple_coordinates = (10, 20)

# # Mapping Type
# dict_person = {'name': 'John', 'age': 30}

# # Set Types
# set_numbers = {1, 2, 3}
# frozenset_numbers = frozenset({1, 2, 3})

# # Boolean Type
# is_active = True
# is_disabled = False

# # None Type
# nothing = None

# # Binary Types
# bytes_data = b'hello'
# bytearray_data = bytearray(b'hello')

# # Range Type
# range_data = range(0, 5)

# # Ellipsis Type
# ellipsis_data = ...

# # Complex Type
# complex_number = complex(2, 3)

# # Memory View Type
# memory_view_data = memoryview(b'hello')

# # Print all the data types
# print("Numeric Types:")
# print(num_integer, type(num_integer))
# print(num_float, type(num_float))
# print(num_complex, type(num_complex))

# print("\nSequence Types:")
# print(str_text, type(str_text))
# print(list_numbers, type(list_numbers))
# print(tuple_coordinates, type(tuple_coordinates))

# print("\nMapping Type:")
# print(dict_person, type(dict_person))

# print("\nSet Types:")
# print(set_numbers, type(set_numbers))
# print(frozenset_numbers, type(frozenset_numbers))

# print("\nBoolean Type:")
# print(is_active, type(is_active))
# print(is_disabled, type(is_disabled))

# print("\nNone Type:")
# print(nothing, type(nothing))

# print("\nBinary Types:")
# print(bytes_data, type(bytes_data))
# print(bytearray_data, type(bytearray_data))

# print("\nRange Type:")
# print(range_data, type(range_data))

# print("\nEllipsis Type:")
# print(ellipsis_data, type(ellipsis_data))

# print("\nComplex Type:")
# print(complex_number, type(complex_number))

# print("\nMemory View Type:")
# print(memory_view_data, type(memory_view_data))

# # Advanced Concepts
# # List comprehension
# squared_numbers = [num ** 2 for num in list_numbers]

# # List comprehensions, a compact way to create lists
# numbers = [i for i in range(1, 11)]
# squares = [x**2 for x in numbers]
# even_numbers = [x for x in numbers if x % 2 == 0]

# # Lambda function
# multiply_by_2 = lambda x: x * 2

# # Map function
# list_numbers = [1, 2, 3]
# mapped_numbers = list(map(multiply_by_2, list_numbers))

# # Filter function
# even_numbers = list(filter(lambda x: x % 2 == 0, list_numbers))

# # Sorting a list using 'sorted' function
# sorted_numbers = sorted(numbers)
  
# # Tuples for storing immutable data
# point = (5, 10)

# # Sets for efficient membership checking and removing duplicates
# unique_numbers = set(numbers)
# primes = {2, 3, 5, 7, 11, 13}

# # Set: Find common elements in two lists using sets
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = set(list1) & set(list2)

# # Set intersection to find common elements between two sets
# common_elements = set_numbers.intersection(frozenset_numbers)

# # Set Operations
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# union_set = set_a | set_b  # {1, 2, 3, 4, 5}
# intersection_set = set_a & set_b  # {3}
# difference_set = set_a - set_b  # {1, 2}

# # Boolean operations
# logical_and = is_active and (2 in set_numbers)
# logical_or = is_disabled or (3 in set_numbers)


# # Dictionary comprehensions: Create a dictionary with numbers as keys and their squares as values
# n = 5
# squares_dict = {x: x**2 for x in range(1, n+1)}

# # Boolean Type and "any" function: Check if any element in a list is divisible by 5
# numbers = [10, 21, 36, 45, 59]
# is_divisible_by_5 = any(num % 5 == 0 for num in numbers)

# # None Type and ternary operator: Determine if a number is even or odd using a ternary operator
# number = 17
# parity = "even" if number % 2 == 0 else "odd"

# # Complex numbers and arithmetic operations
# complex_num1 = 2 + 3j
# complex_num2 = 1 - 2j
# addition_result = complex_num1 + complex_num2
# multiplication_result = complex_num1 * complex_num2

# # Using lambda function for sorting a list of tuples based on the second element
# list_tuples = [(1, 5), (3, 1), (2, 3)]
# list_tuples_sorted = sorted(list_tuples, key=lambda x: x) 
# list_tuples_sorted = sorted(list_tuples, key=lambda x: x[0])
# list_tuples_sorted = sorted(list_tuples, key=lambda x: x[1])

# # Using zip to merge two lists into a list of tuples
# list_a = [1, 2, 3]
# list_b = ['a', 'b', 'c']
# merged_list = list(zip(list_a, list_b))

# # Set intersection to find common elements
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# common_elements = set_a & set_b

# # Mapping Type & Dictionary Comprehension
# dict_person = {'name': 'John', 'age': 30, 'occupation': 'Engineer'}
# dict_ages = {name: age for name, age in {'Alice': 25, 'Bob': 32, 'Eve': 27}.items() if age > 30}

# # Set Types & Lambda Functions
# set_numbers = {1, 2, 3, 4, 5}
# doubled_numbers = set(map(lambda x: x * 2, set_numbers))
# even_set_numbers = set(filter(lambda x: x % 2 == 0, set_numbers))

# print("\nAdvanced Concepts:")
# print("Squared Numbers:", squared_numbers, "type of square_number: ", type(squared_numbers))
# print("multiply_by_2:", multiply_by_2(4), "type of multiplay_by_2: ", type(multiply_by_2))
# print("Mapped Numbers:", mapped_numbers, "type of mapped_numbers: ", type(mapped_numbers))
# print("Even Numbers:", even_numbers, "type of even_numbers: ", type(even_numbers))
# print("Set (Common Elements):", common_elements)
# print("Dictionary Comprehension (Squares):", squares_dict)
# print("Boolean Type and 'any':", is_divisible_by_5)
# print("None Type and Ternary Operator (Parity):", parity)
# print("Complex Numbers (Addition):", addition_result)
# print("Complex Numbers (Multiplication):", multiplication_result)
# print("Sorted Tuples:", list_tuples_sorted)
# print("Merged List:", merged_list)


# # ''''''''''''''''''''''''''''''''# Generate prime numbers using Sieve of Eratosthenes''''''''''''''''''''''''''''''''''''
# import math

# # Generate prime numbers using Sieve of Eratosthenes
# def generate_primes(n):
#     primes = [True] * (n + 1)
#     primes[0] = primes[1] = False
#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1
#     return [i for i in range(n + 1) if primes[i]]

# prime_numbers = generate_primes(50)
# print("Prime numbers up to 50:", prime_numbers)

# # '''''''''Problem: Given a list of integers, find all distinct pairs of elements whose sum is a specific target value.'''''''''''
# def find_pairs_with_sum(nums, target):
#     seen = set()
#     pairs = set()
    
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             pairs.add((min(num, complement), max(num, complement)))
#         seen.add(num)
    
#     return pairs

# # Test the function
# nums = [2, 4, 3, 7, 1, 5, 9, 6]
# target_sum = 10
# result = find_pairs_with_sum(nums, target_sum)

# print("Pairs with sum 10:")
# for pair in result:
#     print(pair)
    
# # ''''''''''''''''''''''''''''''''' Kadane's algorithm to find the maximum sum subarray''''''''''''''''''''
# def kadane_algorithm(arr):
#     # Kadane's algorithm to find the maximum sum subarray
#     max_ending_here = max_so_far = arr[0]
#     for num in arr[1:]:
#         max_ending_here = max(num, max_ending_here + num)
#         max_so_far = max(max_so_far, max_ending_here)
#     return max_so_far

# # Advanced concept using Kadane's algorithm
# print("\nKadane's Algorithm:")
# arr = [1, 2, -3, 4, -1, 5, -2]
# max_sum_subarray = kadane_algorithm(arr)
# print("Maximum Sum Subarray:", max_sum_subarray)

# # ''''''''''''''''''''''''''''''''''''' Using a dictionary to count occurrences of elements in a list''''''''''''''''''''''''''
# # Using a dictionary to count occurrences of elements in a list
# list_numbers = [1, 2, 3]
# count_dict = {}
# for num in list_numbers:
#     count_dict[num] = count_dict.get(num, 0) + 1
    
# print("\nCount of Elements using Dictionary:")
# print(count_dict)

# # Using the "in" operator to check if an element exists in a list
# element_exists = 2 in list_numbers

# print("\nCheck if Element Exists in List:")
# print(element_exists)

# # Example of a custom class to represent a Point in 2D space
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # List comprehensions, a compact way to create lists
# numbers = [i for i in range(1, 11)]
# squares = [x**2 for x in numbers]
# even_numbers = [x for x in numbers if x % 2 == 0]

# # Dictionaries to store data with key-value pairs
# student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# # Sets for efficient membership checking and removing duplicates
# unique_numbers = set(numbers)
# primes = {2, 3, 5, 7, 11, 13}

# # Using 'zip' to combine two lists into tuples
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 22]
# people = list(zip(names, ages))

# # Tuples for storing immutable data
# point = (5, 10)

# # Using 'enumerate' to get index and value while iterating
# for index, value in enumerate(numbers):
#     print(f"Index: {index}, Value: {value}")

# # Slicing to get sub-lists or substrings
# str_text="Hello, world!"
# some_numbers = numbers[2:7]
# first_three_chars = str_text[:3]

# # The 'any' and 'all' functions for quick checks
# has_negative = any(num < 0 for num in numbers)
# all_positive = all(num > 0 for num in numbers)

# # Sorting a list using 'sorted' function
# sorted_numbers = sorted(numbers)

# # Using 'min' and 'max' to find the smallest and largest elements
# min_value = min(numbers)
# max_value = max(numbers)

# # Counting occurrences using 'collections.Counter'
# from collections import Counter
# word_count = Counter(str_text.split())

# # Default dictionaries to handle missing keys more conveniently
# from collections import defaultdict
# fruit_count = defaultdict(int)
# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# for fruit in fruits:
#     fruit_count[fruit] += 1

# # Binary search using 'bisect' module
# from bisect import bisect_left
# sorted_list = [2, 4, 7, 10, 15, 20, 25]
# index = bisect_left(sorted_list, 10)

# # Deque for efficient pop and append operations from both ends
# from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# d.pop()
# d.popleft()

# # Heap queue using 'heapq' for priority queue operations
# import heapq
# heap = [2, 4, 6, 8, 10]
# heapq.heapify(heap)
# smallest = heapq.heappop(heap)

# # Applying functions to a list using 'map'
# def square(x):
#     return x**2
# numbers_squared = list(map(square, numbers))

# # Lambda functions for quick one-liner functions
# double = lambda x: x * 2
# numbers_doubled = list(map(lambda x: x * 2, numbers))

# # Sorting custom objects using 'key' parameter in 'sorted'
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# students = [Student('Alice', 85), Student('Bob', 92), Student('Charlie', 78)]
# sorted_students = sorted(students, key=lambda s: s.score)

# # # Generating all subsets using bit manipulation
# # n = len(numbers)
# # all_subsets = [numbers[i] for i in range(2**n)]

# # Binary exponentiation for efficient power calculation
# def power(base, exp):
#     result = 1
#     while exp > 0:
#         if exp & 1:  # If the least significant bit is set
#             result *= base
#         base *= base
#         exp >>= 1  # Right shift the exponent
#     return result

# # Usage of advanced concepts for competitive programming
# print("Numbers:", numbers)
# print("Squares:", squares)
# print("Even Numbers:", even_numbers)
# print("Student Scores:", student_scores)
# print("Unique Numbers:", unique_numbers)
# print("Primes:", primes)
# print("People:", people)
# print("Point:", point)
# print("Some Numbers:", some_numbers)
# print("First Three Chars:", first_three_chars)
# print("Has Negative Number:", has_negative)
# print("All Positive Numbers:", all_positive)
# print("Sorted Numbers:", sorted_numbers)
# print("Min Value:", min_value)
# print("Max Value:", max_value)
# print("Word Count:", word_count)
# print("Fruit Count:", dict(fruit_count))
# print("Index of 10 in sorted list:", index)
# print("Numbers Squared:", numbers_squared)
# print("Numbers Doubled:", numbers_doubled)
# print("Sorted Students:", [(s.name, s.score) for s in sorted_students])
# # print("All Subsets:", all_subsets)
# print("2^3:", power(2, 3))


# # Using a decorator function to double the result of a function
# def double_result(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper

# # Applying the decorator to a function
# @double_result
# def add(a, b):
#     return a + b

# print("Using decorator to double the result of the add function:", add(3, 5))

# # Using a deque to efficiently implement a queue
# from collections import deque
# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()

# print("\nDeque (Queue):")
# print(queue)

# *******************************************************List Operations ***************************************
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# List comprehension to create a list of squares of numbers from 1 to 10
squares = [x**2 for x in numbers]

# Lambda function to filter even numbers from the list
is_even = lambda x: x % 2 == 0

# Use lambda function with filter to get a list of even numbers
even_numbers = list(filter(is_even, numbers))

# Lambda function to check if a number is prime
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

# Use lambda function with filter to get a list of prime numbers
prime_numbers = list(filter(is_prime, numbers))

# List comprehension to create a list of pairs from numbers and their squares
number_square_pairs = [(x, x**2) for x in numbers]

# List comprehension to create a list of cumulative sums
cumulative_sums = [sum(numbers[:i + 1]) for i in range(len(numbers))]

# List comprehension to create a list of prefix maximums
prefix_maximums = [max(numbers[:i + 1]) for i in range(len(numbers))]

# List comprehension to create a list of differences between adjacent elements
differences = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]

# Output all the lists
print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Prime Numbers:", prime_numbers)
print("Number-Square Pairs:", number_square_pairs)
print("Cumulative Sums:", cumulative_sums)
print("Prefix Maximums:", prefix_maximums)
print("Differences:", differences)

# '''''''''''''''''''''''''''''''''''''''''''''''''''''
# Creating a list
numbers = [1, 2, 3, 4, 5]

# Accessing list elements
print("Accessing List Elements:")
print(numbers[0])  # Output: 1
print(numbers[-1])  # Output: last element
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1] reverse element
print()

# Extend the list with another list
numbers.extend([7, 8, 9])
print("extended numbers list: ", numbers)

# Index of the first occurrence of a value
index_of_4 = numbers.index(4)

# Insert an element at a specific index
numbers.insert(2, 10)

# Count occurrences of a value in the list
count_of_5 = numbers.count(5)

l1=[11,10,5,2,67,9,10]
# Sort the list in ascending order
l1.sort()

# Sort the list in descending order
l1.sort(reverse=True)

# Reverse the list
l1.reverse()

# Calculate the sum of all elements in the list
sum_of_elements = sum(numbers)

# Check if a value is present in the list
is_present = 7 in numbers

# Clear the list
l1.clear()

numbers = [1, 2, 3, 4, 5]
# Reduce using lambda function to get the sum of numbers(elements)
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("sum_of_numbers: ",sum_of_numbers)

# # List concatenation
list1=[1,2,3,4,5,6]
list2=[4,3,7,10,5,11]
merged_list = list1+list2
print("merged_list: ",merged_list)

# List membership test
is_present = 3 in list1
is_absent = 6 not in list2

# List length
list_length = len(list1)

# List repetition
list3=[11,12,13,15]
repeated_list = list3 * 2

print("repeated_list: ",repeated_list)

# Modifying list elements
print("Modifying List Elements:")
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]
print()

# Appending elements to the list
print("Appending Elements to the List:")
numbers.append(6) # Appending an element to the end of the list
print(numbers)  # Output: [1, 2, 10, 4, 5, 6]
print()

# Removing elements from the list
print("Removing Elements from the List:")
numbers.remove(4)
print(numbers)  # Output: [1, 2, 10, 5, 6]
# Pop an element from the list at a specific index
numbers.pop(1) 
print(numbers)  # Output: [1, 10, 5, 6]
del numbers[0]
print(numbers)  # Output: [10, 5, 6]
print()

# List slicing and copying
print("List Slicing and Copying:")
sliced_list = numbers[1:3]
print(sliced_list)  # Output: [5, 6]
copied_list = numbers.copy()
print(copied_list)  # Output: [10, 5, 6]
print()

# List concatenation
print("List Concatenation:")
new_list = numbers + [7, 8, 9]
print(new_list)  # Output: [10, 5, 6, 7, 8, 9]
print()

# List sorting and reversing
print("List Sorting and Reversing:")
numbers.sort()
print(numbers)  # Output: [5, 6, 10]
numbers.reverse()
print(numbers)  # Output: [10, 6, 5]
print()

# List comprehension
print("List Comprehension:")
squared_list = [x**2 for x in numbers]
print(squared_list)  # Output: [100, 36, 25]
filtered_list = [x for x in numbers if x % 2 == 0]
print(filtered_list)  # Output: [10, 6]
print()

# Advanced Concepts
# Using lambda function with map to get cubes of numbers in the list
numbers=[1,2,3,4,5]
cube_func = lambda x: x**3
cubes = list(map(cube_func, numbers))
print("Cubes:", cubes)

# Lambda function to add two numbers
add_func = lambda x, y: x + y

# List comprehension to get the cumulative sum of numbers
cumulative_sum = [numbers[0]] + [add_func(numbers[i], cumulative_sum[i-1]) for i in range(1, len(numbers))]

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Basic list operations
list_length = len(numbers)
list_sum = sum(numbers)
list_min = min(numbers)
list_max = max(numbers)
list_sorted = sorted(numbers)
list_reversed = list(reversed(numbers))
