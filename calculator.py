from secrets import choice

while True:

    print("1 Add")
    print("2 Substract")
    print("3 Multiply")
    print("4 Divide")
    print("Type Quit to Exit")

    choice = input("Choose your operation ")
    if choice == "Quit":
        break

    num1 = float(input("First Number "))
    num2 = float(input("Second Number "))

    if choice == "1":
        print(num1, "+", num2, "=", (num1+num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1-num2))
    elif choice == "3":
        print(num1, "*", num2, "=", (num1*num2))
    elif choice == "4":
        if num2 == 0.0:
            print("You divided by zero you idiot sandwich!")
        print(num1, "/", num2, "=", (num1/num2))
    else:
        print("Select a proper operation Kemosabe!")

    def main():
        
        if __name__ == '__main__':
            main()

