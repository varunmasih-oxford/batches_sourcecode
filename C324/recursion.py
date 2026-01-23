user_input = int(input("any num : "))

def sum_all(user_input):
    res = 0
    if user_input > 0:
        res = user_input + sum_all(user_input-1)

    return res




a = sum_all(user_input)
print(a)

