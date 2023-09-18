# # Concatenation
# string1 = 'Hello,'
# string2 = ' World!'
# print(string1 + string2)

# # Repetition
# print(string1 * 3)

# # Indexing
# print(string1[0])

# # Slicing
# print(string2[7:12])

# # Membership
# print('World' in string2)

# # Formatting
# print('{}, {}'.format(string1, string2))

# # '''''''''''''''''''''''''''''''''
# str1='GeeksforGeeks'
# print(str1[0])#First Elemnt of String
# print(str1[-1])#Last Elements of string
# print(str1[-2])#2nd Last Element of String
# ..............Reversing a Python String (6 different ways).................................
# str1='GeeksforGeeks'
# print(str1[::-1])

# # 1.Reverse a string in Python using a loop
# def Reverse_fun(s):
#     str1=''
#     for i in s:
#         str1=i+str1
#     print("In Reverse_fun(), reverese string str1 is ",str1)
#     return str1
# s='GeeksforGeeks'
# print("The Original String :",s)
# print("The Reverse String (using loop):",Reverse_fun(s))

# # # 2.Reverse a string in Python using recursion
# # def Recursive_Reverse(str1):
# #     if len(str1)==0:
# #         return str1
# #     else:
# #         return Recursive_Reverse(str1[1:])+str1[0]
# # s='GeeksforGeeks'
# # print('The Original String :',s)
# # print("Reverse String :",Recursive_Reverse(s))

# def Recursive_Reersive_String(str1):
#     if len(str1)==0:
#         return str1
#     else:
#         return Recursive_Reersive_String(str1[1:])+str1[0]
# input_string=input("Enter the string characters:\n")
# # input_string='GeeksforGeeks'
# print("The Reversed string :",Recursive_Reersive_String(input_string))

# # ''''''''''''''''''''''Reverse string in Python using stack
# # stack = []

# # # Adding elements to the stack (push)
# # stack.append(1)
# # stack.append(2)
# # stack.append(3)
# # print(stack)
# # # Removing elements from the stack (pop)
# # print(stack.pop()) # Output: 3
# # print(stack)
# # print(stack.pop()) # Output: 2
# # print(stack)
# # print(stack.pop()) # Output: 1


# # # '''''''''''''''''''''''''''''
# # # Function to create an empty stack. It
# # # initializes size of stack as 0
# # def createStack():
# # 	stack = []
# # 	return stack

# # # Function to determine the size of the stack
# # def size(stack):
# # 	return len(stack)

# # # Stack is empty if the size is 0
# # def isEmpty(stack):
# # 	if size(stack) == 0:
# # 		return true

# # # Function to add an item to stack . It
# # # increases size by 1
# # def push(stack, item):
# # 	stack.append(item)

# # # Function to remove an item from stack.
# # # It decreases size by 1
# # def pop(stack):
# # 	if isEmpty(stack):
# # 		return
# # 	return stack.pop()

# # # A stack based function to reverse a string
# # def reverse(string):
# # 	n = len(string)

# # 	# Create a empty stack
# # 	stack = createStack()

# # 	# Push all characters of string to stack
# # 	for i in range(0, n, 1):
# # 		push(stack, string[i])

# # 	# Making the string empty since all
# # 	# characters are saved in stack
# # 	string = ""

# # 	# Pop all characters of string and put
# # 	# them back to string
# # 	for i in range(0, n, 1):
# # 		string +=stack.pop()

# # 	return string


# # # Driver code
# # s = "Geeksforgeeks"
# # print("The original string is : ", end="")
# # print(s)
# # print("The reversed string(using stack) is : ", end="")
# # print(reverse(s))

# # # ''''''''''''''''''''''''''''
# # def reverse_string(input_string):
# #     stack = []
# #     for char in input_string:
# #         stack.append(char)
# #     reversed_string = ""
# #     while len(stack)>0:
# #         reversed_string += stack.pop()
# #     return reversed_string

# # input_string = input("Enter a string: ")
# # print("The reversed string is:", reverse_string(input_string))

