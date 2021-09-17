#! python3
"""
Ask the user for their name and their email address.
You will need to use the .strip() method for this assignment. Be aware of your 
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.
"""
x = input("What is your name?").strip()
y = input("What is your email adress?")
print("Your name is " + x + "," + " Your email address is " + y + ".")


