
import random
import string

def generate_password():
    print("Password Generator")

    # Prompt user for desired password length
    try:
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Please enter a positive number.")
            return

        # Define possible characters for the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the password length.")

# Run the password generator
generate_password()
