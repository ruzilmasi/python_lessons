def num_translate_adv(num):
    for key, value in dict.items():
        if num == key.capitalize():
            print(value.capitalize())
        if num == key:
            print(value)


dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
num_translate_adv('Ten')