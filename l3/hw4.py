# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами,
# а програма, виходячи з дії, обчислює та друкує результат.
#
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

x = float(input("Введіть число: "))
y = float(input("Введіть число: "))
z = input("Введіть оператор для цих чисел:")
if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '*':
    print(x * y)
elif z == '/':
    if y != 0:
        print(x / y)
    else:
        print("Помилка. Дільник не може дорівнювати 0.")
else:
    print("Помилка. Невідомий оператор.")