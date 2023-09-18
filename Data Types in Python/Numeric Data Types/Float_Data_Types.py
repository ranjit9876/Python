# from decimal import Decimal as d
# h=d(0.7+0.2) # will give exact lengthy answer
# h=d(0.7)+d(0.2) # will give exact half answer
# h=d('0.7')+d("0.2") # print 0.9
# print(h)
# print(type(h)) # <class 'decimal.Decimal'>

# a=0.7 ; b= 0.2
# c=a+b
# print(c)
# print("%.1f" %c)

# # print(7/0) # ZeroDivisionError: division by zero

# print(dir(__builtins__))

# # # ''''''''''''''''''''''''''''
# from fractions import Fraction as f
# # a=f(1,0)
# a=f(1,1)
# print(a)
# a=f(1,5)
# print(a)
# b=f(2)
# print(b)
# d=f(0,5)
# print(d)
# v=f(5,25)
# print(v)

# a=2_300_400
# print(a,type(a)) # 2300400 <class 'int'>

'''Note: We can use Underscore _ in between the numbers 
for clarity in reading and understanding the number.
Ex: 1_23 is same as 123 one hundred and twenty three'''

# a=1_2.3
# print(a,type(a)) # 12.3 <class 'float'>

# b=1_3.0
# print(b,type(b))  # 13.0 <class float'>

# c=1._03
# d=1_.03
# e=_14.3
# g=1_4.3

# a=5;b=4.6
# print(a,type(a))
# print(b,type(b))
# print(isinstance(a ,int))
# print(isinstance(a,float))
# print(isinstance(a,bool))
# print(isinstance(b,float))
'''Note: syntax  isinstance(variable,datatype) '''

# c=4j
# print(c,type(c))
# d=1+3j
# print(d,type(d))
# print(isinstance(d,complex))

# from fractions import Fraction as F
# print(F(6,2))
# print(F(2.5))
# print(F('2.5'))
# print(F("2.5"))
# print(F(4.5))
# print(F(5,0))
# b=5/0
# v=F(5,20)
# print(v)

# g=2+3j
# print(g,type(g))
# print(g.real)
# print(g.imag)
# h=7*2.3j
# print(h,type(h))
# print(h.real)
# print(h.imag)

# print(1e0)
# print(4e0)
# print(1e1)
# print(1e2)
# print(12e2)
# print(1.4e0)
# print(1.4e1)
# print(1.4e2)
# print(1.4e3)

# print(4*5)
# print(2**3)
# print(2**4)
# print(1.5**2)
# print(4**3)

# import math as m
# print(m.exp(3)) # e=2.71828 , e*e*e
# print(m.exp(1))