# Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0,1,1,2,3,5,8,13

a, b = 0, 1  # multiple initialization in single line
while a < 15:
    print(a, end=' ')
    a, b = b, a + b             #here all the latest value of b will be assigned to a and latest values of a+b will be assigned to b

# number = int(input("Enter the number\n"))
# a = 0
# b = 1
# while(a < number):         #infinite loop
#    print(a, end='')
