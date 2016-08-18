name = input("What is your name? ")
nameFile = open(str(name) + '.txt', mode='w')
nameFile.write("Your name is {}.".format(str(name)))
nameFile.close()

numbersFile = open('numbers.txt', mode='r')
num1 = int(numbersFile.readline())
num2 = int(numbersFile.readline())
result = num1 + num2
print(result)
numbersFile.close()
