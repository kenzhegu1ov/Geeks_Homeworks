data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'c', 'e', 3, 'e', 1, 'G')

letters = []
numbers = []

for i in data_tuple:
   letters.append(i) if type(i) == str else numbers.append(i)

numbers.remove(6.13)
numbers.insert(2, 2)
letters.append(numbers.pop(0))
numbers = [int(i) for i in numbers[::-1]]
numbers = [int(i) ** 2 for i in numbers]

letters = [str(i) for i in letters[::-1]]
letters[7] = 'c'

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
