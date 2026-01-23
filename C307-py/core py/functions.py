# - Python functions – define and reuse.



name_stud = "aditya"

# function 


# def stud_marks():

#     stud_name = "aditya"
#     marks = 99

#     if marks>=70 and marks<=100:
#         print(stud_name,"got FD")
#     elif marks>=50 and marks<=69:
#         print(stud_name,"got SD")
#     elif marks>=1 and marks<=49:
#         print(stud_name,"got TD")
#     else:
#         print("invailid")


# stud_marks() #calling
# stud_marks()
# stud_marks()
# stud_marks()





# function with params

# def stud_marks(stud_name,marks):

#     if marks>=70 and marks<=100:
#         print(stud_name,"got FD")
#     elif marks>=50 and marks<=69:
#         print(stud_name,"got SD")
#     elif marks>=1 and marks<=49:
#         print(stud_name,"got TD")
#     else:
#         print("invailid")


# stud_marks("aditya",85)
# stud_marks("ritu",95)
# stud_marks("mayank",88)
# stud_marks("aditya",86)





# def sum():
#     x = 10
#     y = 20
#     z = x+y
#     print(z)



# sum()

def getpercentage(marks,total):

    percentage = marks/total*100
    print(percentage)



# positional argument
# getpercentage(50,60)




# keyword argument
# getpercentage(total = 150, marks = 60)




# def sum(x,y):
#     z = x+y
#     return z
#     # print(z)


# # print(z) # z is undefined bcz it has been defined inside a function

# print(sum(10,20))
# print(sum(10,120))



def sum(stud,marks,total):
    per = marks/total*100

    return [stud,per]


details = sum("aditya",10,20)

print(details[0])
print(details[1])







# List

# name = "ritu"
# marks = 40
# print(name,marks)


# stud_1 = ["ritu",40]

# print(stud_1[0])
# print(stud_1[1])

for i in range(1,11):
    print("3X1=3")