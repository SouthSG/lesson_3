def num_translate(eng):
    nums = {'zero': 'ноль', \
            'one': 'один', \
            'two': 'два', \
            'three': 'три', \
            'four': 'четыре', \
            'five': 'пять', \
            'six': 'шесть',
            'seven': 'семь', \
            'eight': 'восемь', \
            'nine': 'девять', \
            'ten': 'десять'}
    if eng[0].islower():
        return nums.get(eng.lower(), 'None').lower()
    else:
        return nums.get(eng.lower(), 'None').capitalize()


print(num_translate(input('Введите английское число для перевода: ')))
