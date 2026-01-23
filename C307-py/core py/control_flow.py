# control flow
# - if…else statement

# if(condition - True | False):
#     print("step 2")


# age = 19

# print("step 1")

# if(age>18):
#     print("step 2")

# print("step 3")

# age = input()
# age = int(age)

# age = int(input("type any num : "))

################### Type conversion

# age = "12"
# age = int(age)
# print(type(age))

# input() - always returns str data type

####################################

# if(age>18):
#     print("Eligible")
# else:
#     print("Not Eligible")


# 18-120 = Eligible
# else - Not Eligible

# if(age>18 and age<120):
#     print("Eligible")
# else:
#     print("Not Eligible")


# 0-19 = Teen
# 20-50 = Adult
# 50-120 = Old
# Else - invalid


# if(age>0 and age<=19):
#     print("Teen")
# elif(age>19 and age<=50):
#     print("Adult")
# elif(age>50 and age<=120):
#     print("Old")
# else:
#     print("Invalid Data")




# - while loop
# init value
# condition
# increment | Decrement

# i = 0

# while(i<5):
#     print("hello", i)
#     i += 1

# print("hey")


# - for loop with range()

# for a in range(10):
#     print(a)

# for a in range(2,10):
#     print(a)

# for a in range(2,10,2):
#     print(a)


# - break

# for a in range(1,11):
#     if(a==5):
#         break

#     print(a)



# - continue

# for a in range(1,11):
#     if(a%2==0):
#         continue
    
#     print(a)



# - pass

a = 15
if (a>10):
    pass  # Handle this case later
else:
    print("Condition is false")  



# - Ternary operator

# value_if_true if condition else value_if_false

result =  "yes" if a>10 else "no"
print(result)



# match-case 
value = 30
match value:
    case 10:
        print("ten")
    case 20:
        print("twenty")
    case "30":
        print("thirty")
    case 40:
        print("fourty")
    case _:
        print("data not avaible")

