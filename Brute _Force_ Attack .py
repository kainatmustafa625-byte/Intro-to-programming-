# limit attempts to 5
correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter the password: ")
    attempts += 1

    if user_input == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. You have {remaining} attempt(s) left.")
        else:
            print("Wrong password. No attempts left.")

else:
    # This else runs only if the while loop completes without break
    print("Maximum attempts reached. Authorities have been alerted.")
