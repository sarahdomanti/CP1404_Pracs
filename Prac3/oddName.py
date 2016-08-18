"""Sarah"""
def main():
    name = get_name()
    FREQUENCY = int(input("What frequency of letters would you like to display? "))
    print_name_chars(name, FREQUENCY)


def print_name_chars(name, frequency):
    for i in range(1, len(name), frequency):
        print(name[i])


def get_name():
    name = input("Enter your name: ")
    while name == False:
        print("Please enter a valid name.")
    return name


main()