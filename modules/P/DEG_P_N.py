# Хохряков Пётр, гр. 4381

from modules.P.P_NUM import PNum
from modules.N.N_NUM import NNum


def DEG_P_N_f(p : PNum)->NNum:
    """
    Возвращает степень многочлена

    p - многочлен (типа PNum)

    Возврат - NNum.
    """
    if p.m in [-1,0] and p.C[0].num_tor.A[-1] >= 0:
        return NNum(1,[0])

    N = list(map(int,str(p.m)))[::-1]
    return NNum(len(N), N)