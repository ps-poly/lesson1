numbers = [3,5,7,9,10.5]
print(numbers)
numbers.append('Python')
print(numbers)
print(len(numbers))

print(numbers[0])
print(numbers[-1])
print(numbers[2:5])
del numbers[5]
print(numbers)
print(len(numbers))
numbers.remove('10.5')
print(len(numbers))