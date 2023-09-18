# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Method 1: Using the print() function with concatenation
# name = "John"
# age = 25
# print("My name is " + name + " and I am " + str(age) + " years old.")

# # Method 2: Using the print() function with formatted string
# print("My name is {} and I am {} years old.".format(name, age))

# # Method 3: Using f-strings (Python 3.6+)
# print(f"My name is {name} and I am {age} years old.")

# # Method 4: Using multiple print() statements
# print("My name is", name, "and I am", age, "years old.")

# # Method 5: Using the join() method
# output = " ".join(["My name is", name, "and I am", str(age), "years old."])
# print(output)

# # Method 6: Using string concatenation
# output = "My name is " + name + " and I am " + str(age) + " years old."
# print(output)
# # print("My name is " + name + " and I am " + str(age) + " years old.")


# # Method 7: Using string formatting
# a = 3.14159
# b = 2.71828
# print("The values are {:.2f} and {:.3f}".format(a, b))

# # Method 8: Using % operator (old-style formatting)
# count = 5
# message = "cats"
# print("I have %d %s." % (count, message))

# # Method 9: Writing output to a file
# with open("output.txt", "w") as f:
#     f.write("This is some output text.")

# # Method 10: Redirecting output to a file
# import sys
# sys.stdout = open("output.txt", "w")
# print("This is some output text.")
# sys.stdout.close()

# # Methode 10: Redirecting standard output to a file
# import sys
# with open("output.txt", "w") as file:  # file = open("output.txt", "w")
#     sys.stdout = file  # sy.stdout = open("output.txt", "w")
#     print("This will be written to the file.")

# # Methode 11: Printing to the console and a file simultaneously
# import sys
# with open("output.txt", "w") as file:
#     original_stdout = sys.stdout
#     sys.stdout = file
#     new_stdout = sys.stdout
#     print("This will be written to the file.")

#     sys.stdout = original_stdout
#     print("This will be printed to the console.")

#     sys.stdout = new_stdout
#     print("This will be printed to the file Again.")

# # Method 11: Using sys.stdout.write()
# import sys
# sys.stdout.write("This is some output text.\n")

# # Method 12: Using logging module
# import logging
# logging.basicConfig(filename='output.log', level=logging.INFO)
# logging.info("This is some output text.")

# # Method 13: Displaying output in a GUI window
# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(window, text="Hello, World! Ranjit Kumar Gupta")
# label.pack()
# window.mainloop()

# # Using f-strings with expressions (Python 3.8+)
# age=20
# print(f"Next year, I will be {age + 1} years old.")

# # ''''''''''''Using formatted output with the % operator:'''''''''''''''''''
# message = "Hello, %s! i am %d years old" % ("World",20)
# print(message)

# # '''''''''''''''''''''Using formatted output with the format() method:''''''''''''''''''
# message= "Hello {}, I am {} years old".format("Hello",20)
# print(message)

# # ''''''''''''''''''''''''''''''''1.Using repr()''''''''''''''''''''''''''''''''''''''''''''
# # The repr() function returns a string representing a printable version of the output object.
# l1=[1,2,3,4]
# print(l1)
# print(repr(l1))

# # '''''''''''''''''''''
# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def __repr__(self):
#         return f"MyClass(value={self.value})"

# obj = MyClass(42)
# print(obj)           # Output: <__main__.MyClass object at 0x00000123ABCDEF>
# print(repr(obj))     # Output: MyClass(value=42)

# # ''''''''''''''''''''2. Using pprint module:'''''''''''''''''''''''''''''''''''''''''
# '''The pprint module provides a pprint() function that can be used to pretty-print complex data structures, such as
# dictionaries or lists, in a well-formatted and readable way. Here's an exampl'''

# import pprint
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# pprint.pprint(my_dict) #well-formed by alphabetic order of keys
# print(my_dict)

# # ''''''''''''''''''''''''3. Using print() '''''''''''''''''''''''
# # print() function is used to display output on the console or terminal
# name = "John Doe"
# age = 25
# height = 1.75

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import sys
# from io import StringIO

# stdout = sys.stdout
# sys.stdout = StringIO()

# # Your code that generates output
# print("Hello, world!")
# print("GFG!")
# output = sys.stdout.getvalue()
# sys.stdout = stdout
# print("Hello, world! Hii")

