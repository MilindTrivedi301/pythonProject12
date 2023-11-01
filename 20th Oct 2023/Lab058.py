# Match         #python is case sesitive lang
# Similar to Switch in Java

number = int(input("Enter a numer\n"))

match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case _: #Nothing is mathcing, I will run # _ is default 
        print("No idea")