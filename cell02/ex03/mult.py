first = float(input("Enter the first number: \n"))
second = float(input("Enter the second number: \n"))

result = first * second
print(f"{first} x {second} = {int(result)}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")


