#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.

def classify_triangle(a, b, c):
    if a == b and b == c:
        return "Equilateral triangle"
    elif a == b or a == c or b == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Classify the triangle and print the result
classification = classify_triangle(a, b, c)
print(f"The triangle with side lengths {a}, {b}, and {c} is a {classification}.")


#Fibonacci series = number + previous numbers 0+1=1 1+1=2 1+2=3 2+3=5 3+5=8 5+8=13