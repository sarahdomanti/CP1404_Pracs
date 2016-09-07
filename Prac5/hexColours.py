COLOUR_DICT = {"Black": "#000000", "Blue": "#0000ff", "Brown": "#a52a2a",
               "Coral": "#ff7f50", "Dark Green": "#006400", "HotPink": "#ff69b4",
               "Orange": "#ffa500", "Pink": "#ffc0cb", "Plum": "#dda0dd", "Red": "#ff0000"}
colour = input("Enter a colour: ").title()
while colour == "":
    print("Please enter a valid colour")
    colour = input("Enter a colour: ").title()
if colour in COLOUR_DICT:
    print("{} is {} in hexadecimal".format(colour, COLOUR_DICT[colour]))
else:
    print("{} is not in the colour dictionary.".format(colour))
