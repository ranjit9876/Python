# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# a = 42

# # Built-in Methods
# print("Value:", a)
# print("Bit Length:", a.bit_length())
# print("Conjugate:", a.conjugate())
# print("Denominator:", a.denominator)
# print("From Bytes:", int.from_bytes(a.to_bytes(2, 'big')))
# print("Numerator:", a.numerator)
# print("Real:", a.real)
# print("To Bytes:", a.to_bytes(2, 'big'))

# # Mathematical Operations
# print("Add 10:", a.__add__(10))
# print("Subtract 5:", a.__sub__(5))
# print("Multiply by 2:", a.__mul__(2))
# print("True Divide by 3:", a.__truediv__(3))
# print("Floor Divide by 4:", a.__floordiv__(4))
# print("Modulo 7:", a.__mod__(7))
# print("Power of 3:", a.__pow__(3))
# print("Negative:", a.__neg__())
# print("Positive:", a.__pos__())
# print("Absolute Value:", a.__abs__())

# # Comparison Operations
# print("Equal to 42?", a.__eq__(42))
# print("Not Equal to 50?", a.__ne__(50))
# print("Less than 60?", a.__lt__(60))
# print("Less than or Equal to 30?", a.__le__(30))
# print("Greater than 20?", a.__gt__(20))
# print("Greater than or Equal to 50?", a.__ge__(50))

# # String Representations
# print("String:", a.__str__())
# print("Representation:", a.__repr__())
# print("Hash Value:", a.__hash__())
# print("Boolean Value:", a.__bool__())
 
# ***********************************************************Properties****************************************************************
# # ''''''''''''''''''''''''''''1. int.bit_length()'''''''''''''''''''''''''''
# num = 10 # 1010
# bit_length = num.bit_length()
# print(bit_length)  # Output: 4

# negative_num = -5 
# bit_length_negative = negative_num.bit_length()
# print(bit_length_negative)  # Output: 3

# # ''''''''''''''''''''''''''''''2. int.conjugate()''''''''''''''''''''''''''''''
# real_num = 5
# conjugate_real = real_num.conjugate()
# print(conjugate_real)  # Output: 5

# complex_num = 3 + 2j
# conjugate_complex = complex_num.conjugate()
# print(conjugate_complex)  # Output: 3 - 2j

# # ''''''''''''''''''''''''''''3. int.denominator '''''''''''''''''''''''''''''''''
# import fractions
# num = 10
# print(num.denominator)  # Output: 1

# fraction_num = fractions.Fraction(3, 5)
# print(fraction_num.denominator)  # Output: 5

# # ''''''''''''''''''''''''''''''4. int.real''''''''''''''''''''''''''''''''''
# num = 5
# print(num.real)  # Output: 5.0

# complex_num = 3 + 4j
# print(complex_num.real)  # Output: 3.0

# # ''''''''''''''''''''''''''''5. int.img'''''''''''''''''''''''''''''''''
# num = 10  # Integer
# print(num.imag)
# complex_num = complex(num)  # Convert to complex number


# print(complex_num.imag)  # Output: 0

# complex_num = complex(3, 4)  # Complex number with real and imaginary parts
# print(complex_num.imag)  # Output: 4

# # ''''''''''''''''''''''int.bit_count()'''''''''''''''''''''''''
# num=10
# bit_count_1=num.bit_count()
# print(bit_count_1)
# bit_count_2=num.bit_count
# print(bit_count_2())
# # '''''''''''''''''''''''''''int.from_bytes()'''''''''''''''''''''
# # Example 1: Converting bytes to an integer
# bytes_seq = b'\x00\x00\x00\x0A'
# integer = int.from_bytes(bytes_seq, byteorder='big')
# print(integer)  # Output: 10

# # Example 2: Converting bytes to a signed integer
# bytes_seq = b'\xFF\xFF\xFF\xFF'
# integer = int.from_bytes(bytes_seq, byteorder='big', signed=True)
# print(integer)  # Output: -1

# bytes_array = b'\xFF\x00\x00\x0F'  # 4 bytes representing the value -16776982
# integer = int.from_bytes(bytes_array, byteorder='little', signed=True)
# print(integer)  # Output: -16776982

# # '''''''''''''''''''''''int.to_bytes()''''''''''''''''''''''''''''''''''
# integer = 15
# bytes_array = integer.to_bytes(length=4, byteorder='big')
# print(bytes_array)  # Output: b'\x00\x00\x00\x0f
# bytes_array2 = integer.to_bytes(length=4, byteorder='little')
# print(bytes_array2) # Output: b'\x0f\x00\x00\x00'


# integer = -16776982
# bytes_array = integer.to_bytes(length=4, byteorder='big', signed=True)
# print(bytes_array)  # Output: b'\xff\x00\x00\xea'

# ''''''''''''''''''''''''''''''int.__abs()__
# num = -10
# # abs_value = num.__abs__ # return object refrence
# abs_value = num.__abs__()
# print(abs_value)  # Output: 10

# # Alternatively, you can use the abs() function directly:
# abs_value = abs(num)
# print(abs_value)  # Output: 10

# # ''''''''''''''''''''''''''''''
# from functools import total_ordering

# @total_ordering
# class MyInt(int):
#     def __new__(cls, value):
#         return super().__new__(cls, value)

#     def __abs__(self):
#         if self < 0:
#             return -self
#         return self

# # Example usage:
# num1 = MyInt(-10)
# num2 = MyInt(20)

# abs_num1 = abs(num1)
# print(abs_num1)  # Output: 10

# abs_num2 = abs(num2)
# print(abs_num2)  # Output: 20

# print(abs_num1 < abs_num2)  # Output: True

