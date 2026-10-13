# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task_1(name):
    '''
    Задача 1. Переменные, типы, f-строки
    Создай переменные:
    name = "Ivan"
    age = 25
    height = 1.85
    is_student = True
    Выведи каждую переменную и её тип через type().
    С помощью f-строки выведи: Иван, 25 лет, рост 1.85.
    Затем переприсвой age = "двадцать пять" и снова выведи тип age.
    В комментарии объясни, почему Python — нестрого типизированный язык.'''
    name = 'Ivan'
    age = 25
    height = 1.85
    is_student = True
    print(f'name = {name}, name type = {type(name)}')
    print(f'age = {age}, age type = {type(age)}')
    print(f'height = {height}, height type = {type(height)}')
    print(f"is_student = {is_student}, is_student type = {type(is_student)}")
    print(f'{name}, {age} лет, рост {height}.')
    age = 'двадцать пять'
    print(type(age))
    # Python не строго типизированный язык, т.к. в одну и ту же перменнную можно по очереди назначать значения разных типов
    # и они будут без ошибок присваиваться.


def task_2():
    '''
    Задача 2. Множественное присваивание и распаковка
    Сделай:

    x = y = z = 0
    print(f"x = {x}, y = {y}, z = {z}")
    Создай кортеж coordinates = (10, 20, 30) и распакуй его в x, y, z.
    Выведи новые значения.
    Поменяй местами a = 5, b = 10 одной строкой.
    Выведи результат.'''
    x = y = z = 0
    print(f"x={x}, y={y}, z={z}")
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    print(f'x={x}, y = {y}, z = {z}')
    a = 5
    b = 10
    a, b = b, a
    print(f'a = {a}, b = {b}')


def task_3():
    '''Задача 3. Числа и арифметика
    Даны a = 7, b = 3.
    Выведи:
    a / b
    a // b
    a % b
    a ** b
    Проверь неточность float: выведи 0.1 + 0.2.
    Используй:
    round(3.14159, 2)
    math.floor(3.7)
    math.ceil(3.1)
    math.trunc(-3.7)
    Импортируй random и выведи:
    random.randint(1, 10)
    random.uniform(1.5, 3.5)
    random.choice([1, 3, 5, 7, 9])
    Также выведи:
    abs(-10)
    max(1, 5, 3)
    sum([1, 2, 3, 4, 5])
    int("42")
    float("3.14")'''
    import math
    a = 7
    b = 3
    print(f'a/b = {a / b}')
    print(f'a//b = {a // b}')
    print(f'a%b = {a % b}')
    print(f'a**b = {a ** b}')
    print(f'0.1 + 0.2 = {0.1 + 0.2}')  # 0.30000000000000004
    print(f'round(3.14159, 2) = {round(3.14159, 2)}')
    import math
    print(f'math.floor(3.6) = {math.floor(3.6)}')
    print(math.ceil(3.1))
    print(math.trunc(-3.7))
    import random
    print(random.randint(1, 10))
    print(random.uniform(1.1, 12.4))
    print(random.choice([1, 3, 5, 7, 9]))
    print(abs(-10))
    print(max(13, 50, 19))
    print(sum([123, 19, 23]))
    print(10 + int("42"))
    print(5 + float("3.14"))


def task_4():
    '''Задача 4. Строки: создание, индексы, срезы
Создай многострочную строку через """...""".
Создай raw-строку для пути: r"C: обратный слеш Users обратный слеш stepa".
Выведи обе строки.
Сделай:
"Конкатени" + "руем"
"42" * 5
Возьми строку s = "Programming".
Выведи:
s[0]
s[-2]
s[0:6]
s[::2]
s[::-1]
Попробуй изменить s[0] = "p" и убедись, что строки неизменяемы. Ошибку закомментируй.'''
    stroka_mnogostrochka = '''raz
    dva 
    tri stroki '''
    siraya_stroka = r'C:\users\stepa'
    print(siraya_stroka)
    print(stroka_mnogostrochka)
    stroka_konkatenashka = "Конкате" + 'niruem'
    print(stroka_konkatenashka)
    print('42' * 5)
    s = 'Programming'
    print(s[0])
    print(s[-2])
    print(s[3:])
    print(s[::2])
    print(s[::3])  # Pgmn
    print(s[::-1])  # gnimmargorP
    # s[0] = 'G'  # TypeError: 'str' object does not support item assignment


def task_5():
    '''Задача 5. Методы строк
    Дана строка:
    python
    text = "  отличный день!  "
    Примени и выведи результат:
    .strip()
    .lstrip()
    .rstrip()
    .strip('.') — создай отдельную строку с точками
    .upper()
    .lower()
    .title()
    .capitalize()
    .find("день")
    .count("н")
    .startswith("отлич")
    .endswith("!")
    'день' in text
    .replace("отличный", "прекрасный")
    .split()
    .split(',') — создай строку с запятыми #На самом деле создаётся список, а не строка. Видимо ИИ ошибся.
    ' '.join(['раз', 'два'])
    '\\'.join(['C:', 'Program Files', 'stepa'])'''
    t = '        отличный  день     '
    print(t.strip())
    print(t.lstrip())
    print(t.rstrip())
    t2 = '. words and. more them..'
    print(t2.strip('.'))
    print(t2.upper())
    print(t2.title())  # . Words And. More Them..
    t2 = 'words these'
    print(t2.capitalize())  # Words these
    print(t2.find('s'))
    print(t2.count('e'))
    t2 = 'Tee is heree'
    print(t2.count('ee'))
    t = 'отличный день'
    print(t.startswith('отлич'))
    print(t.endswith('день'))
    print('ень' in t)
    print('ё' in t)
    print(t.replace('е', 'ё'))
    print(t.split())  # ['отличный', 'день']
    print('  '.join(['one', 'two', 'three']))
    print('\\'.join(['C:', 'users', 'stepa']))


