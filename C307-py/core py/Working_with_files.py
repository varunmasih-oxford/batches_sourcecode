# with open('abc.txt') as f:
#     data = f.read()
#     print(data)


# with open('abc.txt') as f:
#     data = f.read(5)
#     print(data)

# with open('abc.txt','r') as f:
#     data = f.read(5)
#     print(data)

# with open('abc.txt','r') as f:
#     data = f.readline()
#     print(data)

# with open('abc.txt','r') as f:
#     data = f.readlines()
#     for line in data:
#         print(line)
        


# with open('abc.txt','w') as f:
#     f.write("This is a new line")


# with open('abc.txt','r') as f:
#     print(f.read())



with open('abc.txt','a') as f:
    f.write("\nHello World")


with open('abc.txt','r') as f:
    print(f.read())


