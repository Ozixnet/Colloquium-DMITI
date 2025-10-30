
# Ишамчурин Данил Ильфирович, гр. 4381

from modules.P.P_NUM import PNum
from modules.N.N_NUM import NNum

def MUL_Pxk_P_f(poly: PNum, k: int) -> PNum:
    """
    Умножает многочлен на x^k

    poly - значение типа PNum

    Возврат - PNum
    """
    if type(k) == int and k >= 0:
        new_poly = [0]*k + poly.C
        return PNum(poly.m + k, new_poly)
    else:
        raise ValueError('k не 0 или не натуральное')
