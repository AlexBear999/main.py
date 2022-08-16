element = input('Введите элементы первого списка через запятую')
numbers = element.split(',')
element = input('Введите элементы второго списка через запятую')
numbers_two = element.split(',')
print(numbers)
print(numbers_two)

for number in numbers[:]:
    if number in numbers_two:
       numbers.remove(number)

print(numbers)