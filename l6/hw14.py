# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
#
# Користувач вводить число з клавіатури.
#
# Приклади:
#
# 999 -> 2 == Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
# Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2

# 1000 -> 0
# 423 -> 8
# 1 -> 1

digit = int(input('Enter an integer: '))

while digit > 10:
    dig_str = str(digit)
    digit = 1
    for val in dig_str:
        val = int(val)
        digit *= val
print(digit)