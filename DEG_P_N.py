# Хохряков Пётр, гр. 4381

from modules.P.P_NUM import PNum


def DEG_P_N_f(p : PNum)->int:
    """
    Возвращает степень многочлена

    p - многочлен (типа PNum)

    Возврат - int.
    """

    deg_of_poly = p.m
    return deg_of_poly