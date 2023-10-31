# Problem to find the MAX three

a = 10
b = 20
c = 13

output = None

if a > b and a > c:
    output = a
elif b > a and b > c:
    output = b
else:
    output = c

print(output)

#----------------------

a=78
b=5
c=6

if a > b and a >c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


#--------------------------


a, b = 10, 20

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")