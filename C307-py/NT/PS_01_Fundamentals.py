'''

Syntax – introduce basic Python programming syntax.


Variables – how to create concise and meaningful variables.
Data types overview – integers, floats, strings, booleans, complex numbers.
Input and Output – using input() and print() for user interaction.
Strings – learn about string data and basic string operations.
Numbers – integer, float, and complex number handling.
Booleans – truthy and falsy values.
Constants – defining constants in Python.
Comments – adding notes in code.
Type conversion – convert values between types.
type(), id(), and isinstance() – inspecting data types.

resource 1:
https://www.alphacodingskills.com/python/python-variables.php

'''
# Variables

# - Parallel Assignment
x , y = 10,20
print(x)
print(y)

x, y = [1, 2, 3], ('red', 'blue', 'green')
print(x)
print(y)

# Global Variable

glob_var = 1010 #Global Variable

def fn():

    glob_var =2020  #local variable 
    global glob_var1  #creating global variable inside function 
    glob_var1 =2020  #local variable 
    print(glob_var)

fn()
print(glob_var)
print("===>" , glob_var1)


############ concatination



# To combine string value of two or more variable inside print() function, 
# comma (,) operator is used which concatenates string values of variables 
# with a whitespace.

stud_name = "John"
age = 23
nick_name = "Yokhanan"

print(stud_name,age,nick_name)
 
# Alternatively, it can also be achieved with plus (+) character but with some limitation. 
# It combines two or more variables of same datatypes. 
# With string datatype, it returns concatenated variables and 
# with number datatypes it returns sum of the variables. 
# With mixed datatypes, it will raise an exception.

stud_name = "shivam"
age = 23
nick_name = "jak"

print(stud_name+nick_name)
print(age+10)
print(stud_name+age,nick_name)



##################