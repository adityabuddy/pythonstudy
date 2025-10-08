#using input function to take user input
n = int(input("Enter a number: "))  #taking input from user and converting it to integer
fact = 1                              #fact means factorial
for i in range(1, n+1):
    fact *= i  
print("Factorial:", fact)  