def task_6():
    '''Задача 6. Форматирование строк
Даны name = "Иван", age = 25.
Выведи одну и ту же фразу тремя способами:
f-строка: f"Привет, {name}! Тебе {age} лет."
.format(): "Привет, {}! Тебе {} лет.".format(name, age)
%: "Привет, %s! Тебе %d лет." % (name, age)
Добавь комментарий, какой способ рекомендуется и почему.'''
    name = 'Ivan'
    age = 25
    print(f'Привет, {name}! Тебе {age} лет.')  # Это рекомендованный способ
    print('Привет, {}! Тебе {} лет.'.format(name, age))  # Старый способ - не рекомендутся.
    print('Привет, %s! Тебе %d лет.' % (name, age))  # Старый способ - не рекомендутся.


global y
x = 10


def change_global_task_7():
    global x
    x = 20
    print(x)


def task_7_local(z):
    '''Задача 7. Область видимости и global
    Создай глобальную переменную x = 10.
    Напиши функцию change_global(), которая через global x меняет её на 20.
    Вызови функцию и выведи x.

    Затем напиши функцию local_x(), которая без global создаёт свою локальную x = 30.
    Вызови её и выведи глобальный x — он не должен измениться.

    В комментарии напиши, почему лучше минимизировать глобальные переменные.'''
    print(z)
    x = 30
    print(x)
    print("Глобальная через globals():", globals()['x'])
    print(x)


def task_8():
    '''Задача 8. Логика, is и ==, bool()
    Даны a = True, b = False.
    Выведи:
    a and b
    a or b
    not a
    Создай:
    python
    my_scores = [1, 2, 3]
    friend_scores = [1, 2, 3]
    Выведи:
    my_scores == friend_scores
    my_scores is friend_scores
    Теперь сделай friend_scores = my_scores и снова проверь is.
    Объясни разницу в комментарии.
    Выведи bool() для:
    100, 0, 0.0, "", (), [], {}, None, False.'''
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not b)
    my_scores = [1, 2, 3]
    friend_scores = [1, 2, 3]
    stepa_scores = [7, 8, 9]
    print(my_scores == friend_scores)  # Равны ли элементы коллекций? Да.
    print(my_scores is friend_scores)  # Уазывают ли ссылки на один и тот же объект? Нет.
    print(my_scores.__len__() == stepa_scores.__len__())
    print(my_scores.__len__())
    print(bool(100))
    print(bool(0))
    print(bool(0.0))
    print(bool(''))
    print(bool([]))
    print(bool('b'))


def task_9():
    '''Задача 9. Имена, стиль, регистрозависимость
    Создай переменные в snake_case:
    user_name = "Ivan"
    user_age = 25
    MAX_SPEED = 120 — как константу
    Проверь регистрозависимость:
    python
    name = "Ivan"
    Name = "Petr"
    Выведи обе переменные.
    Создай переменную _hidden = 42 и выведи её.
    Выведи тип каждой переменной через type().
    В комментарии оставь ссылку на PEP 8: peps.python.org/pep-0008/.'''
    user_name = 'Ivan'
    user_age = 25
    MAX_SPEED = 120
    _hidden = 42
    print(_hidden)
    print(type(user_name))
    print(type(user_age))
    print(type(MAX_SPEED))


def build_profile_task_10():
    '''Задача 10. Мини-проект: карточка сотрудника
    Напиши скрипт, который:
    Запрашивает у пользователя имя, возраст, ставку за час и количество отработанных часов.
    Очищает имя через .strip() и .title().
    Считает зарплату: salary = rate * hours.
    Округляет зарплату до 2 знаков через round().
    Генерирует случайный ID сотрудника через random.randint(1000, 9999).
    Выводит карточку через f-строку:
    text
    ID: 4821
    Имя: Иван
    Возраст: 25
    Зарплата: 12345.67
    Выводит типы всех переменных.
    Если возраст больше 18, выводит Доступ разрешён, иначе Доступ запрещён.'''
    user_name = input('Enter name\n')
    user_age = input('Enter age\n')
    user_salary = input('Enter salary\n')
    user_hours = input('Enter hours\n')
    user_name = user_name.strip().title()
    # print(user_name)
    salary = round(float(user_salary) * float(user_hours), 2)
    import random
    id = random.randint(1000, 9999)
    print(f'''ID: {id}
Имя: {user_name}
Возраст: {user_age}
Зарплата: {salary}
{'Доступ разрешен' if int(user_age) > 18 else 'Доступ запрещён'}''')


def task_11(pet_name, pet_type='dog'):
    '''Создать функцию с именованными параметрами по умолчанию'''
    print(pet_name)
    print(pet_type)


def make_pizza(**toppings):
    '''Создать функцию с именованными параметрами (словарём, где ключ - имя перменной, значение - значение переменной).'''
    for key, value in toppings.items():
        print(key + ' ' + str(value))
    print(toppings.__len__())


def iterate_teas(*teas):
    '''Создать функцию с произвольным количеством позиционных (неименованных) параметров.'''
    for tea in teas: print(tea)
    print(teas.__len__())


def check_age_task_15(age):
    '''Задача 5. if / elif / else
Напиши функцию check_age(age):
если age >= 18 — вывести buy boose;
если age < 0 — вывести Некорректный возраст;
иначе — вывести Слишком молод.
Вызови для 20, 16, -5.
Проверь, что else стоит на одном уровне отступа с if.'''
    if age >= 18:
        print('buy boose')
    elif age < 0:
        print('incorrect age')
    else:
        print('too young')


