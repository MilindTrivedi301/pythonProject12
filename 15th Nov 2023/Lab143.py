# Collection -

# list, dic, tuple, set, OrderedDict - Data Type

regular = (1, 2, 3)         #regular tuple-unmutable/unchanged
# regular[0] = 20 # They are not mutable

print(regular[0])

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])



person = Person(name="Milind", age=24, gender="M")

print("Name", person.name)
print("Age", person.age)
print("Gender", person.gender)


class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name}")


<<<<<<< HEAD
person2 = Person2("milind", 23, "M")
=======
person2 = Person2("Milind", 23, "M")
>>>>>>> e4cab9c4f0ceb2872787ae88c9579623d6c23dd1
person2.print_details()