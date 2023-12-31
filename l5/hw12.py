# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

text = str(input("Enter a string: "))
res = text.title()
for l in string.punctuation:
    res = res.replace(l, '')
if ' ' in res:
    res = res.replace(' ', '')

res = '#' + res[:140]
print(res)

