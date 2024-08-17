def number_to_word(number):
    digits = {
        0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
        5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }

    tens = {
        10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
        14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
        18: 'восемнадцать', 19: 'девятнадцать'
    }

    dozens = {
        2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят',
        6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'
    }

    hundreds = {
        1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
        5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'
    }

    def convert_below_100(number):
        if number < 10:
            return digits[number]
        elif number < 20:
            return tens[number]
        else:
            digit = digits[number % 10]
            dozen = dozens[number // 10]
        
            if digit == 'ноль':
                return dozen
            else:
                return f'{dozen} {digit}'

    def convert_below_1000(number):
        if number < 100:
            return convert_below_100(number)
        else:
            hundred = hundreds[number // 100]
            below_hundred = convert_below_100(number % 100)
        
            if below_hundred == 'ноль':
                return hundred
            else:
                return f'{hundred} {below_hundred}'

    if number < 1000:
        return convert_below_1000(number)

    if number >= 1000000:
        return 'Неверное число'  # Поддержка чисел до 999,999 (шестизначных)

    thousands_number = number // 1000
    thousands_word = convert_below_1000(thousands_number)
    remaining_number = number % 1000
    remaining_word = convert_below_1000(remaining_number)
    k = 'тысяч'

    if thousands_word[-4:] == 'один':
        thousands_word = thousands_word[0:-4] + 'одна'
        k = 'тысяча'
    elif thousands_word[-3:] == 'два':
        thousands_word = thousands_word[0:-3] + 'две'
        k = 'тысячи'
    elif thousands_word[-3:] == 'три':
        k = 'тысячи'
    elif thousands_word[-6:] == 'четыре':
        k = 'тысячи'
        

    return f'{thousands_word} {k} {remaining_word}'

def count_letters(word):
    # Убираем пробелы и тире в слове
    cleaned_word = word.replace(' ', '').replace('-', '')
    return len(cleaned_word)

c = 0
stroke = ""
cycles = []
means = []
stable_dots = []

def count_all(x):
    global c
    global stroke
    global cycles
    global stable_dots
    global means
    word = number_to_word(x)
    letter_count = count_letters(word)
    c += 1
    ##print(f' -> "{word}" -> {letter_count}')
    if (f' -> "{word}" -> {letter_count}') == stroke:
        stable_dots.append(word)
        for i in cycles:
            if i == letter_count:
                return 0
        cycles.append(letter_count)
        means.append(word)
        return 0
    if c > 20:
        for i in cycles:
            if i == letter_count:
                c = 0
                return 0
        cycles.append(letter_count)
        means.append(word)
        return 0
    stroke = f' -> "{word}" -> {letter_count}'
    count_all(letter_count)

for j in range(999999):
    number = j
    count_all(number)
print(means)
print(cycles)
print(stable_dots)
