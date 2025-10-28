# Function to determine if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the function and get the result
    result = check_even_odd(num)
    
    # Print the returned message
    print(result)

# Entry point of the program
if __name__ == "__main__":
    main()
