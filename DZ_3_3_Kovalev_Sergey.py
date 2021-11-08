def thesaurus(names):
    names_dict = {}
    for name in names:
        first = name[0]
        if names_dict.get(first):
            names_dict[first].append(name)
        else:
            names_dict.setdefault(first, [name])
    return names_dict


list = ('Иван', 'Мария', 'Петр', 'Илья')
name_list = thesaurus(list)
print(name_list)
