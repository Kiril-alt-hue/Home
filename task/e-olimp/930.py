# Вхідні дані
phone_number = input().strip()

# Залишаємо тільки цифри у введеному рядку
digits_in_phone = set(filter(str.isdigit, phone_number))

# Множина всіх можливих цифр
all_digits = set('0123456789')

# Визначаємо відсутні цифри
missing_digits = sorted(all_digits - digits_in_phone)

# Вивід результату
print(len(missing_digits))
print(' '.join(missing_digits))
