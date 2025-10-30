# Exercise: Store and print name, hometown, and age using a dictionary
# Advanced version with user input

name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Age must be a number.")
    age = None  # Assign None if input is not a valid integer

person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 4: Print the values on separate lines using a single print() statement
print(f"\nName: {person['name']}\nHometown: {person['hometown']}\nAge: {person['age']}")
