#file IO in python

#present in the same directory

#append
file2 = open('secret.txt', 'a')             #a is append here
file2.write("Yes Yes, append/add new data")
file2.close()

#wirte
file2 = open('secret23.txt', 'w')             #a is append here  #create a new file with name secret23.txt
file2.write("Yes Yes, override")
file2.close()

#read
file = open('secret.txt','r')               #r is read here
print(file.read())
file.close()

#--------------------------------------------------------------------------------------

#Path is required when present in the differet directory

#append
file2 = open('../8th Nov 2023/secret.txt', 'a')             #a is append here
file2.write("Yes Yes")
file2.close()

#read
file = open('../8th Nov 2023/secret.txt','r')               #r is read here
print(file.read())
file.close()


#--------------------------------------------------------------------------------------
try:
    file= open('milind213.txt','r')
    print(file.read())
except FileNotFoundError as trivedi:
    print("File not found",trivedi)
finally:
    if file:
        file.close()