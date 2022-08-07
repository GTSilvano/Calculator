from secrets import choice


print("1 Add")
print("2 Substract")
print("3 Multiply")
print("4 Divide")

choice = input("Choose your operation")

num1 = float(input("First Number"))
num2 = float(input("Second Number"))

if choice == "1":
    print(num1, "+", num2, "=", (num1+num2))
else:
    print("Error you dumb fuck")