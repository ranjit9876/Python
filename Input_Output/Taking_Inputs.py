# *************************************************************
# # '''''''''''''''''1. Using the input() function:''''''''''''''''''''''
# # Taking a single input
# n = int(input())
# print(n)

# # Taking multiple inputs on the same line
# # a, b, c = map(int , input())
# a, b, c = map(int , input().split())
# print(a, b, c)

# # Taking a list of integers as input
# arr = list(map(int, input().split()))
# print(arr)

# # ''''''''''''''''''''''2.Using the sys module:''''''''''''''''''''''''''''
# # import sys
# from sys import stdin, stdout

# # Taking a single input
# n = int(stdin.readline())
# print("n = %d" % n)
# # Taking multiple inputs on the same line
# a, b, c = map(int, stdin.readline().strip().split())
# print(f"a={a} b={b} c={c}")

# # Taking a list of integers as input
# arr = list(map(int, stdin.readline().strip().split()))
# print(f"arr={arr}")

# # '''''''''''''''''''''''3.Preprocessing inputs:'''''''''''''''''''''''''''
# # Taking a string as input and converting it to a list of characters
# # s = list(input().strip())
# s = list(input().strip().split(','))
# print(f"s={s}")

# # Taking a string of integers as input and converting it to a list of integers
# arr = list(map(int, input().split(',')))
# print(f"arr={arr}")

# *****************************************************************************
# # '''''''''''''''''''''1. Reading Single Input'''''''''''''''''''''''''
# # Reading Single Integer
# # n,m=int(input().strip().split(',')) # error: int() argument must be a string, a bytes-like object or a real number, not 'list'

# n = int(input())

# # Reading a single string
# name = input()

# # Reading a single float
# x = float(input())

# # ''''''''''''''''''''''2. Reading Multiple Input Values on a Single Line:''''''''''''''''''''''''''
# # Reading two integers on a single line
# a, b = map(int, input())

# # Reading three floats on a single line
# x, y, z = map(float, input().split())

# # Reading multiple integers on a single line
# numbers = list(map(int, input().split()))

# # ''''''''''''''''''''''''3. Reading Input Array/List:''''''''''''''''''''''''
# # Reading a list of integers on a single line
# numbers = list(map(int, input().split()))
# print(f'numbers: {numbers}')

# # Reading a list of floats on a single line
# floats_list = list(map(float, input().split()))
# print(f'floats_list: {floats_list}')

# # '''''''''''''''''''''4. Reading Input in Multiple Lines:'''''''''''''''''''''''
# # Reading 'n' integers on separate lines and storing them in a list
# print("Enter the size of 1D array/list of integers:")
# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# print(f"numbers: {numbers}")

# # Reading a 2D array/matrix
# print("Enter size of a 2D array/matrix of integers: ")
# rows, cols = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(rows)]
# print(f"matrix: {matrix}")

# '''''''''''''''''''''5. Handling End-of-File (EOF): '''''''''''''''''''''''''''''''''
# # Reading multiple lines until EOF (End of File)
# while True:
#     try:
#         n = int(input())  # Read integer from the current line
#         # Process n

#     except EOFError as e:
#         print("Get Error Code: " + str(e))
#         break  # End loop when no more input is available

# # '''''''''''''''''''''
# try:
#     while True:
#         # Read input and process the problem
#         n=int(input())
#         print(f"n={n}")
# except EOFError as e:
#     # End of input reached
#     print(f"Error: {e}")

# # '''''''''''''''''''''''''''''''''''''Taking input from standard input(stdin)''''''''''''''''''''''''
# # For single integer input
# n = int(input())

# # For multiple integers on a single line
# a, b, c = map(int, input().split())

# # For a list of integers on a single line
# numbers = list(map(int, input().split()))

# # For a string input
# s = input()

# # For multiple strings on separate lines
# strings = []
# for _ in range(n):
#     s = input()
#     strings.append(s)
#     # strings.append(input())

# # '''''''''''''''''''''''''Taking input from command line arguments''''''''''''''''''''''
# import sys

# # input() == sys.argv[1]
# # For a single integer argument
# n = int(sys.argv[1])
# print(f"n={n}")

# # For multiple integers as arguments
# a, b, c = map(int, sys.argv[1:4])

# # For a list of integers as arguments
# numbers = list(map(int, sys.argv[1:]))

# # For a string argument
# s = sys.argv[1]

# # For multiple string arguments
# strings = sys.argv[1:]

