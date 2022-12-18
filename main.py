


def fun_m(mass):
    mass2 = []
    for i in mass:
        if len(i) <= 3:
            mass2.append(i)
    return mass2

print(fun_m(['wqeeq', '22', '232', 'ewewe', '1']))
