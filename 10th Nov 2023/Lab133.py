class A:
    def print(self):
        print("A")


class C:
    def print(self):        #this is a method coz its within the class
        print("C")

class E:
    def print(self):        #this is a method coz its within the class
        print("E")

def B():                    #this is a function coz its outside the class
    print("B")

def D():                    #this is a function coz its outside the class
    print("D")