def task_16(score):
    '''Задача 6. Вложенные if и отступы
Напиши функцию grade(score):
если score >= 90:
если score == 100 — вывести Perfect;
иначе — вывести Excellent;
иначе, если score >= 75 — вывести Good;
иначе, если score >= 50 — вывести Pass;
иначе — вывести Fail.
Вызови для 100, 95, 80, 60, 30.
Используй 4 пробела. Убедись, что в файле нет табов.'''
    if score >= 90:
        if score == 100:
            print('perfect')
        else:
            print('excellent')
    elif score >= 75:
        print('Good')
    elif score >= 50:
        print('pass')


def get_status_task_17(age):
    '''Задача 7. Тернарный оператор
Дано:
age = 17
status = "совершеннолетний" if age >= 18 else "несовершеннолетний"
Напиши функцию get_status(age), которая возвращает статус через тернарный оператор. Вызови для 17, 18, 25.'''
    return 'grown up' if int(age) >= 18 else 'underage'


def max_func_task17(age, money):
    '''Напиши функцию max_of_two(a, b), которая возвращает большее число через тернарный оператор.
Проверь на (5, 10), (-3, -7), (0, 0).'''
    return age if age > money else money


def validate_password_task_18(password):
    '''Задача 8. isalpha() и isdigit()
Напиши функцию validate_password(password):
если password.isalpha() — вывести Пароль содержит только буквы;
иначе, если password.isdigit() — вывести Пароль содержит только цифры;
иначе — вывести Пароль смешанный.
Вызови:
validate_password("abc")
validate_password("123")
validate_password("abc123")
validate_password("")
Добавь комментарий: что вернёт "".isalpha()?'''
    if password.isalpha():
        print('Пароль содержит только буквы')
    elif password.isdigit():
        print('Пароль содержит только цифры')
    else:
        print('Пароль смешанный')


def order_pizza_task_19(size, *toppings, **details):
    '''Задача 9. Комбинация *args и **kwargs
Объяви функцию:
def order_pizza(size, *toppings, **details):
    ...
Внутри:
выведи размер;
выведи все топпинги через цикл;
выведи все детали заказа через details.items().
Вызови:
order_pizza("large", "сыр", "грибы", delivery=True, address="Москва")
Затем вызови без топпингов, но с delivery=False.
Добавь комментарий: почему size не попал в *toppings?'''
    print(size)
    for ts in toppings: print(ts)
    for key, value in details.items(): print(f'{key}: {value}')


def task_20():
    '''Задача 10. Мини-проект: карточка пользователя
Напиши скрипт, который:
Запрашивает у пользователя:
имя,
фамилию,
возраст,
город,
пароль.
Очищает имя и фамилию через .strip().title().
Проверяет пароль через validate_password() из задачи 8.
Определяет статус через get_status(age) из задачи 7.
Формирует профиль через build_profile(first, last, **user_info), передав город, возраст, статус.
Выводит карточку через f-строку:
text
Иван Иванов
Город: Москва
Возраст: 25
Статус: совершеннолетний
Пароль: смешанный
Если возраст меньше 0 — вывести Ошибка: некорректный возраст.
Используй функции, if/elif/else, тернарный оператор, **kwargs, isalpha()/isdigit().
Отступы — 4 пробела, без табов.'''
    name = input('Enter name\n')
    surname = input('Enter surname\n')
    password = input('Enter password\n')
    validate_password_task_18(password)
    age = input('Enter age\n')
    print(get_status_task_17(age))


def task_21():
    '''Задача 1. Списки: создание, индексы, срезы, изменение
Создай:
nums = [23, 18]
mixed = [1, "привет", True, 3.14]
empty = []
nested = [[1, 2], [3, 4]]
chars = list("Python")
from_tuple = list((1, 2, 3))
Выведи:
chars[0]
chars[::-1]
chars[::2]
chars[2:7]
nested[1][0]
Создай fruits = ["яблоко", "банан", "вишня"].
Замени fruits[0] на "Киви".
Выведи список.
Создай numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9].
Замени срез numbers[1:8] = [20, 30].
Выведи результат.
В комментарии напиши, что значит «список изменяемый, упорядоченный, с индексами».'''
    nums = [23, 18]
    mixed = [2, 'halo', True, 2.5]
    empty = []
    nested = [[1, 2], [3, 4]]
    chari = list('Python')
    from_tuple = list((23, 'ra', True))
    print(f'''{nums}\n{mixed}\n{empty}\n{nested}\n{chari}\n{from_tuple}''')
    print(chari[0])
    print(chari[::-1])
    print(chari[::4])
    print(chari[2:7])
    print(chari[2:7:2])
    print(nested[1][0])
    fruits = ['apple', 'banana', 'chery']
    fruits[0] = 'kiwi'
    print(fruits)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers[1:6] = [76, 34]
    print(numbers)


def task_22():
    '''Задача 2. Методы списка: добавление и удаление
Дано:
fruits = ["яблоко", "банан", "вишня"]
more_fruits = ["груша", "слива"]
Сделай по порядку и после каждого шага выводи список:
fruits.append("вишня")
fruits.insert(1, "апельсин")
fruits.extend(more_fruits)
fruits.remove("вишня")
fruits.pop(1)
fruits.pop()
fruits.clear()
Отдельно:
python
numbers = [10, 20, 30, 40, 50, 60]
del numbers[1:3]
Выведи numbers.
В комментарии объясни разницу между remove(), pop() и del.'''
    fruits = ['apple', 'banana', 'chery']
    more_fruits = ['pear', 'plum']
    fruits.append('chery')
    print(fruits)
    fruits.insert(1, 'orange')
    print(fruits)
    fruits.extend(more_fruits)
    print(fruits)
    fruits.remove('chery')  # Вызовет ошибку если элемента не будет ValueError: list.remove(x): x not in list
    print(fruits)
    print(fruits.pop(1))
    print(fruits)
    print(fruits.pop())
    print(fruits)
    print(fruits.pop())
    print(fruits)
    print(fruits.pop())
    print(fruits)
    fruits.clear()
    print(fruits)
    fruits = ['apple', 'banana', 'chery', 'pear', 'plum', 'orange']
    del fruits[1:3]
    print(fruits)


