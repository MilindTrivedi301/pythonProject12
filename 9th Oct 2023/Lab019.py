# String
# Bunch of Char
name = "Milind"
name = "Trivedi"          #name overwritten

# String Functions
# Python String Immutable in Nature - They can't changed!, Once Created
# name[0] = "h" # TypeError: 'str' object does not support item assignment

# capitalize()
# Returns a copy of the string with its first character capitalized.
result = name.capitalize()  #create a new string
print(result)
print(name)

print(id(name))
print(id(result))  #retursn the idendity of the stings

# Upper Case
result2 = name.upper()
print(result2)

# Lower
result3 = name.lower()
print(result3)
print(id(result3))  # Identity - Address Ref.

# Swapcase()
# Returns a copy of the string with uppercase characters converted to lowercase
# and vice versa.

name = "AmItTrIvEdI"
print(name.swapcase())

# Title
# Returns a titlecased version of the string,
# where words start with an uppercase character and
# the remaining characters are lowercase.

name = "hello world"
print(name.title())

t1 = "trivedi ji"   # t1 is ref or variable name ,  "trivedi ji" which is stored in memory
t2 = "Amit ji"
print(t1.capitalize())
print(t2.upper())

name = "trivedi"
print(len(name))

# Replace
text = "hello world"
result_rep = text.replace("world","Python")
print(result_rep)

#index and len
name  = "Amit"
# len -> 1
print(len(name))
# index - 0 to len-1
# a - 0, m - 1, i - 2, t - 3


#find()
#Returns the lowest index of a substring in the string.
# Returns -1 if the substring is not found.

text = "hello world"
index = text.find("world")
print(index)



#count() - count the char -
count = text.count("l")
print(count)


name  = "p d"             #length is total number of character
print(len(name))          #count is total number of character found


name   = "trivedi"
print(name)
del name
print(name)