# # '''''''''''''''''''''''Taking input from a file''''''''''''''''''''''''''''
# # Assuming the input is stored in a file called "input.txt"
# with open("input.txt", "r") as f:
#     # For a single integer input
#     n = int(f.readline())
#     print(f"n={n}")

#     # For multiple integers on a single line
#     a, b, c = map(int, f.readline().split())
#     print(f"a={a} b={b} c={c}")

#     # For a list of integers on a single line
#     numbers = list(map(int, f.readline().split()))
#     print(f'numbers={numbers}')

#     # For a string input
#     s = f.readline().strip()
#     print(f's={s}')

#     # For multiple strings on separate lines
#     n=4
#     strings = []
#     for _ in range(n):
#         s = f.readline().strip()
#         strings.append(s)
#     print(f'strings={strings}')


# # Read multiple space-separated strings from input
# strings = input().split()
# print(f'strings={strings}')

# # ''''''''''''''''''''''''''''''''''''Reading input with known structure:''''''''''''''''
# # Read the number of test cases
# t = int(input())

# # Process each test case
# for _ in range(t):
#     # Read input for each test case
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(f"arr: {arr}")

# # ''''''''''''''''''''''''''''''Reading a Matrix (2D List):''''''''''''''''''''''''''''
# rows,col=map(int, input().split())
# matrix = []
# for _ in range(rows):
#     row=list(map(int, input().strip().split()))
#     matrix.append(row)
# print(f"matrix: {matrix}")

# # ''''''''''''''''''''''''''''Reading a Graph (Adjacency List):'''''''''''''''''''''''''''''
# vertices=5
# edges=6
# graph = [[] for _ in range(vertices)]
# for _ in range(edges):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)  # Remove this line for directed graphs

# print(f"graph: {graph}")

# # ''''''''''''''''''''''Reading Input until End of File (EOF):''''''''''''''''''''''''''''
# import sys
# # Read multiple lines of input until EOF (End of File)
# lines = []
# for line in sys.stdin:
#     lines.append(line.strip())

# # ''''''''''''''''''''''''Reading list of characters'''''''''''''''''
# s=list(input())
# print(s)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Read multiple lines of input until EOF (End of File)
# lines = []
# while True:
#     try:
#         line = input().strip()
#         lines.append(line)
#     except EOFError:
#         break

# # '''''''''''''''''''''''''''''command line argument'''''''''''''''''''
# import argparse

# # Creating an ArgumentParser object
# parser = argparse.ArgumentParser()

# # Adding an argument
# parser.add_argument('filename', help='Input file name')

# # Parsing the arguments
# args = parser.parse_args()

# # Reading the input file
# with open(args.filename, 'r') as file:
#     # Process the file contents as per the problem requirements
#     print(file.read)

# # '''''''''''''''''''''Reading input with known structure'''''''''''''''''
# # Reading input with known structure
# n = int(input())  # Number of lines
# for _ in range(n):
#     a, b, c = map(int, input().split())  # Read three integers from each line
#     # Process a, b, c

# # Reading input into a 2D list
# grid = [list(map(int, input().split())) for _ in range(n)]  # Read n lines of space-separated integers

# # '''''''''''''''''Reading input until a specific condition is met:'''''''''''''''''''''''
# # Reading input until a specific condition is met
# while True:
#     n = int(input())
#     if n == 0:
#         break  # Terminate the loop when n is 0
#     # Process n

# # ''''''''''''''''''''''''Using list comprehension for concise input processing:''''''''''''''''''
# # Read a single integer
# n = int(input().strip())

# # Read multiple integers on a single line
# a, b, c = [int(x) for x in input().strip().split()]

# # Read a list of integers on a single line
# numbers = [int(x) for x in input().strip().split()]

# # Read a string
# s = input().strip()

# # Read multiple strings on separate lines
# strings = [input().strip() for _ in range(n)]

# # ''''''''''''''''''''''''''''Using a generator function for memory-efficient input:''''''''''''''''''''''''''''''''
# import sys
# def get_input():
#     for line in sys.stdin:
#         yield line.strip()

# input_gen = get_input()
# print(f"input_gen: {input_gen}")

# # Read a single integer
# n = int(next(input_gen))
# print(f"n={n}")
# # Read multiple integers on a single line
# a, b, c = map(int, next(input_gen).split())
# print(f"a={a}, b={b}, c={c}")

# # Read a list of integers on a single line
# numbers = list(map(int, next(input_gen).split()))
# print(f"numbers={numbers}")

# # Read a string
# s = next(input_gen)
# print(f"s={s}")

# # Read multiple strings on separate lines
# strings = [next(input_gen) for _ in range(n)]
# print(f"strings={strings}")

