# Python-lessons

**Підготовка:** скачати та встановити Python з офіційного сайту до системи, опціонально додати до глобальних змінних системи (для windows)  
Встановити запуск в термінал на гарячу клавішу (н-д: ctrl+F10)  
При необхідності встановити віртуальне оточення `python -m venv venv` та перейти в нього `source path` (./venv/Scripts/activate)

Віртуальне оточення дає змогу працювати в відокремленому від основного (на рівні ОС) оточенні. Так різні ВО можуть містити різні версії бібліотек, недоступних ззовні

**Запуск командного рядка python:** `python`. Вийти: `exit()`

**Запуск файлу через консоль:** `python file.py`

## Змінні та літерали

`# comment` - коментар (строковий), `"""..."""` - багаторядковий коментар  
Декларація та ініціалізація: `num = 5`. Присвоєння нового значення так само  
Ручне видалення змінної: `del num`  
Локальні зміні, створені в блоці, не видимі поза ним (без директиви global)  
`global` використовується для створення, редагування або видалення глобальної змінної

**Прості типи даних (незмінні):**  
`12`, `-6`, `0` - int (ціле число)  
`1.2`, `-6.0`, `3e8` - float (дробове)  
`"Hello"` - str (строка)  
`True` - bool (булевий: так або ні)  
Для ручного перетворення змінної існують функції: `int()`, `float()`, `str()`, `bool()`  
Форматування рядка: `f"{var1} text {var2}"`

**Контейнерні типи данних (ітеровані):**  
`[0, True, [2]]` - список (list), упорядкований за індексами  
`(0, True, [2])`, `0, True, [2]`, `0,` - кортеж (tuple), упорядкований, незмінний  
`{0, True, [2]}` - множина (set), невпорядкований, неповторюваний  
`{'name': 'Alex', 'age': 25}` - словник (dictionary), множина пар ключ:значення (ключі можуть бути будь-якого незмінного типу)

Екранування символів рядка: `"\"Yes\""`  
Також є число `complex`, послідовність `range`, множина `frozenset` та бінарні типи.  
Для створення випадкового числа необхідно імпортувати random. `random.randrange(0, 1)`.  
Багаторядкові строки `"""..."""` дозволяють записати текст в кілька рядків з переносами.  
Чи належить до відповідного типу даних: `isinstance(x, type)`.

**Отримати тип:** `type(item)`

**Індексація**  
`[0]` - позитивний (перший від початку)  
`[-1]` - негативний (перший з кінця)  
`[start = 0: end = len]` - зріз за індексами (діапазон)  
`[start = 0: end = len: step = 1]` - вибірка в діапазоні з кроком

**Деструктуризація**
Дає можливість розібрати структуру на елементи  
`lst = [*lst1, *lst2]` розбирає два списки на елементи і додає їх в інший  
`dct = [**dct1, **dct2]` розбирає два словники на пари і додає їх в інший

## Оператори

**Арифметичні**  
`a + b` - додавання;  
`a - b` - віднімання;  
`a * b` - множення;  
`a / b` - ділення;  
`a // b` - цілочислове ділення  
`a % b` - залишок ділення;  
`a ** b` - степінь числа (2 \*\* 3 == 8)

**Присвоєння**  
`=` - присвоєння  
`*=` - арифметична з присвоєнням (для всіх операцій)

**Порівняння**  
`==` - дорівнює  
`!=` - не дорівнює  
`>` - більше  
`<` - менше  
`>=` - більше або дорівнює  
`<=` - менше або дорівнює

**Логічні**  
`and`, `&` - та (обидві умови вірні)  
`or`, `|` - або (одна з умов вірна)  
`not` - не (умова не вірна)

**Ідентифікації**  
`a is b` / `a is not b` - True коли a є / не є тим самим об'єктом, що і y.

**Приналежності**  
`a in b` - True при присутності елемента `a` в ітераторі `b`  
`a not in b` - True при відсутності елемента.

**Умовні**  
`if bool:` - якщо дана умова вірна  
`elif bool:` - якщо попередня невірна, а дана вірна  
`else:` - якщо попередня невірна  
`True if bool else False` - тернарний оператор (строкова функція, що повертає перший варіант при вірному виразі, інакше другий)  
`match cond:` перевіряє на відповідність cond (як switch):  
`case val1: code` виконується при cond == val1  
`case other: code` виконується при cond != жодному з попередніх

