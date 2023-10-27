# if else
# age > 18 ->  watch a movie
# age < 18 -> not allowd to watch movie

# Ternary Operator

# result_if_true if condition else result if_false
#

A = 90-100
B = 80-89
C = 70-79
D = 60-69
F = 0-59

age = input("Enter your age\n")
age = int(age)
result  = "B" if age > 80 and age <= 89 else "A"
print(result)