def task_23():
    '''Задача 3. Поиск, сортировка, копирование, длина
Дано:
fruits = ["банан", "яблоко", "банан", "вишня"]
Выведи:
"банан" in fruits
fruits.index("банан")
fruits.count("банан")
len(fruits)
Дано:
nums = [3, 1, 4, 2]
original = [3, 1, 4, 2]
Сделай nums.sort() и выведи.
Сделай nums.sort(reverse=True) и выведи.
Сделай sorted_list = sorted(original) и выведи original и sorted_list.
Объясни в комментарии, чем sort() отличается от sorted().
Копирование:
original = [1, 2, [3, 4]]
copy1 = original.copy()
copy2 = original[:]
copy3 = list(copy1)
Измени copy1[0] = 100.
Измени copy1[2][0] = 300.
Выведи original, copy1, copy2, copy3.
В комментарии объясни, что такое поверхностная копия (shallow copy) и почему
вложенный список изменился во всех копиях.'''
    fruits = ['banana', 'apple', 'banana', 'chery']
    print('banana' in fruits)
    print(fruits.index('banana'))
    print(fruits.count('banana'))
    print(len(fruits))
    nums = [3, 1, 4, 2]
    original = [3, 1, 4, 2]
    print(nums.sort())  # Won't work(returns None)
    print(nums)
    nums.sort(reverse=True)
    print(nums)
    sorted_list = sorted(original)  # Создал ещё один список, засунув в него отсортированные элементы из первого
    print(f'sorted_list = {sorted_list} ')
    print(f'original =  {original}')
    original = [1, 2, [3, 4]]
    copy1 = original.copy()
    print(copy1)
    copy2 = original[:]
    print(copy1)
    copy3 = list(copy2)
    print(copy3)
    copy1[0] = 100
    copy1[2][0] = 300
    print('before')
    print(original)  # [1, 2, [300, 4]] Здесь и далее вложенный список [300, 4]-это одна и та же область памяти, т.к.
    print(copy1)  # [100, 2, [300, 4]] copy() выполняет поверхностное копирование
    print(copy2)  # [1, 2, [300, 4]]
    print(copy3)  # [1, 2, [300, 4]]


def task_24():
    '''Задача 4. Кортежи: создание, индексы, срезы, распаковка
Создай:
t1 = (4, 4, "d")
empty = ()
one = (42,)
nested = ((1, 2), ("a", "b"))
coords = 10.5, 20.7, 30.9
Выведи type(coords).
Распакуй coords в x, y, z и выведи.
Создай:
k1 = tuple()
k2 = tuple("Python")
k3 = tuple([1, 2, 3])
Для t1 выведи:
t1[0]
t1[1:3]
t1.count(4)
t1.index("d")
В комментарии напиши, почему у кортежа только count() и index().'''
    t1 = (4, 4, 'd')
    empty = ()
    one = (42,)
    nested = ((1, 2), ('a', 'b'))
    coords = 10.5, 20.7, 30.9
    print(type(coords))
    x, y, z = coords
    print(f'{x} {y} {z}')
    k1 = tuple()
    k2 = tuple('Python')
    print(k1)
    print(k2)
    k3 = tuple([1, 2, 3])
    print(k3)
    k4 = (['aa', 'bb', 'cc'])
    print(k4)
    print(t1)
    print(t1[0])
    print(t1[1:3])
    print(t1.count(4))
    print(t1.index(4))
    tc = t1.__add__(('d', 'g'))
    print(tc)


def task_30():
    '''Задача 10. frozenset + мини-проект
Создай:
immutable_set = frozenset([1, 2, 3, 4])
Попробуй immutable_set.add(5). Закомментируй ошибку.
Используй immutable_set как ключ словаря:
data = {immutable_set: "значение"}
Добавь immutable_set как элемент другого множества.
Мини-проект: анализ текста.
Дан текст:
text = "python java python c++ java python"
Сделай:
список слов words_list;
множество уникальных слов unique_words;
словарь word_count, где ключ — слово, значение — сколько раз встретилось;
кортеж most_common = (слово, количество) для самого частого слова;
frozen_unique = frozenset(unique_words);
выведи всё: список, множество, словарь, кортеж, frozenset;
проверь "python" in unique_words и "ruby" in unique_words;
выведи len(unique_words);
отсортируй уникальные слова и выведи.
В комментарии напиши, почему поиск в множестве быстрее, чем в списке.'''
    immutable_set = frozenset([1, 2, 3, 4])
    # immutable_set.add(7)
    data = {immutable_set: 'Value', 'wd': 'ew'}  # frozenset неизменяемый, а значит м.б. использован как ключ в словаре
    print(data)
    mnozhestvo = {'a', 'f', immutable_set}
    text = 'python java python c++ java python'
    words_list = text.split(' ')
    print(words_list)
    unique_words = set(words_list)
    print(unique_words)
    word_count = dict()
    for word in words_list: word_count[word] = words_list.count(word)
    max_key = max(word_count, key=word_count.get)
    most_common = (max_key, word_count[max_key])
    print(most_common)
    frozen_unique = frozenset(unique_words)
    print(frozen_unique)
    print('python' in unique_words)
    print('ruby' in unique_words)
    print(len(unique_words))
    unique_words.sort()
    print(unique_words)
    # words_list = ['alpha', 'beta', 'omega', 'gamma']
    # unique_words = {'glove', 'water', 'stick'}