# def Reverse_Stack_String(input_string):
#     stack=[]
#     for char in input_string:
#         stack.append(char)
#     reverse_string=""
#     while stack:
#         reverse_string+=stack.pop()
#     return reverse_string
# # Driver code 
# if __name__=='__main__':
#     input_string=input("Enter the character elements for string:\n")
#     print("The Original string :",input_string)
#     print("Reverse String :",Reverse_Stack_String(input_string))

# # '''''''''''''Reverse string in Python using an extended slice
# def Reverse_String(input_string):
#     # return input_string[::-1]
#     string=input_string[::-1]
#     return string
    
# # Driver code
# if __name__=='__main__':
#     input_string=input("Enter the elements of string:\n")
#     print("The Original string :",input_string)
#     print("The Reverse string :",Reverse_String(input_string))

# # ''''''''''''''''''''''Reverse string in Python using reversed() method
# def Reverse_string(input_string):
#     string=''.join(reversed(input_string))
#     return string
# # Driver Code
# if __name__=='__main__':
#     input_string=input("Enter the character for string\n")
#     print("The reversed string :",Reverse_string(input_string))

# # '''''''''''''''''''''Reverse string in Python using list comprehension()
# def Reverse_String(input_string):
#     l1=[input_string[i] for i in range(len(input_string)-1,-1,-1)]
#     print(l1)#['s', 'k', 'e', 'e', 'G', 'r', 'o', 'f', 's', 'k', 'e', 'e', 'G']
#     return ''.join(l1)
# # Driver code
# input_string=input("Enter the character elements of string:\n")
# print("The reversed string :",Reverse_String(input_string))

# # ''''''''''''''''''''Reverse string in Python using the function call
# def Reverse_string(input_string):
#     string=list(input_string)
#     string="".join(reversed(string))
#     return string
# # Driver Code
# input_string=input("Enter the character elements of string:\n")
# print("The Reversed string :",Reverse_string(input_string))

# # ''''''''''''''''''''''''''''
# gfg='geeksforgeeks'
# gfg="".join(reversed(gfg))
# print(gfg)

# /////////////////////////////////////String Slicing in Python//////////////////////////////////////////////////
# # Method 1: Using slice() method

# gfg='geeksforgeeks'
# print(gfg[slice(3)])#gee
# s1=slice(5)
# print(gfg[s1])
# s2=slice(1,7,2)
# print(gfg[s2])
# s3=slice(-1,-12,-2)
# print(gfg[s3])

# # Method 2: Using List/array slicing  [ : : ]  method
# gfg='GEEKSFORGEEKS'
# print(gfg[0:len(gfg)])
# print(gfg[4:])
# print(gfg[:8])
# print(gfg[::-1])# Reverse string

# # '''''''''''''''''''Using islice()'''''''''''''''''''
# import itertools
# str1='GeeksforGeeks'
# str2=itertools.islice(str1,0,5)# return itertools objects
# print(''.join(str2))

# import itertools
# s1="Welcome to GeeksforGeeks. GFG is the best Computer Science Portal"
# print(''.join(itertools.islice(s1,0,7)))

# '''''''''''''''''''''''''''''''String in Python''''''''''''''''''''
# str1="GeeekforGeeks"
# print(str1[::-1])
# print("".join(reversed(str1)))
# print("-".join(str1))
# print(reversed(str1))
# str2=reversed(str1)
# print(str2)

# # ''''''''''updation string''''''''''''''
# str1='GFG'
# l1=list(str1)
# print(l1)
# l1.insert(1," ranjit ")
# print(l1)
# # str1="".join(l1)
# # print(str1)
# l1[2]=" kumar "# replace
# print(l1)
# str1="".join(l1)
# print(str1)

# str1="Geekforgeeks"
# str1=str1[:4]+" ranjit kumar "+str1[4:]
# print(str1)

# # '''''''''''''''''''''Deleting String'''''''''''''
# str1="geekforgeeks"
# l1=list(str1)
# l1=l1[:4]+l1[7:]
# print(l1)
# str1="".join(l1)
# print(str1)
# str1="geekforgeeks"
# str1=str1[:4]+str1[7:]
# print(str1)
# # del str1
# # # print(str1) # str1 is not available now  

# l1=[1,2,3]
# del l1
# print(l1) # l1 is not available now

