print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favourite number: "))

print("\nThank you! Your information has been collected.\n")

print(f"Name: {name}", type(name), id(name))
print(f"Age: {age}", type(age), id(age))
print(f"Height: {height}", type(height), id(height))
print(f"Favourite Number: {fav_num}", type(fav_num), id(fav_num))

birth_year = 2026 - age
print(f"\nYour Birth Year is approximately: {birth_year}")