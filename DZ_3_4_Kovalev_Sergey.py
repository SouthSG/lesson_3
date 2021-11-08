def thesaurus_adv(*args):
    d = dict()
    for name in args:
        a0 = name.split()[1][0]
        a1 = name[0]
        if a0 not in d:
            d[a0] = dict()
        if a1 not in d[a0]:
            d[a0][a1] = []
        d[a0][a1].append(name)
    return d


print(thesaurus_adv('Иван Камарилья', 'Мария Тремер', \
                    'Петр Вентру', 'Илья Малкевиан', \
                    'Александр Тремер'))
