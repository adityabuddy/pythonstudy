# Simple calculator using if-else

print("Select operation:")     #displaying the options to the user
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")   #choice is a variable which stores the user input

num1 = float(input("Enter first number: "))   #float is used to take decimal values as input
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':                          #elif is used to check multiple conditions
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
