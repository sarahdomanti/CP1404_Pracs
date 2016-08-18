lower = 10
upper = 100
print("Enter a number between {} and {} : ".format(str(lower), str(upper)))
for i in range(1, 10):
    ASCII = int(input("> "))
    if ASCII < lower or ASCII > upper:
        print("Invalid number.")
    else:
        print("{:<5} {:>5}".format(ASCII, chr(ASCII)))
