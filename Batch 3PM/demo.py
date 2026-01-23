# Python is a 
# high-level, 
# general-purpose, 
# interpreted 
# programming language.

# Syntax

a = 20
b = 30


print(a+b)

# variables
stud_name  = "aditya pal"
print("dear" , stud_name)
print("hello" , stud_name , "." , stud_name , "is 20 years old.", stud_name ," is a PBI developer")


# Input Output
# numbers = input("===>")
# print(numbers)

# user_name = input("please type ur name :")
# user_age = input("please type ur Age :")
# print("Hey",user_name,"you are",user_age)


print("#########################")

# variable and value updation

data = 1010
print(data) #1010

data = "hello"
print(data) # hello



print("#########################")
# Data types overview – integers, floats, strings, booleans, complex numbers.

data = "Hello" # str
data = 1010 # Int
data = 10.10 # float
data = True # bool

chech_type = type(data)

print(chech_type)




print("######################### Strings")


# Strings – learn about string data and basic string operations.

data = 'Hello there'

data = "hello"

data = '''this
 is for multi
   line '''


txt = '''this is also used 
for 
multi line comment'''

print(txt)


# data = 'Aditya's New Phone' # ❌
data = "Aditya's New Phone" # ✔


# data = "Aditya "New Phone"" # ❌
data = 'Aditya "New Phone"' # ✔





print("################## Comments")

# this is used for single line comment


'''this is also used 
for 
multi line comment'''







print("################## variable naming convention ############")
# starts with letters - 1stnum  ❌ num1
# never use space - num 1 
# Use camelCase - studentNameOfThisYear 
# In py variable names are casesensetive
# num1 = 10
# Num1 = 20
# print(num1)
# print(Num1)



# num_1 = 1010
# print(num_1)

print("################## Numbers ############")


num_1 = 1010
num_1 = 10.10
print(type(num_1))



num_1 = 10000000
num_1 = 10_00_00_000
print(num_1)

print("################## Boolean ############")

# True/False

data = True

result = 10<20
# data  = 0
data  = []
# data  = ""
# data  = text
print(data)
# data  = ["dfvg"]

print(bool(data))




# print(result)








print("################## Operators ############")

# arithmetic operators
x = 10
y = 10
z = x + y
z = x * y


z = 10 ** 3 # 10 X 10 X 10 # Exponantion
z = 11 % 2 # Modulas
z = 11 // 2 # flour
print(z)