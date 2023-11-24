#1
class Fractions:
    def init(self, whole_part, fractional_part):
        self.whole_part = whole_part
        self.fractional_part = fractional_part

#прибавление

    def add(self, other):
        new_fraction = Fractions(0, 0)
        new_fraction.whole_part = self.whole_part + other.whole_part
        new_fraction.fractional_part = self.fractional_part + other.fractional_part
        if new_fraction.fractional_part >= 100:
            new_fraction.whole_part += 1
            new_fraction.fractional_part -= 100
        return new_fraction

#вычитание

    def sub(self, other):
        pass

#умножение

    def mul(self, other):
        pass

#проверка равности

    def eq(self, other):
        return self.whole_part == other.whole_part and self.fractional_part == other.fractional_part

#сравнения

    def lt(self, other):
        pass

#результата

    def str(self):
        return f"{self.whole_part}.{self.fractional_part}"

fraction1 = Fractions(4, 30)
fraction2 = Fractions(4, 24)

sum_result = fraction1 + fraction2
print(f"Сумма: {sum_result}")

#2
class Деньги:
    def __init__(self, рубли, копейки):
        self.рубли = рубли
        self.копейки = копейки

    def __str__(self):
        return f"{self.рубли},{self.копейки:02d}"

    def __add__(self, other):
        сумма_в_копейках = self.рубли * 100 + self.копейки + other.рубли * 100 + other.копейки
        сумма_рубли = сумма_в_копейках // 100
        сумма_копейки = сумма_в_копейках % 100
        return Деньги(сумма_рубли, сумма_копейки)

    def __sub__(self, other):
        разность_в_копейках = self.рубли * 100 + self.копейки - other.рубли * 100 - other.копейки
        разность_рубли = разность_в_копейках // 100
        разность_копейки = разность_в_копейках % 100
        return Деньги(разность_рубли, разность_копейки)

    def __truediv__(self, other):
        делимая_в_копейках = self.рубли * 100 + self.копейки
        делитель_в_копейках = other.рубли * 100 + other.копейки
        результат_в_копейках = делимая_в_копейках / делитель_в_копейках
        результат_рубли = int(результат_в_копейках)
        результат_копейки = round((результат_в_копейках - результат_рубли) * 100)
        return Деньги(результат_рубли, результат_копейки)

    def __divmod__(self, other):
        делимая_в_копейках = self.рубли * 100 + self.копейки
        результат, остаток = divmod(делимая_в_копейках, other)
        результат_рубли = результат // 100
        результат_копейки = результат % 100
        return Деньги(результат_рубли, результат_копейки), остаток

    def __mul__(self, other):
        умножаемая_в_копейках = self.рубли * 100 + self.копейки
        результат_в_копейках = умножаемая_в_копейках * other
        результат_рубли = результат_в_копейках // 100
        результат_копейки = результат_в_копейках % 100
        return Деньги(результат_рубли, результат_копейки)

    def __eq__(self, other):
        return self.рубли == other.рубли and self.копейки == other.копейки

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.рубли < other.рубли or (self.рубли == other.рубли and self.копейки < other.копейки)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.рубли > other.рубли or (self.рубли == other.рубли and self.копейки > other.копейки)

    def __ge__(self, other):
        return self > other or self == other


# Проверка методов класса Деньги
a = Деньги(10, 50)
b = Деньги(5, 75)

# Сложение
c = a + b
print(c)  # Output: 16,25

# Вычитание
d = a - b
print(d)  # Output: 4,75

# Деление суммы на дробное число
e = a / 2
print(e)  # Output: 5,25

# Умножение на дробное число
f = a * 1.5
print(f)  # Output: 15,75

# Сравнение
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

#3
class РавнобочнаяТрапеция:
    def __init__(self, точка1, точка2, точка3, точка4):
        self.точка1 = точка1
        self.точка2 = точка2
        self.точка3 = точка3
        self.точка4 = точка4

    def является_равнобочной(self):
        сторона1 = self.расстояние(self.точка1, self.точка2)
        сторона2 = self.расстояние(self.точка2, self.точка3)
        сторона3 = self.расстояние(self.точка3, self.точка4)
        сторона4 = self.расстояние(self.точка4, self.точка1)
        return сторона1 == сторона3

    def длины_сторон(self):
        сторона1 = self.расстояние(self.точка1, self.точка2)
        сторона2 = self.расстояние(self.точка2, self.точка3)
        сторона3 = self.расстояние(self.точка3, self.точка4)
        сторона4 = self.расстояние(self.точка4, self.точка1)
        return сторона1, сторона2, сторона3, сторона4

    def периметр(self):
        сторона1, сторона2, сторона3, сторона4 = self.длины_сторон()
        return сторона1 + сторона2 + сторона3 + сторона4

    def площадь(self):
        сторона1, сторона2, сторона3, сторона4 = self.длины_сторон()
        полупериметр = self.периметр() / 2
        основание1 = сторона1 if сторона1 == сторона3 else сторона2
        высота = 2 * ((сторона2 ** 2) - ((основание1 ** 2) + (сторона2 ** 2) - (сторона4 ** 2))) ** 0.5 / (основание1 * 2)
        return основание1 * высота

    @staticmethod
    def расстояние(точка1, точка2):
        return ((точка2[0] - точка1[0]) ** 2 + (точка2[1] - точка1[1]) ** 2) ** 0.5