def task_31():
    '''Задача 31. Создание словарей
Создай:
empty1 = {}
empty2 = dict()
person = {"name": "John", "age": 30}
from_list = dict([("name", "Anna"), ("age", 28)])
from_kwargs = dict(theme="dark", font_size=12)
Выведи все пять.
Выведи type() каждого.
В комментарии напиши, почему dict(theme="dark") работает, а dict(1="dark") — нет.'''
    empty_1 = {}
    empty2 = dict()
    person = {'name': "John", "age": 30}
    from_list = dict(([1, 2], [3, 4]))
    print(from_list)  # {1: 2, 3: 4}
    from_list2 = dict([(1, 2), (3, 4)])
    print(from_list2)  # {1: 2, 3: 4}
    #    from_list3=dict([1,2],[3,4])#TypeError: dict expected at most 1 argument, got 2
    from_list4 = dict([[1, 2], [3, 4]])
    print(from_list4)  # {1: 2, 3: 4}
    from_kwargs = dict(theme='dark', font=12)
    print(from_kwargs)  # {'theme': 'dark', 'font': 12}
    # Имена переменных не могут начинаться с цифр, поэтому dict(1='dark') не сработает
    print(
        f'{type(from_list)} {type(from_list2)} {type(from_list4)} {type(from_kwargs)}')  # <class 'dict'> <class 'dict'> <class 'dict'> <class 'dict'>


def task_32():
    '''Задача 32. Доступ, get, in, not in
Дано:
person = {"name": "John", "age": 30, "city": "Moscow"}
Выведи person["name"].
Выведи person.get("age").
Выведи person.get("phone").
Выведи person.get("phone", "Not specified").
Выведи "name" in person.
Выведи "phone" not in person.
Попробуй person["phone"] — закомментируй строку и объясни, почему это ошибка, а get — нет.'''
    person = {"name": "John", "age": 30, "city": "Moscow"}
    print(person['name'])
    print(person.get('age'))
    print(person.get('phone'))
    print(person.get('phone', 'Not specified'))
    print('name' in person)  # True
    print('John' in person)  # False
    print('phone' not in person)  # True
    # print(person['phone']) #KeyError: 'phone' - это незащищённый вариант обращения по ключу в отличие от get()


def task_33():
    '''Задача 33. Вложенные словари и безопасный доступ
Дано:
nested = {
    "person": {"name": "John", "age": 30},
    "contacts": {"email": "john@example.com"}
}
Выведи nested["person"]["name"].
Выведи nested.get("contacts", {}).get("email").
Выведи nested.get("contacts", {}).get("website", "Not specified").
Выведи nested.get("address", {}).get("city", "Unknown").
В комментарии объясни, зачем нужен {} вторым аргументом в get.'''
    nested = {
        'person': {'name': 'John', 'age': 30},
        'contacts': {'email': 'john@example.com'}
    }
    print(nested['person']['name'])
    print(nested.get('contacts', {}).get('email'))  # Здесь нужно указывать {} чтобы не было ситуации, когда contacts
    # вернул None и в итоге был бы вызов None.get('email'), что привело бы к ошибке, ведь get() безопасен только при
    # вызове на словаре, но не на None. В данном случае если будет None, то вызов произойдёт на пустом словаре по
    # умолчанию, который мы указали как {}.
    print(nested.get('contacts', {}).get('website', 'Not specified'))
    print(nested.get('address', {}).get('city', 'Unknown'))


def task_34():
    '''Задача 34. Добавление, обновление, удаление
Дано:
person = {"name": "John", "age": 30}
Добавь person["city"] = "New York", выведи.
Измени person["age"] = 31, выведи.
Сделай person.update({"age": 32, "job": "developer", "language": "Python"}), выведи.
Удали del person["job"], выведи.
Попробуй del person["salary"] — закомментируй и объясни ошибку.
Объясни в комментарии, что произойдёт, если в update() передать уже существующий ключ.'''
    person = {"name": "John", "age": 30}
    person['city'] = 'New York'
    print(person)
    person['age'] = 31
    print(person)
    person.update({'age': 32, 'job': 'developer', 'language': 'Python'})
    print(person)
    del (person['job'])
    print(person)
    # del (person['slary'])  # KeyError: 'slary' - обращаемся небезопасно по несуществующему ключу
    person.update({'age': 33})
    print(person)


def task_35():
    '''Задача 35. pop, popitem, clear
Дано:
person = {"name": "John", "age": 30, "city": "Moscow", "job": "developer"}
age_value = person.pop("age") — выведи age_value и person.
job_value = person.pop("job", "Not specified") — выведи.
salary_value = person.pop("salary", "Not specified") — выведи.
Попробуй person.pop("salary") без дефолта — закомментируй, объясни.
last_item = person.popitem() — выведи.
person.clear() — выведи.
В комментарии напиши, что вернёт popitem() в Python 3.7+.'''
    person = {"name": "John", "age": 30, "city": "Moscow", "job": "developer"}
    age_value = person.pop('age')
    print(age_value)
    print(person)
    job_value = person.pop("job", "Not specified")
    print(job_value)
    print(person.pop("salary", "Not specified"))
    print(person)
    # person.pop("salary")  # KeyError: 'salary'
    print(person.popitem())  # Pairs are returned in LIFO (last-in, first-out) order
    person.clear()
    print(person)


