val = None
name = None

# None is also not a default value for the variables that has other None Type variables.
# None is not the same as False.
# None is not an empty string.
# None is not 0.
# None will not any memory.

a = None
b = None

#val = None + 2
# unsupported operand type(s) for +: 'NoneType' and 'int'
print(val)
name = "milind"
print(name)
print (type(val)) #<class 'NoneType'>
print(id(val))

# print(len(val)) # print(len(val)) this is not possible