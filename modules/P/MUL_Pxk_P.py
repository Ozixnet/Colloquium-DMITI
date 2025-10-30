# Ишамчурин Данил Ильфирович, гр. 4381

from modules.P.P_NUM import PNum
from modules.N.N_NUM import NNum

def MUL_Pxk_P_f(poly: PNum, k: NNum) -> PNum:
    """
    Умножает многочлен на x^k

    poly - значение типа PNum

    Возврат - PNum
    """
    new_poly = [0]*k + poly.C
    return PNum(poly.m + k, new_poly)