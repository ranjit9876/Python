# # '''''''''''''''''''''1.To Find the Memory Address of Integer Data Types by id()''''''''''''''''''''''''''''
# '''(function) def id(__obj: object,/) -> int'''
# # id(__obj: object) -> int; Return the identity of an object

# num1 = 3
# # Return the identity of an int data type.
# print(f"Memory Address of Integer Data Type {num1}: {id(num1)}")

# str1 = 'Ranjit Kumar Gupta'
# # Return the identity of an str data type
# print(f"Memory Address of String Data Type, {str}: {id(num1)}")

# x = 5
# y = 5
# z = [1, 2, 3]

# print(id(x))  # Print the id of variable x
# print(id(y))  # Print the id of variable y (which will be the same as x)
# print(id(z))  # Print the id of list z
# # '''''''''''''''
# # Define a function that takes an object and returns its id


# def get_object_id(__obj: object):
#     return id(__obj)


# # Creates some objects
# x = 10
# y = 20
# z = [10, 20]
# str1 = "Hello, world!"

# # Get and print the id of these objects
# x_id = get_object_id(x)
# y_id = get_object_id(y)
# z_id = get_object_id(z)
# str1_id = get_object_id(str1)

# print(f'id of x: {x_id}')
# print(f'id of y: {y_id}')
# print(f'id of z: {z_id}')
# print(f'id of str1: {str1_id}')

# # Check if tho objects have the same identifier
# if (x_id == y_id):
#     print(f"{x} and {y} have the same identifier")
# else:
#     print(f"{x} and {y} have the different identifier")

# if (x_id == z_id):
#     print(f"{x} and {z} have the same identifier")
# else:
#     print(f"{x} and {z} have the different identifier")

# # ''''''''''''''''id() for competitive programming''''''''''''''
# # Import defaultdict from collections module
# # Function to find the number of unique objets in a list

# from collections import defaultdict
# def count_unique_objects(arr):
#     unique_ids = set()

#     count_dict = defaultdict(int)
#     print(count_dict)

#     for obj in arr:
#         obj_id = id(obj)
#         if obj_id not in unique_ids:
#             unique_counts.add(obj_id)
#             count_dict[obj_id] += 1
#     return count_dict


# if __name__ == '__main__':
#     # Sample list of objects
#     objects = [1, 2, 3, 2, 4, 5, 3, 'apple', 'bannana', 'apple']

#     # Count the number of unique objects and their occurrences
#     unique_counts = count_unique_objects(objects)
#     for obj_id, count in unique_counts.items():
#         obj = [item for item in objects ]

# # ''''''''''''''''''''
# class ObjectManager:
#     def __init__(self):
#         self.objects = {}
#         self.counter = 0

#     def create_object(self, data):
#         # Generate a unique ID for the object
#         unique_id = self.counter
#         self.counter += 1

#         # Store the object with its unique ID
#         self.objects[unique_id] = data

#         return unique_id

#     def get_object(self, unique_id):
#         # Retrieve an object by its unique ID
#         return self.objects.get(unique_id, None)

# # Create an instance of ObjectManager
# object_manager = ObjectManager()

# # Create some objects and get their unique IDs
# id1 = object_manager.create_object([1, 2, 3])
# id2 = object_manager.create_object("Hello, World!")
# id3 = object_manager.create_object(42)
# id4 = object_manager.create_object(42)
# # Get objects by their unique IDs
# object1 = object_manager.get_object(id1)
# object2 = object_manager.get_object(id2)
# object3 = object_manager.get_object(id3)
# object4 = object_manager.get_object(id4)

# # Print the unique IDs and objects
# print(f"Unique ID 1: {id1}, Object 1: {object1}")
# print(f"Unique ID 2: {id2}, Object 2: {object2}")
# print(f"Unique ID 3: {id3}, Object 3: {object3}")
# print(f"Unique ID 4: {id4}, Object 4: {object4}")


# # # ''''''''''''''''''''''''2.Assingning The Singal and  Multiple Values at the same time''''''''''''''''''''''''''
# # num1  = 10 # Assigning the integer value to num variable
# # print(type(num1)) # <class 'int'>

# # num2: str = 10
# # print(type(num2)) # <class 'int'>
# # print(num2)

# # a, b, c = 10, 20, 30
# # print(f'a= {a}, b= {b}, c= {c}')

# # a, b, c = 10, 'ChatGPT', 3.0
# # print(f'a= {a}, b= {b}, c={c}')

# # Unpacking Sequence: unpack values from sequences like lists or tuples into multiple variables.
# l1 = [1,2,3]
# x,y,z = l1
# print(f'x= {x}, y= {y}, z= {z}')

# # Swaping variables:
# x, y = 10, 20
# x, y = y, x
# print(f'x= {x}, y= {y}')

# # Extended Unpacking: extended unpacking using the * operator to capture multiple values into a single variable.
# l1 = [1,2,3,4,5,6,7,8,9,10,"Hello world!"]
# first, *rest = l1
# print(f'first: {first}, rest: {rest}')
# print(f'l1: {l1}')
# first, second, *rest = l1
# print(f'first: {first}, second: {second}, rest: {rest}')

# first, *middle, last = l1
# print(f'first: {first}, middle: {middle}, last: {last}')

# # Using extended unpacking for function return values.
# def get_numbers():
#     return 1,2,3,4,5,6,7,8,9,10,11,"hello world"

# first, second, *rest = get_numbers()
# print(f'first: {first}, second: {second}, rest: {rest}')

# # Unpacking in the functional argument
# def add(a,b):
#     return a + b

# values = (1,2)
# sum = add(*values) # unpack the tuple
# print(f'sum: {sum}')

# # '''''''''''''''''''''''''''''''''''''''Unlimited Size of int''''''''''''''''''''''''''''''''''''''''''
# # 1.Performing Operations with Large Integer'''''''''''''''''
# import math
# a = 10 ** 20  # very large integer
# b = 20 ** 100  # another big integer
# # print(a + b)

# # 2. Exponentiation with large Integer
# num = 2 ** 1000
# print(num)

# # 3.Factorial Calculations
# num = 1000  # Calculate 1000!
# result = math.factorial(num)
# print(result)

# # 4.Modular Arithmetics
# a = 10**50
# b = 7
# mod = 1000000007 # A Common Modulo value
# # Calculate (a ^ b) % mod
# result = pow(a,b,mod)
# print(result)

# # 5.Factorization with Large Primes:
# import sympy

# large_prime = sympy.nextprime(10 ** 100)  # Find the next prime larger than 10^100
# print(f'large_prime: {large_prime}')

# 6.Large Summation
large_list = [10 ** 18] * 10**6
total_sum = sum(large_list)  # Efficiently sum a large list of integers
print(total_sum)

# 7.Prime Number Generation
import sympy

n = 10**100
primes = list(sympy.primerange(n, n + 100))
print(primes)