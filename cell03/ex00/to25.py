number = int(input("Enter a number less than 25\n"))

if number > 25:
    print("Error")
else:
    current = number
    while current <= 25:
        print(f"Inside the loop, my variable is {current}")
        current += 1


