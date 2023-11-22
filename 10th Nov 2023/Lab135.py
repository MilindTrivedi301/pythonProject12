
# Exception
# An exception is an event that occurs during the execution of a program
# that disrupts the normal flow of instructions.

# divide by zero - ZeroDivisionError
# string or nothing - value error (invalid literal for int() with base 10: 'Milind')
# none - value error(invalid literal for int() with base 10: 'None'),
# float - value error (invalid literal for int() with base 10: '43.23')
# complex 1+8j - value error (invalid literal for int() with base 10: '1+8j')
# AB123 - value error (invalid literal for int() with base 10: 'AB123')
# 100000000000000000000000 0 veru big value of int
# True - value error (invalid literal for int() with base 10: 'True')
# tuple() or list[] - value error (invalid literal for int() with base 10: '[12345]')
# special char ~!@#$%^ - value error (invalid literal for int() with base 10: '@#$%^&')

x = int(input("Enter a number:"))
result = 10/x
print(result)

#-----------------------------------------------


a = 10
b = 0

try:
    c = a/b
except Exception as error:
    print(error)

try:
    c=a/b
except ZeroDivisionError as error:
    print(error)