
str_number = input('Введите числа через запятую')
numbers = str_number.split(',')
result = []
for number in numbers:
   if numbers.count(number) == 1:
        result.append(number)
print(result)