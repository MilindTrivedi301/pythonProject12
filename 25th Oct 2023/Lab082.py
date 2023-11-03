# Map and Filter in the List


# Map Functions ( where we will go from one item and apply a functions)
numbers = [1, 2, 3, 4, 5]
# sq_numbers = [1, 4, 9, 16, 25]
sq = lambda x: x * x
sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)


def ThreeTimes(a):
    return a ** 3

def triple(a):
    return a * 3


# Map Function
sq_numbers1 = list(map(ThreeTimes, numbers))
sq_numbers2 = list(map(triple, numbers))
sq_numbers3 = list(map(lambda x: x * 3, numbers))
sq_numbers4 = list(map(lambda x: x * x, numbers))

print(sq_numbers1)
print(sq_numbers2)
print(sq_numbers3)
print(sq_numbers4)