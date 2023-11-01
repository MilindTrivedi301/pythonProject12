#using slice method
original_str = "NAMAN"

def is_palindrome(original_str):
    rev_str = original_str[::-1]    #reverse will be printed... called as string slicing (::-1) [start:stop:step]
    print(rev_str)
    if original_str == rev_str:
        print("Palindrome")
    else:
        print("It is not")


is_palindrome(original_str)



l =[1,2,3,4,5,6,7,8,9]
#print(l[0:8:1])
print(l[::-1]) #reversing the sting



def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)