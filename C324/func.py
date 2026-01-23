# def xyz():
#     data = input("type anything : ")
#     print(data)


# xyz()
# xyz()
# xyz()

# fn with params
def xyz(first_name,last_name):  
    # print("hello", first_name, last_name)
    print(f"hello {first_name} {last_name}")


xyz("harshkirath","kaur")
xyz("shubh","budhiraja")



def per(marks,totals):
    res = marks/totals*100
    return res


abc = per(500,2000)
print(abc)

# per(500.1000) # positional argument
# per(totals=1000,marks=500)# named argument


# return statment



