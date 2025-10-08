  #factorial of a number 

n = 5                       #number whose factorial is to be found
fact = 1                  #initializing fact variable to 1
for i in range(1, n+1):    #n+1 is used as range function excludes the last number
    fact *= i              # i stands for 1,2,3,4,5
print("Factorial:", fact)  #printing the factorial value


#using input function to take user input
#n = int(input("Enter a number: "))  #taking input from user and converting it to integer
#fact = 1   
#for i in range(1, n+1):
#    fact *= i  
#print("Factorial:", fact)  