def task_36():
    '''Задача 36. keys, values, items, итерация
Дано:
person = {"name": "John", "age": 30, "city": "Moscow"}
Выведи person.keys().
Выведи list(person.keys()).
Выведи list(person.values()).
Выведи list(person.items()).
Пройди циклом for key in person: — выведи каждый ключ.
Пройди for value in person.values(): — выведи каждое значение.
Пройди for key, value in person.items(): — выведи "key -> value".
В комментарии объясни, чем keys() отличается от list(keys()).'''
    person = {"name": "John", "age": 30, "city": "Moscow"}
    print(person.keys())
    print(list(person.values()))
    print(person.values())
    print(type(person.values()))  # <class 'dict_values'>
    print(list(person.items()))  # <class 'list'>
    print(type(list(person.values())))
    for key in person: print(key)  # для ключа не надо указывать .keys()
    for value in person.values(): print(value)  # для значения надо указывать .values()
    for key, value in person.items(): print(f'{key} -> {value}')


def task_37():
    '''Задача 37. Dict comprehension и fromkeys
Создай:
squares = {x: x ** 2 for x in range(1, 6)}
Создай:
evens = {x: x * 10 for x in range(10) if x % 2 == 0}
Создай:
defaults = dict.fromkeys(["name", "age", "city"], None)
Создай defaults2 = dict.fromkeys(["a", "b", "c"], 0), выведи.
В комментарии напиши, что будет, если вторым аргументом в fromkeys()
передать список: dict.fromkeys(["a", "b"], []).'''
    squares = {x: x ** 2 for x in range(1, 6)}
    print(squares)
    evens = {x: x * 10 for x in range(10) if x % 2 == 0}
    print(evens)
    defaults = dict.fromkeys(["name", "age", "city"], None)
    print(defaults)
    defaults2 = dict.fromkeys(["a", "b", "c"], 0)
    print(defaults2)
    dicti = dict.fromkeys(["a", "b"], [])
    print(dicti)  # {'a': [], 'b': []}


def task_38():
    '''Задача 38. Shallow copy vs deep copy
Дано:
original = {"name": "John", "nested": {"age": 30, "city": "Moscow"}}
Сделай три «поверхностные» копии:
shallow1 = original.copy()
shallow2 = dict(original)
import copy; shallow3 = copy.copy(original)
Сделай глубокую копию:
deep1 = copy.deepcopy(original)
Измени shallow1["nested"]["age"] = 99, выведи все словари.
Измени deep1["nested"]["city"] = "SPb", выведи все словари.
В комментарии объясни, почему shallow1 изменил original, а deep1 — нет.'''
    original = {"name": "John", "nested": {"age": 30, "city": "Moscow"}}
    print(original)  # {'name': 'John', 'nested': {'age': 30, 'city': 'Moscow'}}
    shallow1 = original.copy()
    print(shallow1)  # {'name': 'John', 'nested': {'age': 30, 'city': 'Moscow'}}
    shallow2 = dict(original)
    print(shallow2)  # {'name': 'John', 'nested': {'age': 30, 'city': 'Moscow'}}
    import copy
    shallow3 = copy.copy(original)
    print(shallow3)  # {'name': 'John', 'nested': {'age': 30, 'city': 'Moscow'}}
    print('----------------')
    deep1 = copy.deepcopy(original)
    print(deep1)
    shallow1['nested']['city'] = 'New York'
    print(original)  # {'name': 'John', 'nested': {'age': 30, 'city': 'New York'}}
    print(deep1)  # {'name': 'John', 'nested': {'age': 30, 'city': 'Moscow'}}


def task_39():
    '''Задача 39. Объединение двух списков в словарь, счётчик
Дано:
names = ["Anna", "Bob", "Cara"]
grades = [5, 4, 5]
Собери словарь через цикл:
result = {}
for i in range(len(names)):
    result[names[i]] = grades[i]
Выведи.
Сделай то же через zip():
result2 = dict(zip(names, grades))
Выведи и сравни.
Дан список:
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
Посчитай частоты через счётчик:
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
Выведи counts.
Найди самое частое слово через max(counts, key=counts.get).'''
    names = ["Anna", "Bob", "Cara"]
    grades = [5, 4, 5]
    result = {}
    for i in range(len(names)):
        result[names[i]] = grades[i]
    print(result)
    result2 = dict(zip(names, grades))
    print(result2)
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)
    print(max(counts, key=counts.get))


def task_40():
    '''Задача 40. Мини-проект: анализ текста через словарь
Дан текст:
text = "python java python c++ java python rust go python java rust"
Сделай скрипт, который:
Разбивает текст на слова: words = text.split().
Строит word_count — словарь {word: count} через цикл с counts.get(word, 0) + 1.
Строит unique_words = set(words).
Строит sorted_words = sorted(unique_words) — отсортированный список уникальных слов.
Находит самое частое слово:
max_key = max(word_count, key=word_count.get)
most_common = (max_key, word_count[max_key])
Строит frozen = frozenset(unique_words).
Создаёт вложенный словарь:
report = {
    "total_words": len(words),
    "unique_count": len(unique_words),
    "most_common": most_common,
    "all_counts": word_count,
}
Выводит всё через for key, value in report.items():.
Проверяет "python" in word_count и "ruby" in word_count.
Через copy.deepcopy() создаёт копию report, меняет в копии most_common
на ("test", 0) и показывает, что оригинал не изменился.'''
    text = "python java python c++ java python rust go python java rust"
    words = text.split()
    word_count = {}
    for w in words: word_count[w] = words.count(w)  # Работает,но не по заданию. Как сделать?
    print(word_count)
    unique_words = set(words)
    print(unique_words)
    sorted_words = sorted(unique_words)
    print(sorted_words)
    max_key = max(word_count, key=word_count.get)
    print(max_key)
    most_common = (max_key, word_count[max_key])  # просто создал кортеж
    print(most_common)
    frozen = frozenset(unique_words)
    print(frozen)
    report = {
        "total_words": len(words),
        "unique_count": len(unique_words),
        "most_common": most_common,
        "all_counts": word_count,
    }
    print(report)
    print('python' in word_count)
    print('ruby' in word_count)
    import copy
    copied = copy.deepcopy(report)
    print(copied)
    copied['most_common'] = ('test', 0)
    print(copied)


