# Моржовый оператор сразу позволяет выполнять присваивание внутри операций. Взгляните на код ниже

print(see_walrus := 'Look at my walrus, my walrus is amazing')

print(see_walrus[:11] + 'horse')
#

words = input('Введите слова через пробел: ').split()

if (count := len(words)) > 3:
    print (f"Ого сколько слов вы знаете, аж {count}")
else:
    print (f"Словарный запас пополнить надо, {count} это маловато")

#
if number := int(input('Введите число: ')) == 100:
  print('Соточка')
else:
  print('Не Соточка')

#
if (num := int(input())) <= 10000:
    print(f"Сумма {num} не превышает лимит, проходите")
else:
    print(f"Ого! {num}! Куда вам столько? Мы заберем {num - 10000}")

#
if 'walrus' in (phrase := input()):
    print("Нашли моржа")
else:
    print("Никаких моржей тут нет")

#
if (digit := input()).isdigit():
    print("Можно преобразовать")
else:
    print("Нельзя преобразовать")

#
nums = input().strip().replace(',', '.')  # заменяем для проверки   # убираем пробелы слева и справа

# nums = nums.replace(',', '.')  # заменяем для проверки

try:
    float(nums)
    print("Можно преобразовать")

except ValueError:
    print("Нельзя преобразовать")