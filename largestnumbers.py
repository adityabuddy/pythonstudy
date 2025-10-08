## Find the largest numbers..

a, b, c = 10, 25, 15
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:  #elif is used beacause if the first if condition is false then only it will check this condition
    print("Largest:", b)
else:                       #else is used because if both the above conditions are false then only it will execute this block
    print("Largest:", c)



      #using max function
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#c = int(input("Enter third number: "))
#largest = max(a, b, c)                  # max function returns the largest of the input values
#print("The largest number is:", largest)


           # using list
#numbers = [10, 25, 7, 89, 56]
#print("List:", numbers)       #list is a collection which is ordered and changeable. Allows duplicate members.
#largest = max(numbers)
#print("The largest number in the list is:", largest)
