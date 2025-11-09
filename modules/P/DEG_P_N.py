# Хохряков Пётр, гр. 4381

from modules.P.P_NUM import PNum


def DEG_P_N_f(p : PNum)->int:
    """
    Возвращает степень многочлена

    p - многочлен (типа PNum)

    Возврат - int.
    """
    if p.m in [-1,0] and p.C[0].num_tor.A[-1] >= 0:
        return 0

    else:
        return p.m