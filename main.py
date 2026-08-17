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


def brain_loop():
    message = ""
    while message != "quit":
        message = input("Say something to Pip: ")

        if message == "quit":
            break

        print(message)


def check_is_online(is_online):
    if is_online:
        print("Pip is awake.")
    else:
        print("Pip is sleeping.")


def main():
    is_online = True
    check_is_online(is_online)
    start_pip()
    name = get_name()
    print(name)
    age = get_age()
    check_age(age)
    brain_loop()


# for i in range(5, 11):
#     print(i)
main()
