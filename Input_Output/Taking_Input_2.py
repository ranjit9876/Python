# ***********************************Taking multiple inputs from user in Python********************************
# # ''''''''''''''''''''''''1. Using List comprehension :'''''''''''''''''''''''''''''''''''''''''''''
# # taking two input at a time
# x, y = [int(x) for x in input("Enter two values: ").strip().split()]
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

# How to input multiple values from user in one line in Python
# x, y = input(), input()
# print(f"x={x} y={y}")
# x, y = input().split()
# print(f"x={x} y={y}")

# x,y=[int(x),int(y)]
# print(f"x={x} y={y}")

# x, y = [int(x) for x in [x, y]]
# print(f"x={x} y={y}")

# x,y=[int(x) for x in input().split()]
# print(f"x={x} y={y}")

# x, y = map(int, input("Enter two numbers:\n").split())
# print(f"x={x} y={y}")

# import sys
# line=[int(x) for x in sys.stdin.readline().strip().split()]
# print(f"line={line}")

# # ''''''''''''''''''''''''''''''''''''''Taking a matrix input ''''''''''''''''''''''''
# Row = int(input())
# Col = int(input())
# matrix = []
# print("Enter the entries the rowwise: ")
# for i in range(Row):
#     arr = []
#     for j in range(Col):
#         arr.append(int(input()))
#     matrix.append(arr)
# # For printing the matrix
# for i in range(Row):
#     for j in range(Col):
#         print(matrix[i][j], end=" ")
#     print()

# # ''''''''''''''''''''
# R=int(input())
# C=int(input())
# # one-liner logic to take input for rows and columns
# mat = [[int(input()) for x in range (C)] for y in range(R)]
# print(mat)

# # '''''''''''''''''''''''''
# import numpy as np
# R=int(input())
# C=int(input())
# print("Enter the entries in a single line (separated by space): ")
# entries=list(map(int, input().split()))

# # For printing the matrix
# matrix = np.array(entries).reshape(R, C)
# print(matrix)

# # '''''''''''''''''''''''Take input from user and store in .txt file '''''''''''''''''''''''''''
# # Take input from the user
# input_data = input("Enter your input: ")

# # Specify the file name
# file_name = "input.txt"

# # Open the file in write mode and write the input
# with open(file_name, "w") as file:
#     file.write(input_data)

# print("Input saved to", file_name)

# # '''''''''''''''''''''
# # Take input from the user
# lines = []
# print("Enter input (type 'END' to finish):")
# while True:
#     line_entities = input()
#     if line_entities == 'q': #q for "quite"
#         break
#     lines.append(line_entities)

# # Specify the file name
# file_name = "input.txt"

# try:
#     # Open the file in write mode and write the input
#     with open(file_name, "w") as file:
#     # for value in lines:
#     #     file.write(value + "\n")
#         file.write(" ".join(lines))
# except Exception as e:
#     print("Error occurred while writing file: " + str(e))
# print("Input saved to", file_name)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# import sys

# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')

# print("Exit")

# # '''''''''''''''Reading multiple files by providing file names in fileinput.input() function argument''''''''''''''''''''''''
# import fileinput

# with fileinput.input(files=('sample.txt', 'input.txt','sample.txt')) as f:
# 	for line in f:
# 		print(line)

# # '''''''''''''''''''Reading multiple files by passing file names from command line using fileinput module'''''''''''''''''''''
# import fileinput

# for f in fileinput.input():
#     if 'q'==f.rstrip():
#         break
#     print(f)

# # '''''''''''''''''''''''''''
# # *s,l = input().split()
# s,*l = input().split()
# l = list(map(int,l))
# print(s)
# print(l)

# # ''''''''''''''''''
# _,n,*l = input().split()
# n = int(n)
# l = list(map(int,l))
# print(_)
# print(n)
# print(l)

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # template begins
# #####################################

# # import libraries for input/ output handling
# # on generic level
# import atexit
# import io
# import sys

# # A stream implementation using an in-memory bytes
# # buffer. It inherits BufferedIOBase.
# buffer = io.BytesIO()
# sys.stdout = buffer

# # print via here


# @atexit.register
# def write():
#     sys.stdout.write(buffer.getvalue())

# #####################################
# # template ends


# # normal method followed
# # input N
# n = int(input())

# # input the array
# arr = [int(x) for x in input().split()]

# # initialize variable
# summation = 0

# # calculate sum
# for x in arr:
#     summation += x

# # print answer
# print(summation)

# '''''''''''''''''''''''''''''''''''''''''''''''''''
