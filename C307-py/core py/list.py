stud_name = "aditya"
stud_age = 15
stud_roll = 1010

stud_name = "aditya kumar"

print("===>" , stud_name)
print(stud_age)
print(stud_roll)


stud_detail = ['aditya',15,1010]

# print(stud_detail)
# print(stud_detail[0])
# print(stud_detail[1])
stud_detail[0] = 'aditya kumar'
print(stud_detail)


stud_detail.append('new')
print(stud_detail)

list2 = [9876543210,"class1"]

stud_detail.extend(list2)
print(stud_detail)


stud_detail.insert(3,"inserted")
print(stud_detail)


stud_detail.append(153)
stud_detail.append(153)
stud_detail.remove(153)
stud_detail.remove(153)


stud_detail.pop(1)

# stud_detail.clear()

cnt = stud_detail.count("class1")
print(cnt)

lst = [1,3,2]
lst.reverse()
lst.sort()

lst = ['a','c','g','b']
lst.sort()
print(lst)


lst.reverse()
print(lst)








lst = ['a','c','g','b']
lst_cpy = lst.copy()
print(lst_cpy)



lst = [
    ["01","aditya"],
    ["02","another"],
    ["03","anki"],
    ["04","ritu"]
    ]

print("###########")
print(lst[3][1])

# make a fun to calculate GST of an amout
# recieved_amount = 1000
# gst_rate = 18
# print - 
# amount
# gst_rate
# total amount


# - Tuple – immutable sequences.

# lst = [1,2,3,4,5]
# print(type(lst))
# lst[0] = 10 # value updated
# print(lst)

# tpl = (1,2,3,4,5)
# print(type(tpl))
# tpl[0] = 10 # cannot update value in tuple
# print(tpl)


# creating tuple
#1st way
tpl = tuple([1,2,3])

#2nd way
tpl = (1,2,3)
print(tpl)


# -Without parentheses (Python allows this) - t = 1, 2, 3

tpl = 1,2,3,4,5
print(type(tpl))


# list sorting
#1way - sort() method
lst = [5,3,1,4,2]
lst.sort()
lst.sort(reverse=True)
print(lst)


# - Sort a list (with `sorted()`)

#2way - sorted() function
lst = [5,3,1,4,2]
new_lst = sorted(lst, reverse=True)
print(new_lst)

# - Slice a list

lst = [1,2,3,4,5,6,7,8,9,10]
print(lst[1:5])
print(lst[1:])
print(lst[:5])
print(lst[2:5:2])
print(lst[::2])


# - Unpack a list
lst = [1,2,3]
a = lst[0]
b = lst[1]
c = lst[2]
print(a,b,c)

a,b,c = lst
print(a,b,c)

long_list = [1,2,3,4,5,6,7,8,9]
*a,b,c = long_list
print(a)
print(b)
print(c)


def print_non_vowels(name):
    vowels = "aeiouAEIOU"
    for ch in name:
        if ch not in vowels:
            print(ch)
print_non_vowels("aditya kumar")


            