# Пример использования класса
трапеция1 = РавнобочнаяТрапеция((0, 0), (0, 3), (4, 3), (4, 0))
трапеция2 = РавнобочнаяТрапеция((0, 0), (0, 2), (3, 2), (3, 0))
трапеция3 = РавнобочнаяТрапеция((0, 0), (0, 5), (6, 5), (6, 0))
трапеции = [трапеция1, трапеция2, трапеция3]

сумма_площадей = sum(трапеция.площадь() for трапеция in трапеции)
средняя_площадь = сумма_площадей / len(трапеции)

количество_трапеций_превышающих_среднюю = sum(трапеция.площадь() > средняя_площадь for трапеция in трапеции)

print(f"Количество трапеций с площадью больше средней: {количество_трапеций_превышающих_среднюю}")

#4
class Строка:
    def __init__(self, строка):
        self.значение = len(строка.encode('utf-8'))

    def получить_длину(self):
        return self.значение

    def очистить(self):
        self.значение = 0

    def __del__(self):
        pass


class КомплексноеЧисло(Строка):
    def __init__(self, строка):
        super().__init__(строка)
        self.действительная_часть, self.мнимая_часть = self.извлечь_части(строка)

    def извлечь_части(self, строка):
        части = строка.split('i')
        if len(части) == 2:
            действительная_часть = self.проверить_часть(части[0])
            мнимая_часть = self.проверить_часть(части[1])
        else:
            действительная_часть = 0
            мнимая_часть = 0
        return действительная_часть, мнимая_часть

    def проверить_часть(self, часть):
        if (часть[0] == '+' or часть[0] == '-') and часть[1:].isdigit():
            return int(часть)
        elif часть.isdigit():
            return int(часть)
        else:
            return 0

    def проверка_на_равенство(self, другое_число):
        if isinstance(другое_число, КомплексноеЧисло):
            return self.действительная_часть == другое_число.действительная_часть and \
                   self.мнимая_часть == другое_число.мнимая_часть
        else:
            return False

    def сложение(self, другое_число):
        if isinstance(другое_число, КомплексноеЧисло):
            действительная_сумма = self.действительная_часть + другое_число.действительная_часть
            мнимая_сумма = self.мнимая_часть + другое_число.мнимая_часть
            return КомплексноеЧисло(str(действительная_сумма) + 'i' + str(мнимая_сумма))
        else:
            return КомплексноеЧисло("0i0")

    def умножение(self, другое_число):
        if isinstance(другое_число, КомплексноеЧисло):
            действительная_произведение = (self.действительная_часть * другое_число.действительная_часть) - \
                                         (self.мнимая_часть * другое_число.мнимая_часть)
            мнимая_произведение = (self.действительная_часть * другое_число.мнимая_часть) + \
                                   (другое_число.действительная_часть * self.мнимая_часть)
            return КомплексноеЧисло(str(действительная_произведение) + 'i' + str(мнимая_произведение))
        else:
            return КомплексноеЧисло("0i0")


строка1 = Строка("Hello")
строка2 = Строка("World")
комплекс1 = КомплексноеЧисло("2i5")
комплекс2 = КомплексноеЧисло("-3i7")

print(f"Длина строки 1: {строка1.получить_длину()}")
print(f"Длина строки 2: {строка2.получить_длину()}")

строка1.очистить()
print(f"Длина строки 1 после очистки: {строка1.получить_длину()}")

print(f"Комплексное число 1: {комплекс1.действительная_часть} + {комплекс1.мнимая_часть}i")
print(f"Комплексное число 2: {комплекс2.действительная_часть} + {комплекс2.мнимая_часть}i")

результат_равенства = комплекс1.проверка_на_равенство(комплекс2)
print(f"Результат проверки на равенство: {результат_равенства}")

сумма_чисел = комплекс1.сложение(комплекс2)
print(f"Сумма комплексных чисел: {сумма_чисел.действительная_часть} + {сумма_чисел.мнимая_часть}i")

произведение_чисел = комплекс1.умножение(комплекс2)
print(f"Произведение комплексных чисел: {произведение_чисел.действительная_часть} + {произведение_чисел.мнимая_часть}i")

#5