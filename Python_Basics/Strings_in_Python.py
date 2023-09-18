# Data Types in Python
'''Here is a list of the built-in data types in Python:

Numeric Types:

int
float
complex
Text Type:

str
Sequence Types:

list
tuple
range
Mapping Type:
Heap
Queue
Stack

dict
Set Types:

set
frozenset
Boolean Type:

bool
Binary Types:

bytes
bytearray
None Type:

None'''

# # ''''''''''''''''''''''''''''''' Numeric Data Types:''''''''''''''''''''''''''''''''''
# # 1.int
# # Creating and initializing integer variables
# a = 5
# b = -10
# c = 0

# # Performing arithmetic operations
# sum_result = a + b  # Addition
# difference_result = a - b  # Subtraction
# product_result = a * b  # Multiplication
# quotient_result = a / b  # Division (floating-point result)
# floor_div_result = a // b  # Floor division (integer result)
# remainder_result = a % b  # Modulo (remainder)
# exponent_result = a ** 2  # Exponentiation

# # Printing the results
# print("Sum:", sum_result)
# print("Difference:", difference_result)
# print("Product:", product_result)
# print("Quotient:", quotient_result)
# print("Floor Division:", floor_div_result)
# print("Remainder:", remainder_result)
# print("Exponent:", exponent_result)

# # Converting other data types to integers
# float_num = 3.14
# converted_int = int(float_num)
# print("Converted int from float:", converted_int)

# string_num = "10"
# converted_int = int(string_num)
# print("Converted int from string:", converted_int)

# # Binary, octal, and hexadecimal representations
# binary_num = 0b101  # Binary number 101
# octal_num = 0o17  # Octal number 17
# hexadecimal_num = 0x1F  # Hexadecimal number 1F

# print("Binary number:", binary_num)
# print("Octal number:", octal_num)
# print("Hexadecimal number:", hexadecimal_num)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# a=10
# b=15
# # Conversion Functions:
# # c="123"
# # c=123.56
# c=True
# print(int(c))

# # '''''''''''''''''''''int all methods'''''''''''''''''''''''''''''''''''''''''''
# a = 5
# b = 15
# print(a.as_integer_ratio)
# print(a.as_integer_ratio())

# # ''''''''''''''''''int.bit_length()''''''''''''''''''''''''
# num = 10
# bit_length = num.bit_length()
# print(bit_length)  # Output: 4

# negative_num = -5
# bit_length_negative = negative_num.bit_length()
# print(bit_length_negative)  # Output: 3

# # '''''''''''''''''''''''''int.conjugate()'''''''''''''''''''''''''''''
# real_num = 5
# conjugate_real = real_num.conjugate()
# print(conjugate_real)  # Output: 5

# complex_num = 3 + 2j
# conjugate_complex = complex_num.conjugate()
# print(conjugate_complex)  # Output: 3 - 2j

# '''''''''''''''''''''''''int.denomminator'''''''''''''''''''''''''''
# # from fractions import Fraction
# import fractions
# num = 10
# print(num.denominator)  # Output: 1

# fraction_num = fractions.Fraction(3, 5)
# print(fraction_num.numerator)  # Output: 3
# print(fraction_num.denominator) # Output:5

# # '''''''''''''''''''
# import fractions

# # Example 1: Simplifying a fraction
# fraction = fractions.Fraction(32, 15)  # Rational number 6/15
# simplified_fraction = fraction.numerator // fraction.denominator  # Simplified value
# print("simplified_fraction: ", simplified_fraction)  # Output: 2

# # Example 2: Comparing fractions
# fraction1 = fractions.Fraction(3, 4)
# fraction2 = fractions.Fraction(5, 6)
# if fraction1 > fraction2:
#     print("fraction1 is greater")
# else:
#     print("fraction2 is greater")

# # Example 3: Calculating a sum of fractions
# fraction_list = [fractions.Fraction(
#     1, 2), fractions.Fraction(2, 3), fractions.Fraction(3, 4)]
# total_sum = sum(fraction_list)  # Sum of the fractions
# print("total_sum: ", total_sum)  # Output: 37/12

# # ''''''''''''''''''''''''''''''''''
# import fractions

# # Example: Find the denominator of the sum of two rational numbers

# def find_sum_denominator(a, b):
#     fraction_sum = fractions.Fraction(a) + fractions.Fraction(b)
#     return fraction_sum.denominator

# # Test the function
# numerator1 = 3
# denominator1 = 5
# numerator2 = 2
# denominator2 = 7

# result = find_sum_denominator(f"{numerator1}/{denominator1}", f"{numerator2}/{denominator2}")
# print(result)  # Output: 35
