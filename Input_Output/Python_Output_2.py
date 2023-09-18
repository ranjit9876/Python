# ''''''''''''''''''''''''''Standard Output by print()''''''''''''''''''''''''''
print("Hello World!")
print("Hello World!","Hii",123)

# '''''''''''''''''''''''''''''''''''''''''String Concatinate''''''''''''''''''''''''''''''
name="Ranjit Kumar"
age=19
# print("Hello "+" World! "+"my name is "+name+" and age: "+age) # TypeError: can only concatenate str (not "int") to str
print("Hello World!"+" My name :"+name+" and age: "+str(age))

# '''''''''''''''''''''''''''''''''''''''Formatted strings (f-strings):'''''''''''''''''''''''''''''''
name = "Bob"
age = 35
print(f"My name is {name} and I am {age} years old.")

# '''''''''''''''''''''''''''''Escape sequences:'''''''''''''''''''''''''''''
print("Hello World!\nMy name is Ranjit")

# ''''''''''''''''''''''''''Separator and end parameters''''''''''''''''''''''''''''''''
print("First", "Second", "Third", sep="-", end="\n\n")
print("Forth")