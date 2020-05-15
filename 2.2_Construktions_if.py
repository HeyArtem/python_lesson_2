# 15.05.20 Операторы условия if elif

brend = 'Volvo'      # Бренд
engine_volume = 1.5  # Обьем двигателя
horsepower = 152     # мощность двигателя
sunroof = True         # есть люк

# Проверка условия if
#
# if horsepower < 80:
#    print('No tax')

# Проверка условия if/else
# if horsepower < 80:
#     print('No tax')
#     print('No tax')
#     print('No tax')
# else:
#     print('Tax')

# Проверка условия if/elif/elif/else
tax = 0
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
print(tax)

# if для присваивания
cool_car = 0
cool_car = 1 if sunroof ==1 else 0
print(cool_car)