import secrets
import string

allCharacters = string.ascii_letters + string.digits + string.punctuation
enterPassword = True

while enterPassword:
    try:
        length = int(input("Length of Password: "))
        if length > 0:
            print(''.join(secrets.choice(allCharacters) for i in range(length)))
            nextPassword = input("Next password? Y / n ")[:1].lower()
            if nextPassword != "y":
                enterPassword = False

        else:
            print("Value has to be positive")

    except ValueError:
        print("Enter digits!")
