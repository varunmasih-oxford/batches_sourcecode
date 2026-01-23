'''
## What is a Set?
A set is an 
unordered, 
mutable collection that only stores 
unique items.
'''


setOfNums = {10,20,30,10}
# print(type(setOfNums))
print(setOfNums)


states = {'delhi','mumbai','punjab','haryana','delhi','haryana','delhi','haryana'}
print(states)



s = {1, 2}

# Adds a single element.
s.add(3)
print("add:", s)

# removes a single element.
s.remove(2)
# s.remove(5) # error if not found
print("remove:", s)

s.discard(5) # NO error if not found
print("remove:", s)


s.update([5,6])
print("update:", s)


s.pop()
print("POP:", s)

s.clear()
print("remove all:", s)


squares = {x*x for x in range(5)}
print(squares)


evens = {x for x in range(10) if x % 2 == 0}
print(evens)

a = {1, 2}
b = {2, 3}
c = a | b
print('union : ',c)

c = a & b
print('Intersection : ',c)


# a = {1,2,4}
# b = {2,3}
c = a - b
print('Diff : ',c)



c = a ^ b
print('symmDiff : ',c)




squares = {x*x for x in range(10)}
print(squares)


