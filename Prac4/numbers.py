numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
"""print(numbers[0], numbers[-1], numbers[3], numbers[:-1], numbers[3:4])
#3, 2, 1, [3,1,4,1,5,9], [1,5]#
print(5 in numbers) #true#
print(7 in numbers) #false#
print('3' in numbers) #false or error#
print(numbers + [6, 5, 3]) #[3, 1, 4, 5, 9, 2, 6, 5, 3]"""

numbers[0] = 'ten'
numbers[-1] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)
