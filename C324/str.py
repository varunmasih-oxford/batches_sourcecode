# txt = 'this is single quote string'
# txt_dbl = "this is duble quote string"

# print(txt)
# print(txt_dbl)


# txt_dbl = "He has bought a 'new' Iphone"
# txt_dbl = 'He has bought a "new" Iphone'
# print(txt_dbl)

# txt_dbl = "He has bought a new's Iphone"
# txt_dbl = 'He has bought a new\'s Iphone'
# print(txt_dbl)



# txt_dbl = 'He has bought a new Iphone'
# print(txt_dbl)

# triple quote string or multi line string
txt_triple = '''
hey 
this is 
Triple quote 
'''
# print(txt_triple)

"single line string"
# single line string

'''
multi 
line 
string
'''


txt_dbl = 'He has bought a new Iphone'

print(len(txt_dbl))

print(txt_dbl[0])
print(txt_dbl[-1])
print(txt_dbl[5])

# slicing string
# print(txt_dbl[START:END])

print(txt_dbl[7:])
print(txt_dbl[:7])

status = "loggedout"
user_name = "anvit"

if(status=="loggedin"):
    print(user_name , txt_dbl[3:])
else:
    print(txt_dbl)
