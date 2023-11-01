#lambda function is used to reduce the lines of the code or useful when functions requires another function as its argument

original_str = "Milind"
reverse_str = lambda original_str : original_str[::-1]


if reverse_str("Milind") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")

#-----------------------------------------------------------------------------

add = lambda x,y : x+y

print(add(3,4))

#------------------------------------------------------------------------------

is_palindrome = lambda original_str : original_str[::-1]

if reverse_str("Milnd") == "Milind":
    print("Palindrome")
else:
    print("Not palindrome")
    original_str = "Milind"

#-----------------------------------------------------------------------------

reverse_str = lambda original_str : original_str[::-1]

if reverse_str("Milind") == original_str:
    print("Palindrome")
else:
    print("Not a Palindrome")




add = lambda x,y : x+y

print(add(3,4))