# # ''''''''''''''''''''''''''''''''''''''
# # Example 1: Compute the absolute difference between two integers
# a = 5
# b = -8

# abs_diff = abs(a - b)
# print(abs_diff)  # Output: 13

# # Example 2: Find the maximum absolute difference in a list of integers
# nums = [1, -3, 6, -9, 4, -2]

# max_abs_diff = max(abs(num1 - num2) for num1 in nums for num2 in nums)
# print(max_abs_diff)  # Output: 15
# # '''''''''''''''''''''''''''''''''''''''''''''''
# def absolute_value(num):
#     mask = num >> (num.bit_length() - 1)  # Create a mask to get the sign bit (0 for positive, -1 for negative)
#     return (num + mask) ^ mask  # XOR the number with the mask to flip the sign bit for negative numbers

# # Example usage:
# num = -110
# abs_value = absolute_value(num)
# print(abs_value)  # Output: 10

# # ''''''''''''''''''''''''''''''''''''''''''''''
# # Given an array of integers, find the sum of absolute differences between adjacent elements.
# # For example, for the array [2, -5, 8, 0], the result would be |2-(-5)| + |(-5)-8| + |8-0| = 17.

# def sum_of_absolute_differences(arr):
#     total_sum = 0
#     for i in range(1, len(arr)):
#         difference = abs(arr[i] - arr[i-1])  # Use abs() to get the absolute difference
#         total_sum += difference
#     return total_sum

# # Example usage:
# array = [2, -5, 8, 0]
# result = sum_of_absolute_differences(array)
# print(result)  # Output: 17

# # '''''''''''''''''''''''''''''''''''''''''''''''custom abs'''''''''''''''''''
# # Custom implementation of int.__abs__() method
# def custom_abs(num):
#     return num if num >= 0 else num.__neg__()

# # Example usage in competitive programming
# num1 = -10
# num2 = 15

# # Using built-in abs() function
# abs_value_1 = abs(num1)
# abs_value_2 = abs(num2)

# # Using custom_abs() method
# abs_value_1_custom = custom_abs(num1)
# abs_value_2_custom = custom_abs(num2)

# print(abs_value_1)  # Output: 10
# print(abs_value_2)  # Output: 15
# print(abs_value_1_custom)  # Output: 10
# print(abs_value_2_custom)  # Output: 15
# # ''''''''''''''''''''''''''''''''2.int.__add__(other)''''''''''''''''''''''''''
# num1 = 10
# num2 = 20

# # Using the '+' operator to add two integers
# result = num1 + num2
# print(result)  # Output: 30

# # Equivalent to the above code using the __add__() method directly
# result_method = num1.__add__(num2)
# print(result_method)  # Output: 30
# # ''''''''''''''''''''''''''''''''''''''
# class MyInt:
#     def __init__(self, value):
#         self.value = value
    
#     def __add__(self, other):
#         if isinstance(other, MyInt):
#             return MyInt(self.value + other.value)
#         elif isinstance(other, int):
#             return MyInt(self.value + other)
#         else:
#             raise TypeError("Unsupported operand type: {}".format(type(other)))

# # Example usage:
# a = MyInt(5)
# b = MyInt(10)
# c = a + b
# print(c.value)  # Output: 15

# d = a + 7
# print(d.value)  # Output: 12
# # '''''''''''''''''''''''''''''''''''''''''''''
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Point):
#             return Point(self.x + other.x, self.y + other.y)
#         else:
#             raise ValueError("Unsupported operand type for +")

# # Example usage:
# point1 = Point(1, 2)
# point2 = Point(3, 4)

# # Adding two Point objects using the '+' operator
# result = point1 + point2
# print(result.x, result.y)  # Output: 4 6

# # '''''''''''''''''''''''''''''''''''''''''''''''Integer Built-in-Function''''''''''''''''''''''''
# '''abs(x): Returns the absolute value of x.
# divmod(a, b): Returns a tuple containing the quotient and remainder of the division of a by b.
# pow(x, y, z=None): Returns x to the power of y, modulo z (if provided).
# round(number[, ndigits]): Rounds a number to the nearest integer or to the specified number of decimal places (ndigits).
# bin(x): Converts an integer x to a binary string prefixed with '0b'.
# hex(x): Converts an integer x to a lowercase hexadecimal string prefixed with '0x'.
# oct(x): Converts an integer x to an octal string prefixed with '0o'.
# int(x): Converts x to an integer. If x is not specified, it returns 0.'''

# num = -10

# # Absolute value
# abs_value = abs(num)
# print(abs_value)  # Output: 10

# # Divmod
# quotient, remainder = divmod(num, 3)
# print(quotient, remainder)  # Output: (-4, 2)

# # Power
# result = pow(2, 3)
# print(result)  # Output: 8

# # Rounding
# rounded = round(3.14159, 2)
# print(rounded)  # Output: 3.14

# # Conversion to binary, hexadecimal, and octal strings
# binary_str = bin(num)
# hex_str = hex(num)
# octal_str = oct(num)
# print(binary_str, hex_str, octal_str)  # Output: '-0b1010' '-0xa' '-0o12'

# # Integer conversion
# # int_num = int('1010',2)
# int_num = int('14563',8)
# print(int_num)  # Output: 3

# # ''''''''''''''''''''''''''''''''''int.__and__(other)'''''''''''''''''
# num=9
# bitwise_and=num.__and__(6)
# bitwise_and_2=num & 6
# print(bitwise_and," ",bitwise_and_2)

# num=1
# # print(num.__bool__(True))
# print(num.__sub__(8))

# # ''''''''''''''''''''''''''''''''''''''''''''
# num=10
# print(num.__getstate__())
# print(num.__float__())

# l1=[1,2,3,4]
