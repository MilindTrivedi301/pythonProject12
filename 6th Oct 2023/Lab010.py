# string - bunch of characters
c='A'
print(c)

name = "Milind"
print(name)

new_line= "This is the 'code'"
print(new_line)

#Code to take input as aa string

user_input = input("Enter your name\n")
print("Your name is",user_input,sep="->", end="\n")

#code to create a calculator
#take input fron users num1 and num2

num1= input("Enter your number 1 \n")
num1= int(num1)  #change the input type from sting to integar
num2= input("Enter your number 2 \n")
num2= int(num2)
print(num1, num2)
print(num1+num2) #print the output as a string
print(num1-num2)
print(num1*num2)
print(num1/num2) #div -> (div - float -12.34)

print(type(num1)) #print the type of the the input variable
print(type(num2))

sum = int(num1)+int(num2) #adding two int
print("The sum is:", sum)

#Note: Intergar and float value takes 24bytes data to store in python