**Циклічні**  
`while bool:` - умовний цикл (виконується при вірності умови)  
`for i in sequence:` - ітеративний цикл, (виконується задану ітератором виразу кількість ітерацій (н-д: по елементах масива))  
`for i in range(start = 0, stop, step = 1)` - ітеративний цикл (має цілочисловий ітератор, обов'язковий параметр `stop`)  
`continue` - перервати поточну ітерацію  
`break` - перервати цикл  
`else:` - вираз, який виконується при нормальному завершенні цикла

**Виняткові**  
`try:` - блок пошуку винятків (помилок)  
`except:` - блок обробки винятків  
`except Exception:` - блок обробки конкретного типу винятків (може бути кілька для послідовної перевірки, може містити перелік типів в дужках)  
`except Exception as errorName:` - відловлює виняток і записує в змінну  
`else:` - спрацьовує при коректному завершенні try-блока  
`finally:` - спрацьовує будь-якому завершенні (try, except, error)  
`raise ErrorClass(args)` - створити помилку відповідного класу (перший арг - опис)

## Функції:

### Вводу-виводу

**Виведення в консоль:** `print()`  
При передачі декількох аргументів вони виведуться почергово,  
аргумент `sep=""` вказує розділювач (за умов.: " "),  
аргумент `end=""` вказує кінцевий символ (за умов.: "\n")  
`print('Hello', 'World', sep=', ', end="!")` >> `Hello, World!`  
Спецсимволи:  
`\n` - перенос строки;  
`\t` - символ табуляції;  
`\` - екранування символів (для використання спеціальних символів)

**Читання з консолі:** `input()`  
Зчитує строку, введену в консоль  
аргумент буде виведений перед читанням вводу  
`input("Enter message: ")` >> `Enter message: |`

### Загальні

`len(obj)` - повертає довжину ітерованого об'єкта  
`isinstance(obj, type)` - перевіряє чи відноситься до типу (може приймати кортеж типів)

### Математичні

`min(args[])`, `max(args[])` - шукає мінімум (максимум) серед аргументів;  
`abs(a)` - модуль числа;  
`pow(a, b)` - ступінь числа  
`round(a)` - округлення числа

### Об'єктні

`filter(func, obj)` - пропускає кожний елемент об-та через ф-ю та повертає задовільні  
`sum(obj[, start])` - повертає суму елементів об'єкта, починаючи зі start

**Спискові**  
`.append(val)` - додає елемент в кінець списку  
`.insert(idx, val)` - додає елемент за вказаним індексом  
`.extend(seq)` - додає елементи за виразом в кінець  
`.remove(val)` - видаляє перший елемент зі значенням  
`.pop(idx=-1)` - видаляє та повертає елемент за індексом (останній)  
`.sort()` - сортує список, повертає none*  
`.reverse()` - обертає список, повертає none  
`.clear()` - очищає список  
`.count(val)` - повертає кількість елементів зі значенням  
`.index(val)` - поверне індеск першого елементу зі значенням  
`.copy()` - повертає копію списку  
`list(obj)` - перетворює ітеративний об'єкт в список  
`[exp[ if cond] for i in iter[ if cond]]` - повертає список відповідно виразу exp, який формується на основі циклу ітератора, фільтрованого за умовою (можна опустити)  
*аргументом може бути `reverse = True` для оберненого сортування та/або `key = func`, який пропускає значення через ф-ю та сортує в порядку його результатів (назва).

**Кортежні**  
`.count(val)` - повертає кількість елементів зі значенням  
`.index(val)` - поверне індеск першого елементу зі значенням  
`tuple(obj)` - перетворює ітеративний об'єкт в кортеж

**Словникові**  
`.update(dict)` - доповнює словник іншим  
`.keys()` - повертає ітеративний об'єкт ключів  
`.values()` - повертає ітеративний об'єкт значень  
`.items()` - повертає ітеративний об'єкт кортежів ключів та значень  
`.get(key)` - повертає значення за вказаним ключем  
`.setdefault(key, val)` - повертає значення за ключем, якщо відсутній, створює з val  
`.pop(key)` - видаляє та повертає значення за вказаним ключем  
`.popitem()` - видаляє останній елемент  
`.clear()` - очищає словник  
`.copy()` - повертає копію словника  
`dict(dict)` - створює словник на основі іншого (копію)  
`dict.fromkeys(keys, value)` - повертає словник з ключами keys та спільним значенням

**Множинні**  
`.add(obj)` - доповнює множину об'єктом  
`.union(obj)` - повертає нову множину з елементами поточної множини і додаваної  
`.update(obj)` - доповнює множину елементами ітеративного об'єкта  
`.issubset(obj)` - перевіряє чи є підмножиною іншої  
`.issuperset(obj)` - перевіряє чи вміщає іншу множину  
`.intersection(obj)` - повертає нову множину зі спільними елементами множин (перетин)  
`.intersection_update(obj)` - видаляє елементи, відсутні в аргументі (перетин)  
`.isdisjoint(obj)` - перевіряє, чи є перетин множин  
`.symmetric_difference()` - повертає лише унікальні елементи обох множин  
`.summetric_difference_update(obj)` - зберігає лише унікальні елементи обох множин  
`.remove(obj)` - видаляє об'єкт, видає помилку при відсутності  
`.discard(obj)` - видаляє об'єкт, не видає помилку при відсутності  
`.copy()` - повертає копію множини  
`.clear()` - очищає множину  
`set(obj)` - перетворює ітеративний об'єкт в множину  
`frozenset(obj)` - перетворює ітеративний об'єкт в незмінну множину

**Текстові**  
`.count(sub[, start[, end]])` - кількість підстроки діапазону  
`.index(sub[, start[, end]])` - індекс підстроки діапазону  
`.is...()` - чи символи певної категорії (isUpper(), isLower())  
`.upper()` - повертає строку з великими літерами, не змінює дану  
`.lower()` - повертає строку з малими літерами, не змінює дану  
`.capitalize()` - повертає строку з першою великою літерою, не змінює дану  
`.strip([chars])` - повертає рядок, обрізавши chars напочатку і вкінці.  
`.replace(tar, val)` - заміняє всі tar на val.  
`.split(sep)` - розділяє строку на елементи ітеративного об'єкту за розділювачем  
`sep.join(obj)` - поєднує елементи ітеративного об'єкту в строку із розділювачем  
`.format(values)` підставляє values в `{}` рядка. Підтримує кілька змінних, зміну порядку, багаторазове використання, параметри форматування  
Для форматування можна використовувати інтерполяцію рядка `f"text {var1} {var2}`

### Файлові

Відкриття файлу: `file = open(path, mode="r", encoding="utf8")`  
`"r"` - читання;  
`"w"` - запис (переписує);  
`"a"` - запис (додає);  
`"x"` - створення (помилка, якщо вже існує);  
Читання файлу (з обмеженням символів): `file.read(len=all)`  
Читання наступного рядка: `file.readline()`  
Цикл for перебирає рядки файлу: `for line in file:`  
Запис в файл строки: `file.write(str)`  
Запис в файл кількох строк: `file.writelines([str1, str2)]`  
Закриття файлу: `file.close()`  
Для видалення файлу можна імпортувати бібліотеку `os` та викликати `os.remove(file)  
Конструкція `with open() as file:` автоматично закриває файл після роботи з ним (навіть після помилки або винятку)

### Користувацькі

Декларація: `def func(args[]):`  
Аргумент за умовчуванням: `arg=val`  
Довільні аргументи: `def func(*args):`, записує довільну кількість аргументів в кортеж  
Аргументи довільного ключового слова: `def func(**kwargs):`, записує в словник  
Важливий порядок: звичайні аргументи, _args, параметри за умовчуванням, **kwargs  
Повернути результат: `return `  
Виклик: `func(args[])` відповідно до порядку, вказаного вище  
Аргументи можна передавати парами ключ=значення  
**Анонімні функції\*\* - однострокові функції, які передаються в змінну, повертають тіло  
Декларація: `func = lambda args: res` (н-д: `multyple = lambda x, y: x _ y`)  
Виклик: `func(args[])`  
Перевизначення функцій передбачає написання ф-й з одною назвою та різними параметрами, заміняє попередню

## ООП

**Клас**  
Декларація класу `class ClassName:`  
всередині вказуються поля та методи класу  
Перший параметр ф-ї класу відображає поточний об'єкт, звичне ім'я `self`  
Ініціалізація екземпляра класу: `className = ClassName()`  
Перевизначення конструктора: `def __init__(self, args[]):`  
Ф-я `__str__(self)` викликається при приведенні екземпляра до рядка  
Існує багато інших "магічних" dunded методів (з двома підкресленнями), викликаються за певних умов

**Екземпляр (об'єкт)**  
Створення об'єкта: `name1 = ClassName(args[])`  
Зміна властивості об'єкта: `name1.param = value`  
Видалення властивості: `del name1.param`; об'єкта: `del name1`

**Спадкування**  
Класи-спадкоємці успадковують всі поля, методи та конструктори  
Позначення спадкування: `class Child(Parent):`  
Виклик батьківського конструктора: `super().__init__(args[])`

**Поліморфізм**  
Для різних класів методи зі спільною назвою і параметрами можуть бути викликані однаково  
(н-д в циклі for item in iter: item.method() незалежно, до якого класу він належить)
У спадкоємцях може перезаписуватися логіка методів з тим же ім'ям  
При відсутності відповідного метода буде викликаний батьківський

**Інкапсуляція**  
Для забезпечення правильності значень полів доступ до них організовується лише через методи (конструктори)  
Встановлення приватності поля: `__field = value`  
До приватних полів є доступ, але їх значення не змінюються  
Сама мова не підтримує дієвого засобу для заборони доступу до полів

## Модулі

`import moduleName`, `import modules.path.moduleName` - підключення вбудованих модулів  
`import sys, os` - підключення кількох модулів (небажано)  
`import moduleName as mn` - підключення зі вказанням псевдоніма  
`from math import sqrt, ceil` - підключення окремих полів та методів з модулю (можна додавати псевдоніми)  
`dir(moduleName)` - перераховує всі визначені імена модуля
Модулі шукаються в поточному каталозі (або іншому вказаному), а також в шляхах, описаних PYTHONPATH  
Шляхи PYTHONPATH зберігаються в sys.path бібліотеки sys

### Вбудовані модулі

`help("modules")` виводе список доступних модулів

**Модуль time**  
Дозволяє керувати часом виконання програми  
`time.sleep(sec)` - призупиняє виконання програми на sec секунд

**Модуль datetime**  
Дозволяє працювати з датою та часом  
`datetime.date(year, month, day)` створює і повертає об'єкт дати зі вказаною датою  
`datetime.date.today()` створює і повертає об'єкт дати з поточною датою  
`datetime.time(hour=0, minute=0, second=0, microsec=0, tzinfo=None)` повертає час  
`datetime.datetime(year, month, day [...])` створює об'єкт дати, можна додати час та ЧП  
`datetime.datetime.now()` - створює і повертає об'єкт датачасу з поточним датачасом  
Відокремити дату від часу: `datetimeObject.date()`, `datetimeObject.time()`  
Класи datetime, date, time мають метод `.strftime(format)` для форматування дати в рядок  
та метод `.strptime(str, format)` для парсингу рядка в дату  
Клас datetime.timedelta містить різницю між двома моментами до мікросекунди

**Модуль sys**  
Дозволяє працювати з проектом  
`sys.path` - поверне повний шлях до проєкту

**Модуль os** та **модуль system**  
Дозволяють працювати з ОС та платформою користувача  
`os.name` - поверне назву ОС  
`platform.system()` - поверне назву ОС

**Модуль math**  
Дозволяє працювати з математичними функціями  
`math.sqrt(n)` - поверне квадратний корінь числа (дробове)  
Крім того підтримує методи як `.ceil()`, `.floor()`, `.sin()`, `.cos()`, та інші  
а також константи як `.pi`, `.e`, `.inf`, `.nan`, `.tau`

**Модуль json**  
Дозволяє працювати з даними в форматі JSON  
`json.loads(data)` - конвертує JSON-дані в словник  
`json.dumps(dict[, indent[, sort_keys=bool]])` - конвертує словник в JSON-дані, форматує з пробілами, сортує по ключам  
dict = Object; list, tuple = Array; int, float = Number;  
str = String; True = true; False = false; None = null

**Модуль re**  
Дозволяє працювати з регулярними виразами (шаблонами пошуку)  
`.findall(pattern, str)` - шукає і повертає список всіх збігів  
`.search(pattern, str)` - шукає і повертає об'єкт-збіг  
`.split(pattern, str[, max])` - шукає і повертає список підстрок, розділених збігом  
`.sub(pattern, replacer, str[, max])` - шукає і заміняє всі збіги, повертає результат  
Об'єкт-збіг має властивості і методи `.string`, `.span()`, `.group()` та інші  
Метасимволи: `[]`, `\`, `.`, `^`, `$`, `*`, `+`, `?`, `{}`, `|`, `()`  
Спецсимволи: `\A`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S`, `\w`, `\W`, `\Z`  
Набори: `[abc]`, `[a-z]`, `[^abc]`, `[123]`, `[0-9]`, `[a-zA-Z]`, `[+]`

### Створення власного модуля

1. Створити окремий файл (папку)
2. Прописати поля, методи
3. Підключити модуль за назвою файлу (без розширення)

### Сторонні модулі

Знайти потрібний модуль можна на сайті pypi.org  
Встановити модуль через пакетний менеджер pip (встановлюється разом з python)  
В ОС Linux (Unix) pip може поставлятись в окремій упаковці pithon3-pip, який встановлюється окремо  
`pip install module` - встановити модуль  
`pip uninstall module` - видалити модуль  
`pip list` - перегляд встановлених модулів  
Встановлення відбувається глобально або локально при використанні віртуального середовища

## Розширені теми

### Ітератори

Ітератори - методи, які ітерують колекції (ітерабельні об'єкти)  
Метод `__iter__(self)` повертає об'єкт ітератора (унікальний для кожного виклику)  
Всередині ітератора реалізується метод `__next__(self)`, повертає наступний елемент  
Для переривання (завершення) ітерування використовується `raise StopIteration`  
Вбудований метод `iter(obj)` викликає `__iter__` об'єкта, `next(iter)` - `__next__`  
Цикл for використовує вбудовані iter та next в своїй реалізації

```py
class PowTwo:
  def __init__(self, max=0):
    self.max = max
  def __iter__(self):
    self.n = 0
    return self
  def __next__(self):
    if self.n <= self.max:
      result = 2 ** self.n
      self.n += 1
      return result
    else:
      raise StopIteration
numbers = PowTwo(3)
iterator = iter(numbers)
print(next(iterator))
for elem in numbers:
  print(elem)
```

### Генератори

Генератори - ф-ї, які повертають ітератори для створення послідовності значень під час повторення  
Використовують ключове слово `yield` замість `return`, яке створює значення і призупиняє виконання

```py
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
generator = PowTwoGen(3)
print(next(generator))
for elem in PowTwoGen(3):
  print(elem)
```

Вираз генератора - стислий спосіб створити генераторний об'єкт `(expression for item in iterable)`,  
expression - значення, яке повертатиметься для кожного елемента iterable  
```py
squares_generator = (i * i for i in range(3))
print(next(squares_generator))
```

### Замикання (closures)

Замикання - явище, за якого вкладена функція має доступ до змінних зовнішньої, навіть після закриття  
Може бути використане для забезпечення простого приховування даних та уникання глобальних значень

```py
def counter():
  count = 0
  def increase():
    nonlocal count
    count += 1
    return count
  return increase
counter1 = counter()
print(counter1())
counter2 = counter()
print(counter2())
```

### Декоратори

Дозволяють додавати шаблонний функціонал до або після функції
Декларація передбачає створення функції `def decor(func):`  
аргументом являється цілова функція  
тіло складає функція-обгортка, результат - та ж обгортка (без аргументів)  
Всередині обгортки прописується весь необхідний функціонал разом із викликом функції  
Виклик декоратора: `@decor`, далі вказується цільова функція

Приклад:
def validatior(func):
def wrapper(args):
print("before")
func(args)
print("after")
return wrapper

@validatior
def open_url(url):
webbrowser.open(url)
