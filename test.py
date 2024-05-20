string = '25,000-29,999'

# Разделяем строку по дефису '-' и преобразуем каждую часть в числа
start, end = map(int, string.split('-'))

# Вычисляем среднее значение
average_value = (start + end) / 2

print("Среднее значение:", average_value)
