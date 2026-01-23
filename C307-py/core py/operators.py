# Section 2. Operators

## Topics
# - Arithmetic operators
# - Assignment operators
# - Comparison operators
# - Logical operators

# - Identity operators (`is`, `is not`)
# - Membership operators (`in`, `not in`)
# - Bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`)

# - Arithmetic operators
x = 20
y = 50


'''
+
-
/
* 
**
//
%

'''
print(y*x)
print(y**x) # 50 X 50 X 50......20 Times
print(11/2) # 5.5
print(11//2) # 5
print(11%2) # 1

########## Assignment operators
'''
+=
-=
/=
*=
**=
//=
%=

'''
x = 5
# x = 10
# print(x)

# x = x + 10
# x +=  10
# x = x * 10
# x *=  10
x **=  2

print(x)

############ - Comparison operators

z = x>y
print(z)

print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)


################# - Logical operators
# and or not
print("################# - Logical operators")


print(10>15 and 15>12)
print(10>15 or 15>12)
print(not(10>15))


