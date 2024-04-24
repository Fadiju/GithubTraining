# Exercise 6:
    
# A palindrome is a word, phrase or sequence that is the same forwards and backwards (eg.
# radar, level, 121, 19791)
# Write a program that prints whether a number or string is a palindrome
# Example 1:
# number = 191
# Output:
# This is a palindrome
# Example 2:
# number = 192
# Output:
# This is not a palindrome

# Ansser>>>

while True:
    
    palindrome = input("Enter a String or Number: ").lower()
    if palindrome == (palindrome[::-1]):
        print("this is palindrome")
    else:
        print("the number you enterd is not palaindrome")
    Continue = input("Would you like to check anther (Palaindrome) \nchose yes/no: ").lower()
    if Continue != "yes":
        break