
# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Part 1: Basic search for "Sam"
search_name = "Sam"
if search_name in names:
    print(f"Basic Search: {search_name} was found in the list!")
else:
    print(f"Basic Search: {search_name} was not found in the list.")

print("-" * 40)  # separator

# Part 2: User input search
 
user_search = input("Optional Search: Enter the name to search: ")

# Check if the user input exists in the list
if user_search in names:
    print(f"Optional Search: {user_search} was found in the list!")
else:
    print(f"Optional Search: {user_search} was not found in the list.")
