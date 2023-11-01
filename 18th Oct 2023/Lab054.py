# Continue

for num in range(1, 10):    #num is variable
    if num % 2 == 0:
        print("Found even Number", num)
        print(f"Found even Number -> {num}")        #f means value of num variable will be replased first time # f is used for formatting
        continue
    print("Odd number Found ->", num)