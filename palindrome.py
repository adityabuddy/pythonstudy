 # Check if a word is a palindrome
word = "madam"  #word to be checked
if word == word[::-1]:  #slicing concept is used here
    print("Palindrome")  #if the word is same when reversed
else:
    print("Not Palindrome")  
