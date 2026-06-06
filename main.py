import random
import string


print("\nRANDOM PASSWORD GENERATOR\n")


length = int(input("Enter password length: "))


letters = input("Include letters? (yes/no): ").lower()

numbers = input("Include numbers? (yes/no): ").lower()

symbols = input("Include symbols? (yes/no): ").lower()


characters = ""


if letters == "yes":
    characters += string.ascii_letters

if numbers == "yes":
    characters += string.digits

if symbols == "yes":
    characters += string.punctuation


if characters == "":
    print("Select at least one option")

else:

    password = ""

    for i in range(length):

        password += random.choice(characters)

    print("\nGenerated Password:")

    print(password)