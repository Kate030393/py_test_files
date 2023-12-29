numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Використання lambda функції для відфільтрування непарних чисел
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Конвертція об'єкту filter у список
even_numbers_list = list(even_numbers)
print(even_numbers_list)
print(numbers)
