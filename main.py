def start_pip():
    print("PIP is on line")


def get_name():
    name = input("Please enter your name: ")
    return name


def get_age():
    age = int(input("Please enter your age: "))
    return age


def check_age(age):
    if age < 18:
        print("Come here kid, I got some candy.")
    else:
        print(f"{age} fuck you are old.")


start_pip()
name = get_name()
print(name)
age = get_age()
check_age(age)
