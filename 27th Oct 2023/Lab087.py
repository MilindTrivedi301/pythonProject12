# Set -

# Initial Blank Set
set1 = set()
print(set1)

set2 = set("Milind")        #creates unordered collection
print(set2)

set3 = {1, 2, 3, 4, 5, 5, 4}        #{} used to create a set for int
print(set3)
print(type(set3))

# List of element - in Web Automation
# Can  set to store the value, so that we don't have duplicate!!


set3 = {1, 2, 3, 4, 5, 5, 4}
#set3[1] = 34 # Not possible!, Immutable
print(set3)

set1 = set(["Milind", "For", "Milind"])     #no duplicate value would be printed
print(set1)