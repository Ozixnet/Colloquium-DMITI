# Двойникова Валерия Алексеевна, гр. 4381.

from modules.N.N_NUM import NNum

def ADD_1N_N_f(num: NNum) -> NNum:
    """
    Функция добавления 1 к натуральному числу
    num — экземпляр класса NNum (натуральное число)
    Возвращает новый экземпляр NNum
    """
    carry = 1

    for i in range(len(a)):
        a[i] += carry
        if a[i] < 10:
            carry = 0
            break
        a[i] = 0

    if carry:
        a.append(1)

    a.reverse()
    return NNum(len(a), a)