def task_41():
    """Task 41. For loops and range variants.
    Goal: practice every range form and basic iteration.
    Step 1. Create a list `fruits` with at least 4 items and print each via
    `for fruit in fruits`.
    Step 2. Print numbers 0..4 using `range(5)`.
    Step 3. Print numbers 2..4 using `range(2, 5)`.
    Step 4. Print odd numbers 1..9 using `range(1, 10, 2)`.
    Step 5. Print numbers 10 down to 1 using a negative step.
    Step 6. Iterate over the string `"python"` and print each char on its own line.
    Step 7. Use `enumerate(fruits)` to print `index -> fruit` pairs.
    Step 8. In a comment, explain the Java difference for classic indexed loops.
    Hint: check the `range(start, stop, step)` signature in your notes.    """
    fruits = ['kiwi', 'banana', 'apple', 'orange']
    print('-1:-')
    for fruit in fruits: print(fruit)
    print('-2:-')
    for n in range(5): print(n)
    print('-3:-')
    for n in range(2, 5): print(n)
    print('-4:-')
    for n in range(1, 10, 2): print(n)  # ВАЖНО - В ЦИКЛЕ FOR СТАВИМ НЕ ДВОЕТОЧИЯ, А ЗАПЯТЫЕ ЧТОБЫ БРАТЬ
    # НЕЧЕТНОЕ НАПРИМЕР range(start, stop, step)
    print('-5:-')
    for n in range(10, 1, -1): print(n)  # Здесь надо указывать откуда идём вниз сначала - ОТ 10 (для -1)
    print('-6:-')
    for c in 'python':
        print(c)
    print('-7:-')
    for f in enumerate(fruits):  # Здесь f - кортеж из индекса очередного элемента и самого элемента списка fruits
        print(f'{f[0]}->{f[1]}')


def task_42():
    '''Task 42. While loop with break, continue, else.
1. Use count starting at 1; while count <= 5, print count.
2. Same, but stop early with break when count == 3.
3. Use continue to skip even numbers from 1 to 10.
4. Use while True with a break condition.
5. Add an else block to a while loop that ends normally.
6. Add an else block to a while loop that breaks — show else is skipped.
7. Explain in a comment: when does the else branch run.'''
    print('-1:-')
    count = 1
    while (count <= 5):
        count = count + 1
        print(count)
    print('-2:-')
    count = 1
    while (count <= 3):
        count = count + 1
        print(count)
    print('-3:-')
    count = 1
    while (count < 10):
        count = count + 1
        if (count % 2 == 0): continue
        print(count)
    print('-4:-')
    while (True):
        n = random.randint(1, 10)
        print(n)
        if n == 7: break
    print('-5:-')
    n = 0
    while (n < 5):
        n = n + 1
        print(n)
    else:  # отрабатывает в случае нормального завершения цикла (если не было завершения по break)
        print('Нормальное завершение')  # Также работает и для цикла for
    print('-6:-')
    n = 0
    while (n < 5):
        n = n + 1
        print(n)
        if n == 3: break  # В этом случае до else не дойдёт
    else:
        print('Нормальное завершение')  # Также работает и для цикла for


def task_43():  # ПРИМЕРНО 147 СТРОКА КОНСПЕКТА. ДАЛЬШЕ РЕШИЛ ПРОДОЛЖИТЬ УСКОРЕННО, Т.К. ПРОКРАСТИНИРОВАЛ МНОГО
    """    Task 43. List comprehension.
    1. Build list of squares for range(10).
    2. Build list of squares for even numbers only.
    3. Build list of strings from ["a","b","c"] uppercased.
    4. Build list of tuples (index, value) from ["x","y","z"] using enumerate inside comprehension.
    5. Build list of lengths of words in ["hi","hello","world"].
    6. Build list of numbers 1..20 that are divisible by 3.
    7. Build flattened list from [[1,2],[3,4],[5,6]].
    8. Explain in a comment: difference between list comprehension and generator expression.    """
    print('-1:-')
    list_of_squares = [i ** 2 for i in range(1, 10)]
    print(list_of_squares)
    print('-2:-')
    list_of_squares_for_even_numbers = [i ** 2 for i in range(2, 10, 2)]
    print(list_of_squares_for_even_numbers)
    print('-3:-')
    listik = ["a", "b", "c"]
    listik_upper = []
    for l in listik:
        listik_upper.append(l.upper())
    print(listik_upper)
    print('--alternative:--')
    listik = ['а', 'б', 'в']
    listik_upper_alternative = [s.upper() for s in listik]
    print(listik_upper_alternative)
    print('-4:-')
    listik = ['x', 'y', 'z']
    listik_of_tuples = []
    for l in enumerate(listik):
        listik_of_tuples.append(l)
    print(listik_of_tuples)
    print('-alternatively:-')
    lot = [(i, val) for i, val in enumerate(listik)]
    print(lot)
    print('-5:-')
    print('-6:-')
    print('-7:-')


import sys

'''solve_00 начало определения'''