# # '''''''''''''''''''''''''''''''''''''Error Messages and Tracebacks:'''''''''''''''''''''''''''
# import sys
# from io import StringIO

# stderr = sys.stderr
# sys.stderr = StringIO()

# # Your code that generates error messages
# # print(num)
# errors = sys.stderr.getvalue()
# # print(num)
# sys.stderr = stderr
# # print(num)

# # ''''''''''''''''''''''''''''''''''''''''Logging''''''''''''''''''''''''''''''''''

"""Logging module: Use the logging module to record events and errors during the execution of your program. 
You can configure it to provide different levels of detail, including timestamps, error levels, and custom messages.
"""

# import logging

# logging.basicConfig(filename='output.log', level=logging.INFO)
# logger = logging.getLogger()

# # Your code that generates log messages

# logger.info('This is an informational message')

# # ''''''''''''''''''''''''''''''''''''''''''''''''Using "json" module'''''''''''''''''''''''''''''''
"""The json module provides methods for encoding and decoding JSON data. 
It can be used to convert Python objects into JSON strings and vice versa."""

# import json
# import pprint
# data = {"name": "John", "age": 30, "city": "New York"}
# # print(json.dumps(data, indent=4))
# output = json.dumps(data, indent=4)
# print(output)
# # pprint.pprint(output)
# pprint.pprint(data)

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# '''''''''''''''basic systex of print fuction''''''''''''''''''''
# print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)


"""value1, value2, ...: The values or expressions to be printed. You can provide multiple values separated by commas.
sep=' ': (optional) The separator between the values. By default, it is a single space ' '.
end='\n': (optional) The character(s) to be appended at the end of the output. By default, it is a newline character '\n'.
file=sys.stdout: (optional) The file object where the output will be directed. By default, it is the console (standard output).
flush=False: (optional) Whether to flush the output buffer. By default, it is set to False, meaning the output is buffered."""

# # '''''''''''''''''''''''''''''''''''Exception Handling'''''''''''''''''''''''''''''''''''''''
# try:
#     # Code that may raise an exception
#     print(num)
# except Exception as e:
#     print("An error occurred:", e)

# # ''''''''''''''''''''''''''''''''Logging module'''''''''''''''''''''''''''''''
# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.debug("This is a debug message")

# age = 20
# # Using f-strings with expressions (Python 3.8+)
# print(f"Next year, I will be {age + 1} years old.")

# # ''''''''''''''''''''''''''''''''''''''
# import time
# count_time=3
# for i in reversed(range(count_time+1)):
#     if i>0:
#         print(i,end=">>>",flush=True)
#         time.sleep(1)
#     else:
#         print("start")

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# a=12
# b=12
# c=2022
# print(a,b,c,sep="-")

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import io

# # declare a dummy file
# dummy_file = io.StringIO()

# # add message to the dummy file
# print('Hello Geeks!!', file=dummy_file)

# # get the value from dummy file
# print(dummy_file.getvalue())
# # '''''''''''''''''''''''''''''''''''''''''''''
# file1=open("output.txt","w")
# # print("Welcome to output.txt file through Python_Output.py File:", file=file1)
# print('Welcome to GeeksforGeeks Python world.!!', file=open('output.txt', 'w'))

# ''''''''''''''''''''''''''''''''''print without newline '''''''''''''''''''''''''
# print("Hello world!",end=" ")
# print("Welcome to GFG")

# l1=[1,2,3,4,5,6,7,8,9,10,11,12]
# print(*l1)

# import sys
# sys.stdout.write("Hello world!")
# sys.stdout.write("Welcome to GFG")

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# print('G', 'F', sep="", end="")
# print('G')
# # \n provides new line after printing the year
# print('09', '12', '2016', sep='-', end='\n')

# print('Red', 'Green', 'Blue', sep=',', end='@')
# print('geeksforgeeks')
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import antigravity
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # ''''''''''''''''''''''Formatting output using String modulo operator(%) : ''''''''''''''''''''''''''
""" %[flags][width][.precision]type """

# # print integer and float value
# print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

# # print integer value
# print("Total students : %3d, Boys : %2d" % (240, 120))

# # print octal value
# print("%7.3o" % (25))

# # print exponential value
# print("%10.3E" % (356.08977))

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

