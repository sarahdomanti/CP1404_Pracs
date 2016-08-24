LOWER = 33
UPPER = 127


def main():
    letter = input("Enter a character: ")
    ASCII = ord(letter)
    print("The ASCII code for {} is {} ".format(letter, ASCII))
    number = get_number(LOWER, UPPER)
    character = chr(number)
    print("The character for {} is {} ".format(number, character))

    for i in range(LOWER, UPPER + 1, 1):
        print("{:<5} {:>5}".format(i, chr(i)))


def get_number(lower, upper):
    number = int(input("Enter a number between {} and {} : ".format(str(lower), str(upper))))
    while number < lower or number > upper:
        print("Please enter a valid number!")
        number = int(input("Enter a number between {} and {} : ".format(str(lower), str(upper))))
    return number


main()
