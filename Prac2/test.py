
def get_number(lower, upper):
    number = int(input("Enter a number between {} and {} : ".format(str(lower), str(upper))))
    while number < lower or number > upper:
        print("Please enter a valid number!")
        number = int(input("Enter a number between {} and {} : ".format(str(lower), str(upper))))
    return number
number = get_number(10, 50)
