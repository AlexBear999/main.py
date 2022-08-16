count = int(input('Введите количество элементов'))
result = []
for i in range(count):
    number = int(input('Введите число'))
    result.append(number)
result.sort()
print(result)