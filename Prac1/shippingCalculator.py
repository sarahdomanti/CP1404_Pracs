numberItems = int(input("Number of items: "))
totalCost = 0
while numberItems < 0:
    print("Invalid number of items.")
    numberItems = int(input("Number of items: "))

for i in range(numberItems):
    cost = float(input("Price of item: "))
    totalCost += cost

if totalCost > 100:
    totalCost += 0.1 * totalCost

print("Total price for ", str(numberItems), " items is $", str(totalCost), sep="")
