# Цикл while

# Простейший while
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5: break

answer = None

while answer != 'Volvo':
    answer = input ('Какая лучшая марка автомобиля?')
print('Вы абсолютно правы!')


while i < 10:
    print(i)
    i = i + 1
    if i == 9: break
    if 1 < 3: continue