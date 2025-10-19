import random
import string

def password_generator (length, complexity):
    if complexity =="easy":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Please Select Appropriate Complexity For Your Password!")

    password = "".join(random.choice(characters) for i in range (length) )
    return password

print("PASSWORD GENERATOR")
length = int(input("\nEnter Desired Password Length: "))
print("Select Complexity Level For Your Password: ")
print("1. Easy Password (has only lowercase letters)")
print("2. Medium Password (has letters + numbers)")
print("3. Strong Password (has letters + numbers + symbols)")
choice = input("\nEnter Your Choice (1 / 2 / 3 ): ")

if choice == "1":
    complexity = "easy"
elif choice == "2":
    complexity = "medium"
elif choice == "3":
    complexity = "strong"
else:
    print("Error: Select choice from (1 / 2 / 3) only. ")

password_generated = password_generator(length , complexity)
print("\nGenerated Password: ", password_generated)
