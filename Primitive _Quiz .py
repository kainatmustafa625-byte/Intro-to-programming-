# Ask the user a question
answer = input("What is the capital of France? ")

# Convert the answer to lowercase to ignore capitalization
if answer.lower() == "paris":
    print("Correct!")
else:
    print("Wrong!")
# Dictionary of 10 European countries and their capitals
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Greece": "Athens"
}

# Loop through each country and ask the user
for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower():  # Ignore capitalization
        print("Correct! \n")
    else:
        print(f"Wrong!  The correct answer is {capital}.\n")
