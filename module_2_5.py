numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Создаем пустые списки
primes = []
not_primes = []
for num in numbers: # Перебираем список numbers
    if num == 1:
        continue  # Пропускаем число 1, так как оно не простое и не составное
    is_prime = True # Изначально предполагаем, что число простое
    for i in range(2, int(num**0.5) + 1): # Проверяем, есть ли у числа делители (кроме 1 и самого себя)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num) # Добавляем число в соответствующий список
print("Простые числа:", primes)
print("Непростые числа:", not_primes) # Выводим списки