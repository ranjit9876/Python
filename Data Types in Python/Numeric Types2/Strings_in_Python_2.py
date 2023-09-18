# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''1.String Creation:'''''''''''''''''''''''''''''''''''''''''''''''''''
# Single quotes
single_quoted_str = 'Hello, I am a single-quoted string.'

# Double quotes
double_quoted_str = "Hello, I am a double-quoted string."

# Triple quotes (useful for multi-line strings)
multiline_str = """This is a
multi-line string."""

print(single_quoted_str)
print(double_quoted_str)
print(multiline_str)

# '''''''''''''''''''''''''''''''''''''''2.String Access:'''''''''''''''''''
text = "Python"
first_char = text[0]  # 'P'
last_char = text[-1]  # 'n' (negative indexing starts from the end)
# ''''''''''''''''''''''''''''''''''3.String Slicing:'''''''''''''''''''''''''''''''
text = "Hello, World!"
substring = text[0:5]  # 'Hello'
substring_with_step = text[::2]  # 'Hlo ol!'
# '''''''''''''''''''''''''''''''''''4.String Concatenation:''''''''''''''''''''''''''''
str1 = "Hello, "
str2 = "World!"
result = str1 + str2  # 'Hello, World!'

# Using '+=' operator
str1 += str2  # str1 now becomes 'Hello, World!'
# ''''''''''''''''''''''''''''''''''''5.String Length:'''''''''''''''''''''''''''''''''''
text = "Hello, World!"
length = len(text)  # 13
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""String Methods:
Python provides numerous built-in methods to manipulate strings, such as:
upper(): Converts the string to uppercase.
lower(): Converts the string to lowercase.
strip(): Removes leading and trailing whitespace.
split(): Splits the string into a list based on a delimiter.
join(): Joins elements of an iterable with the string as a separator.
replace(): Replaces occurrences of a substring with another substring.
find(): Returns the index of the first occurrence of a substring.
count(): Returns the number of occurrences of a substring."""
print("\n\n")
text = "   Hello, World!   "
uppercase_text = text.upper()  # '   HELLO, WORLD!   '
lowercase_text = text.lower()  # '   HELLO, WORLD!   '
print(lowercase_text)          # '   hello, world!   '
stripped_text = text.strip()  # 'Hello, World!'
words = text.split(',')  # ['   Hello', ' World!   ']
joined_text = '-'.join(words)  # '   Hello- World!   '
replaced_text = text.replace('World', 'Python')  # '   Hello, Python!   '
occurrences = text.count('l')  # 3

# '''''''''''''''''''''''''''''String Formatting:''''''''''''''''''''''''''''''''''
# ''''''''''''Using format()''''''''''''
name = "John"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
# 'My name is John and I am 30 years old.'

# Using f-strings (available in Python 3.6 and later):
name = "John"
age = 30
message = f"My name is {name} and I am {age} years old."
# 'My name is John and I am 30 years old.'

# Using % operator:
message="My name is %s and I am %d years old." % (name, age)
# 'My name is Alice and I am 25 years old.'

# '''''''''''''''''''''''''''''''''String Escape Sequences:'''''''''''''''''''''''''''''''''''''''''''''''
escaped_str = "This string has a new line.\nAnd a tab:\tHello!"
print(escaped_str)
# Output:
# This string has a new line.
# And a tab:    Hello!

# # ''''''''''''''''''''''''''''''''''''''''immutability'''''''''''''''''''''''''''
# my_string = "Hello"
# # This will raise an error: 'str' object does not support item assignment
# my_string[0] = 'M'

# ''''''''''''''''''String Operations''''''''''''''''''''
my_str = "Hello, world!"
print("world" in my_str)       # Output: True
print("python" not in my_str)  # Output: True

# ''''''''''''''''''''''''''''''Raw String''''''''''''''''''''''''''''
# raw_str = r"This is a raw \n string."
raw_str = R"This is a raw \n string."
print(raw_str)  # 'This is a raw \n string.'

# '''''''''''''''''''''''''''''String Searching'''''''''''''''''''''''''''
my_string = "Hello, World!"
index = my_string.find('World')
# Output: 7

# ''''''''''''''''''''''''String Reversal:''''''''''''''''''''''''''
my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: "!dlroW ,olleH"

# ''''''''''''''''''''''''''String Comparison''''''''''''''''''''''''
# Compare two strings to check for equality or ordering.
str1 = "apple"
str2 = "banana"
print(str1 == str2)    # Output: False
print(str1 < str2)     # Output: True (lexicographically smaller)

# ''''''''''''''''''''''''''''''''String repetition''''''''''''''''''''''''''''''
str1="Hello World! "
str1=str1*2
print(str1)

# '''''''''''''''''''''''''''''''''''''String Joining:'''''''''''''''''''''''''''
# join a list of strings into a single string using the str.join() method.
strings = ['Hello', 'Python', 'World']
joined_string = '-'.join(strings)
print(joined_string)  # Output: 'Hello-Python-World'

# '''''''''''''''''''''''''''''''''''String Check and Manipulation:''''''''''''''''''''''''''''
my_string = "Hello, Python"
print(my_string.startswith("Hello"))   # Output: True
print(my_string.endswith("Python"))    # Output: True
print(my_string.isalpha())            # Output: False (isalpha(): Checks if all characters are alphabetic.)
print(my_string.isdigit())            # Output: False (isdigit(): Checks if all characters are digits.)
print(my_string.splitlines())         # Output: ['Hello, Python']  (isspace(): Checks if all characters are whitespace.)
print(my_str.isalnum())               #                             ( Checks if all characters are alphanumeric.)

# '''''''''''''''''''''''''''''''''Counting'''''''''''''''''''''''''''
my_string = "banana"
count = my_string.count("a")
print(count)  # Output: 3
# '''''''''''''''''''''''''''''''''String Encoding and Decoding:'''''''''''''''''''
# Convert strings to bytes using encoding and decode bytes to strings.
my_string = "Hello, World!"
encoded = my_string.encode("utf-8") #Converting string to bytes (UTF-8 encoding):
decoded = encoded.decode("utf-8") #Converting bytes to string (UTF-8 decoding):
print(encoded)  # Output: b'Hello, World!'
print(decoded)  # Output: Hello, World!

# ''''''''''''''''''''''''''''''''String Alignment:''''''''''''''''''''''''''''
my_string="Hello"
my_string.center(20)    # Centers the string in a field of width 20
my_string.ljust(20)     # Left-justifies the string in a field of width 20
my_string.rjust(20)     # Right-justifies the string in a field of width 20

# '''''''''''''''''''''''''''''''''''''''''String Zipping and Unzipping:''''''''''''''''''''''''''''''''''''''''


# ''''''''''''''''''''''''''''''''''''''''''''''''Removing whitespace:''''''''''''''''''''''''''''''
print('Hii')
my_string='  Hello World!           '
my_string.strip()      # Removes leading and trailing whitespace
print(my_string)

my_string='  Hello World!           '
my_string.lstrip()     # Removes leading whitespace
print(my_string)

my_string='  Hello World!           '
my_string.rstrip()     # Removes trailing whitespace
print(my_string)

# ''''''''''''''''''''''''''''''''''String Template:'''''''''''''''''''''''''''''''''
from string import Template

t = Template("$name is $age years old.")
result = t.substitute(name="Alice", age=30)
print(result)  # Output: "Alice is 30 years old."

# ''''''''''''''''''''''''''''''''''''''''String Padding (Advanced):'''''''''''''''''''''''''''
my_string = "42"
padded_string = my_string.zfill(5)
print(padded_string)  # Output: "00042"

aligned_string = my_string.rjust(5, "0")
print(aligned_string)  # Output: "00042"

# ''''''''''''''''''''''''''''''''''''''''String Checking (Advanced - Regular Expressions):'''''''''''''''''''''
import re

text = "Hello, World!"
pattern = r"Hello"
if re.search(pattern, text):
    print("Pattern found.")
else:
    print("Pattern not found.")

# ''''''''''''''''''''''''''''''''''''''String Justification:''''''''''''''''''''
my_string = "Hello"
left_justified = my_string.ljust(10)
right_justified = my_string.rjust(10)
center_justified = my_string.center(10)
print(left_justified)   # Output: "Hello     "
print(right_justified)  # Output: "     Hello"
print(center_justified) # Output: "  Hello   "

my_string = "Hello"
left_justified = my_string.ljust(10, '-')
right_justified = my_string.rjust(10, '-')
center_justified = my_string.center(10, '-')
print(left_justified)   # Output: "Hello-----"
print(right_justified)  # Output: "-----Hello"
print(center_justified) # Output: "--Hello---"


# '''''''''''''''''''''''''''''''''String Character Transformation:''''''''''''''''''''''''''
my_string = "Hello, World!"
translation_table = my_string.maketrans("HW", "hw")
transformed_string = my_string.translate(translation_table)
print(transformed_string)  # Output: "hello, world!"

# ''''''''''''''''''''''''''''''''''''''''''String Formatting with Template Strings:''''''''''''''''''''''''''''
from string import Template

name = "Alice"
age = 30
template_string = Template("My name is ${name} and I am ${age} years old.")
formatted_string = template_string.substitute(name=name, age=age)
print(formatted_string)
# Output: "My name is Alice and I am 30 years old."

# '''''''''''''''''''''''''''''''''''''''''''String Partitioning:''''''''''''''''''''''''''''''''''''''''''''
my_string = "apple-banana-orange"
first_part, separator, last_part = my_string.partition("-")
print(first_part)   # Output: "apple"
print(separator)    # Output: "-"
print(last_part)    # Output: "banana-orange"

# ''''''''''''''''''''''''''''''''''''String Splitting (Max Split):''''''''''''''''''''''''''''''
my_string = "apple,banana,orange"
split_list = my_string.split(",", maxsplit=1)
print(split_list)  # Output: ['apple', 'banana,orange']

# ''''''''''''''''''''''''''''''''''''''String Case Swapping:'''''''''''''''''''''''''''''''''''''''''
#  swap the case of a string using methods like swapcase().
my_string = "Hello, World!"
swapped_case_str = my_string.swapcase()
print(swapped_case_str)  # Output: "hELLO, wORLD!"

# ''''''''''''''''''''''''''''''''''''''''''''String Title Case:''''''''''''''''''''''''''''''''''''
my_string = "this is a title"
title_case_str = my_string.title()
print(title_case_str)  # Output: "This Is A Title"

# '''''''''''''''''''''''''''''''''''''String Checking (Case Sensitive):'''''''''''''''''''''''''''
my_string = "Hello, World!"
is_equal = my_string == "hello, world!"
print(is_equal)  # Output: False

