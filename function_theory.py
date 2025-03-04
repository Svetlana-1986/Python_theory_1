# Значение по умолчанию для аргумента
#
# Параметры функции делятся на обязательные и необязательные.
# Для создания необязательных параметров необходимо использовать значения по умолчанию.
# Параметры со значением по умолчанию — это параметры, которые могут принимать значение по умолчанию во время вызова
# функции. Если мы не передадим функции какой-либо аргумент, то будет использован аргумент по умолчанию.
#
# Создаются параметры по умолчанию по следующему шаблону
#
# def имя_функции(параметр1, параметр2=значение2, параметр3=значение3, ...):
# В заголовке функции вы указываете с помощью оператора присваивания (=) значения по умолчанию
# (в этом шаблоне они обозначаются значение2 и  значение3,…) для тех параметров, которым вы хотите задать дефолтное значение.
#
# Например, функция greet, определенная ниже, имеет обязательный параметр name и необязательный msg,
# имеющий значение по умолчанию "Привет!"

def greet(name, msg="Привет!"):
    print(f"{name}, {msg}")


greet("Брюс")
greet("Степан", "Как дела?")
greet("Евгений", "Отлично!")

# Когда вы вызываете функцию и передаете аргумент параметру, имеющему значение по умолчанию, функция будет использовать
# этот аргумент вместо значения по умолчанию.
#
# Однако если вы не передадите аргумент, функция будет использовать значение по умолчанию.

# В определении  функции сперва описываются все обязательные параметры, только затем следуют необязательные параметры.

# Никогда не используйте изменяемые объекты в качестве значений по умолчанию.
# К изменяемым объектам у нас относятся:
#
# списки
# словари
# множества

# Значение по умолчанию вычисляется только один раз при определении функции.
# Как только вы определите свою функцию с необязательными параметрами, каждое значение по умолчанию будет создано
# и сохранено один раз. Значит при каждом вызове данной функции вы будете иметь дело с одним и тем же значением по
# умолчанию, он  будет занимать одну и ту же ячейку в памяти.  А зная адрес, в котором хранится изменяемый объект,
# можно легко внести в него изменения.

# В этом и заключается самая большая ошибка при работе с изменяемыми объектами в качестве дефолтных
# значений. Поэтому всегда, когда вам нужен изменяемый объект в значении по умолчанию параметра, делайте так
#
#       1️⃣ сперва присваивайте параметру значению None
#
#       2️⃣ внутри функции проверяйте, если параметр принимает None, значит создаем пустой изменяемый объект
#
# Вот как должна выглядеть программа, которая создает новый пустой список по умолчанию для параметра my_list

def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))
    return my_list

# С помощью функции id легко убедиться в том, что вы всегда будете иметь дело с одним и тем же объектом по умолчанию
# при вызове функции.

def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))
    return my_list


result1 = append_to_list(10)
result1 = append_to_list(15, result1)
result2 = append_to_list(25)
result2 = append_to_list(37, result2)

def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
       my_dict = {}
    my_dict[key] = value
    print(my_dict)

append_to_dict(10, 100)
append_to_dict(20, 200)

# Добавление в корзину покупок
# Ваша задача написать функцию add_item, которая добавляет в корзину (глобальная переменная shopping_list)
# товар и его количество.
#
# Функция add_item обязательно должна принимать имя товара и необязательно - его количество (по умолчанию оно равно 1)

shopping_list = {}
def add_item(name, digit = 1):
    if name not in shopping_list:
        shopping_list.setdefault(name, digit)
    else:
        shopping_list[name] += digit
    return shopping_list

# Исправьте функции так, чтобы добавление одной оценки студенту не влияло на оценки других учеников
def create_student(name, age, marks = None):
    if marks is None:
        marks = []
    return {
        'name': name,
        'age': age,
        'marks': marks  # оценки
    }


def add_mark(student, mark):
    student['marks'].append(mark)


ivan = create_student('Ivan', 15, [3, 4, 5])
anatoliy = create_student('Anatoliy', 16, [2])
add_mark(ivan, 4)
add_mark(ivan, 5)
add_mark(anatoliy, 4)
add_mark(anatoliy, 5)
add_mark(anatoliy, 2)
print(ivan['marks'])
print(anatoliy['marks'])

Поход в ресторан
# Мы часто сталкиваемся с математической проблемой, когда после совместного похода в ресторан необходимо посчитать
# сколько должен каждый человек. Давайте создадим функцию  calculate_per_person, которая поможет выполнить расчет.
#
# Будем считать, что у нас идеальная ситуация, когда между N количеством людей нужно разделить счет поровну.
# Также в счет нужно включить чаевые официанту, которые по умолчанию составляют 10%.
#
# Итого получаем, что функция calculate_per_person может принимать следующие аргументы
#
# обязательно счет за ресторан
# обязательно количество людей
# необязательно процент чаевых официанту, по умолчанию 10%
# Функция calculate_per_person должна вернуть результат - сумму, которую должен заплатить каждый участник ужина.
#
# При расчете у  вас будут возникать вещественные числа, результат нужно будет округлять функцией round до второго
# разряда после запятой

def calculate_per_person(bill, num, tips = 10):
    rez = (bill +  (bill * tips / 100))/num
    return round(rez, 2)

print(calculate_per_person(200.0, 4))

