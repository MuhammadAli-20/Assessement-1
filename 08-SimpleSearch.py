# Exercise 8

user_input = input("Enter the name you want to search: ")
names = ("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")

if user_input in names: #Using an "in" operator to search the names in the list.
    print(f"You searched {user_input}.") 
else:
    print(f"{user_input} is not in the list.")

