
# open file

# with open('doc.txt') as f:
#     abc = f.read()
#     print(abc)


# with open('doc.txt') as f:
#     abc = f.readline()
#     print(abc)


# with open('doc.txt') as f:
#     abc = f.readlines()
#     print(abc)

# with open('doc.txt') as f:
#     abc = f.readlines()
#     for i in range(len(abc)):
#         print(abc[i])

    # print(abc)


# list = ["hello","all","there"]
# print(len(list[0]))


# a = "hello"
# print(a[2])

# print(len(a))







########################## write



# with open('doc.txt','r') as f:
#     abc = f.read()
#     print(abc)

# with open('doc.txt','w') as f:
#     f.write("a")

# with open('doc.txt','r') as f:
#     abc = f.read()
#     print(abc)


with open('doc.txt','a') as f:
    abc = f.write("\nb")
    print(abc)

with open('doc.txt','r') as f:
    abc = f.read()
    print(abc)



