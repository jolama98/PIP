def start_pip():
    print("PIP is on line")


start_pip()
name = input("Please enter your name: ")


def greet_user(name):
    print(f"Hello, {name}! I am PIP.")


greet_user(name)

age = int(input("Please enter your age: "))

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print(f"You are {age} years old.")