# ****************************************Advanced input programming ********************************
# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Importing the required libraries
# import sys
# from typing import List, Tuple

# # Function to read integers from input
# def read_int() -> int:
#     return int(sys.stdin.readline().strip())

# # Function to read a list of integers from input
# def read_int_list() -> List[int]:
#     return list(map(int, sys.stdin.readline().strip().split()))

# # Function to read space-separated integers on a single line
# def read_ints() -> Tuple[int]:
#     return tuple(map(int, sys.stdin.readline().strip().split()))

# # Function to read a string from input
# def read_str() -> str:
#     return sys.stdin.readline().strip()

# # Function to read a list of strings from input
# def read_str_list() -> List[str]:
#     return sys.stdin.readline().strip().split()

# # Example usage
# n = read_int()  # Read a single integer
# print(f"n={n}")
# a, b, c = read_ints()  # Read multiple integers
# print(f"a={a} b={b} c={c}")
# numbers = read_int_list()  # Read a list of integers
# print(f"numbers={numbers}")
# s = read_str()  # Read a string
# print(f"s={s}")
# strings = read_str_list()  # Read a list of strings
# print(f"strings={strings}")

# # '''''''''''''''''''''''''''''''''''''''''''''
# import sys
# n=5
# # For multiple strings on separate lines
# strings = [sys.stdin.readline().strip() for _ in range(n)]
# print(f"strings={strings}")
# # ''''''''''''''''''''''''''''''''''''''''''''''
# # Read multiple strings on separate lines
# strings = [input().strip() for _ in range(n)]

# # ''''''''''''''''''''''''''''''''''''''Using generator functions:'''''''''''''''''''''''''''''''''
# def read_int():
#     for i in map(int, input().split()):
#         yield i
# print(f"read_int: {read_int()}")

# def read_int_list():
#     return list(read_int())
# print(f"read_int_list(): {read_int_list()}")

# # Read multiple integers on a single line
# a, b, c = read_int_list()
# print(f"a: {a}, b: {b}, c: {c}")

# # Read a list of integers on a single line
# numbers = read_int_list()
# print(f"numbers: {numbers}")

# # '''''''''''''''''''''''''Using numpy for matrix input:''''''''''''''''''''''''
# import numpy as np

# # Read a 2D matrix of integers
# matrix = np.array([list(map(int, input().split())) for _ in range(n)])
# print(matrix)

# # '''''''''''''''''''''''''Fast I/O using read() and write():'''''''''''''''''''''''''''''''''
# import sys

# # For single integer input
# n = int(sys.stdin.read(1))
# print(f"n={n}")

# # For multiple integers on a single line
# a, b, c = map(int, sys.stdin.read().split(','))
# print(f"a={a} b={b} c={c}")

# # For a list of integers on a single line
# numbers = list(map(int, sys.stdin.read().split()))
# print(f"numbers: {numbers}")

# # For a string input
# s = sys.stdin.read().strip()
# print(f"s: {s}")

# # For multiple strings on separate lines
# strings = sys.stdin.read().splitlines()
# print(f"strings: {strings}")

# # Output using sys.stdout
# sys.stdout.write("Output\n")
# sys.stdout.flush()

# # ''''''''''''''''''''''''''''Python program showing how to take multiple input using List comprehension''''''''''''''''''''''''

# # taking two input at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)

# # taking three input at a time
# x, y, z = [int(x) for x in input("Enter three values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print("Third Number is: ", z)

# # taking two inputs at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First number is {} and second number is {}".format(x, y))

# # taking multiple inputs at a time
# x = [int(x) for x in input("Enter multiple values: ").split()]
# print("Number of list is: ", x)

# # ''''''''''''**********Not Understanding***********'''''''''''Using numpy as array inputs''''''''''''''''''''''''''
# import numpy as np

# # For a single line of space-separated integers
# arr = np.array(input().split(), dtype=int)

# # For a matrix input
# n, m = map(int, input().split())
# matrix = np.zeros((n, m), dtype=int)
# for i in range(n):
#     matrix[i] = np.array(input().split(), dtype=int)

# # '''''''''''''''''''''''''''Using readlines() for multiple inputs:'''''''''''''''''''''
# import sys
# lines1=sys.stdin.readline()
# lines2=sys.stdin.readlines()
# print(f"lines1: {lines1}")
# print(f"lines2: {lines2}")

# # Accessing the individual lines
# n=int(lines2[0])
# print(f"n: {n}")

# a,b,c=map(int,lines2[1].split())
# print(f"a: {a},b: {b},c: {c}")

# '''''''''''''''''''''''''