'''Условие: дан список браузеров через ,. Найти самый частый. Если ничья — выбрать тот, у которого первое 
вхождение позже (то есть в данных он появился позже всех из лидеров). Если и тут ничья 
(одинаковый индекс — невозможно, но на всякий случай) — лексикографически меньший.
Пример:
Chrome, Firefox, Chrome, Safari, Firefox, Chrome  → Chrome
GET, POST, PUT, POST, GET, PUT                     → PUT
A, B, C, B, A, C, D                                → C
DELETE                                             → DELETE'''


def read_line():
    return sys.stdin.readline().rstrip('\n')


def write(value):
    sys.stdout.write(str(value))


def writeln(value=''):
    sys.stdout.write(str(value) + '\n')


def solve_00():
    text = read_line()
    text_split = text.split(', ')
    dicti = {}
    for bro in text_split:
        if bro in dicti:
            dicti[bro] += 1
        else:
            dicti[bro] = 1
    m = max(dicti.values())
    keys = [k for k, v in dicti.items() if v == m]
    writeln(keys[keys.__len__() - 1])
    '''solve_00 конец определения'''


'''solve_01 Анализ конверсии пользователей 
Вы анализируете результаты email-рассылки.
Для каждого пользователя известно, открыл ли он письмо:
1 - пользователь совершил целевое дейстиве
0 - пользователь не совершил целевое действие
Нужно посчитать конверсию - процент пользователей, которые совершили целевое действие. 
Результат нужно вывести с округлением до двух знаков после запятой. 
Формат ввода входных данных:
1 0 1 0 0 1 1 0
Формат выходных данных:
50.00
'''
import sys
import io


def read_line():
    return sys.stdin.readline().rstrip('\n')


def write_value(value):
    sys.stdout.write(str(value))


def writeln(value=''):
    sys.stdout.write(str(value) + '\n')


def solve_01():
    text = read_line()
    text_split = text.split(' ')
    # print(text_split)
    num_1 = text_split.count('1')
    num_0 = text_split.count('0')
    print(num_0)
    print(num_1)
    print(round((num_1 / (num_0 + num_1)) * 100, 2))  # ЗДЕСЬ Я ОШИБСЯ, ВЕДЬ 0.375 ОКРУГЛИТСЯ ДО 0.38 СНАЧАЛА


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''solve_01 начало запуска'''
    test_input = '1 0 1 0 0 1 1 0'  # 50.0
    sys.stdin = io.StringIO(test_input)
    solve_01()
    print('-------------')
    test_input = '0 0 1 0 0 1 1 0'  # 37.5
    sys.stdin = io.StringIO(test_input)
    solve_01()
    print('-------------')
    test_input = '0 0 0 0 0 0 0 0'  # 0.0
    sys.stdin = io.StringIO(test_input)
    solve_01()
    print('-------------')
    test_input = '1 1 1 1 1 1 1 1'  # 100.0
    sys.stdin = io.StringIO(test_input)
    solve_01()
    print('-------------')
    test_input = '0 0 1 0 0 0 0 0 0'  # 11.11
    sys.stdin = io.StringIO(test_input)
    solve_01()
    print('-------------')
    test_input = '0 0 1 0 0 1 0 0 0 0 0 0 0'  # 15.38
    sys.stdin = io.StringIO(test_input)
    solve_01()
    '''solve_01 конец запуска'''
    '''solve_00 начало запуска'''
    # # ── имитация теста ──────────────────────────
    # test_input = "Chrome, Edge, Firefox, Chrome, Edge, Safari, Firefox, Edge, Chrome\n"  # →Edge
    # sys.stdin = io.StringIO(test_input)  # имитация чтения через создание псевдо инпута
    # solve_00()
    # # ────────────────────────────────────────────
    # test_input = "Chrome, Firefox, Chrome, Safari, Firefox, Chrome"  # → Chrome
    # sys.stdin = io.StringIO(test_input)  # имитация чтения через создание псевдо инпута
    # solve_00()
    # # ────────────────────────────────────────────
    # test_input = "GET, POST, PUT, POST, GET, PUT"  # → PUT
    # sys.stdin = io.StringIO(test_input)  # имитация чтения через создание псевдо инпута
    # solve_00()
    # # ────────────────────────────────────────────
    # test_input = "A, B, C, B, A, C, D"  # → C
    # sys.stdin = io.StringIO(test_input)  # имитация чтения через создание псевдо инпута
    # solve_00()
    # # ────────────────────────────────────────────
    # test_input = "DELETE"  # → DELETE'''"
    # sys.stdin = io.StringIO(test_input)  # имитация чтения через создание псевдо инпута
    # solve_00()
    # # ────────────────────────────────────────────
    '''solve_00 конец запуска'''

# order_pizza_task_19("large", "сыр", "грибы", delivery=True, address="Москва")
# order_pizza_task_19(34, delivery=False)
# validate_password_task_18('abc')
# validate_password_task_18('123')
# validate_password_task_18('abc123')
# validate_password_task_18('')
# print(max_func_task17(5, 10))
# print(max_func_task17(-3, -7))
# print(max_func_task17(0, 0))
# print(get_status_task_17(17))
# print(get_status_task_17(18))
# print(get_status_task_17(25))
# task_16(60)
# task_16(100)
# task_16(95)
# check_
# age_task_15(17)
# iterate_teas("сыр", 123, True)
# make_pizza()
# iterate_teas('black', 'white', 'green', 'fruit', 'herbal')
# make_pizza(name='Ivan', age=30, profession='programmer')
# task_11('Sharik')
# task_11('Bobrik', pet_type='cat')
# task_7_local(14)
# task_1('PyCharm')
# task_3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
