# conditions

# if True:
#     print("yes")
#     print("No")



# if False:
#     print("yes")
#     print("No")

# age = input("Tpe any value : ")

# if int(age)>18:
#     print("yes")
# else:
#     print("No")
  


# bool()
# int()
# str()
# float()

# age 1-19 Teen 
# age 20-45 Young 
# age 46-120 Old 


# age = input("Type any value : ")
# age = int(age)
# if age>0 and age<20:
#     print("Teen")
# elif age>19 and age<=45:
#     print("Young")
# elif age>45 and age<=120:
#     print("old")
# else:
#     print("Pls Five Right Input")
  

# Attendance = int(input("Attendance : "))
# Marks = int(input("Marks : "))

# if Marks>75 or Attendance > 90:
#     print("Scholorship")
# else:
#     print("No Scholorship")
    
    
# if Marks>75 and Attendance > 90:
#     print("Scholorship")
# else:
#     print("No Scholorship")
    
    
# yob = int(input("Year : "))

# if yob >= 1900 and yob <= 1910:
#     print("10s") 
# elif yob >= 1911 and yob <= 1920:
#     print("20s") 
# elif yob >= 1921 and yob <= 1930:
#     print("30s") 
# else:
#     print("pls give right input")



# day = int(input("day : "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid day")

day = input("day : ")

match day:
    case "bittu":
        print("Monday")
    case "aakash":
        print("Tuesday")
    case "dhruv":
        print("Wednesday")
    case _:
        print("Invalid day")
