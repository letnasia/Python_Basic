# Написати програму, яка переміщає всі нулі у кінець списку.
#
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
#
# Порядок ненульових чисел має зберегтися!

# [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
# [0] -> [0]
# [1, 0, 3, 0, 0, 0, 5] -> [1, 3, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

# lst = [0, 1, 0, 3, 12]
# lst = [0]
# lst = [1, 0, 3, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = []
for el in lst:
    if el != 0:
        result.append(el)
for el in lst:
    if el == 0:
        result.append(el)
print(result)