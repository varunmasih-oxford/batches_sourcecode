dt = [
    "aditya",
    1010,
    "ritu",
    2020,
    "mayank",
    3030,
    "aditya pal",
    4040
    ]

# print(dt[1])

stud_list = {
    "aditya": 1010,
    "ritu": 2020,
    "mayank": 3030,
    "aditya pal": 4040
}

# print(stud_list['aditya'])


for i in stud_list:
    # print(i)
    # print(stud_list[i])
    # print(f"my name is {i} my roll no is {stud_list[i]}")
    pass






# stud_details = {
#     "aditya": [1010, "class1", "A+"],
#     "ritu": [2020, "class2", "A+"],
#     "mayank": [ 3030, "class3", "A+"],
#     "aditya pal": [ 4040, "class4", "A+"]
# }

# print(stud_details['aditya'][1])




stud_details = {
    "aditya": {"roll": 1010, "class": "class1", "grade": "A+"},
    "ritu": {"roll": 2020, "class": "class2", "grade": "A+"},
    "mayank": { "roll": 3030, "class": "class3", "grade": "A+"},
    "aditya pal": {"roll": 4040, "class": "class4", "grade": "A+"}
}

print(stud_details)

# print(stud_details['aditya']['grade'])




# Modifying and Adding Items:

print(stud_details['aditya']['grade'])
stud_details['aditya']['grade'] = "A++"


print(stud_details['aditya'])
stud_details['aditya']['marks'] = 500
print(stud_details['aditya'])

# Removing Items:
stud_details['aditya'].pop('marks')
print(stud_details['aditya'])

for i in stud_details["aditya"]:
    print(i)

for i in stud_details["aditya"].values():
    print(i)

for i,o in stud_details["aditya"].items():
    print(i)
    print(o)
