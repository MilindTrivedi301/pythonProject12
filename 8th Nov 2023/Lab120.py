# Parent - Child
# Father -> son
# GF -> F -> S
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:

    def car(self):
        print("Lambo")
    def speak(self):
        print("Animal Speak!")


class Dog(Animal):
    #def speak(self):
        #print("Bow Bow")
    pass


dog = Dog()         #calling funct

dog.car()           #single inheritance of the fuct car

dog.speak()         #single inheritance of the fuct speak


dog = Dog()
dog.speak()