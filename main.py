import string
import random

length = int(input("Enter password length: "))
print('''Choose character set for password from these :
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')
charList = ""

while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):
        charList += string.ascii_letters
    elif (choice == 2):
        charList += string.digits
    elif (choice == 3):
        charList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):

    randomchar = random.choice(charList)

    password.append(randomchar)

print("The random password is " + "".join(password))
