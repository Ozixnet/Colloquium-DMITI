# Ишамчурин Данил Ильфирович, гр. 4381

from modules.P.P_NUM import PNum

def MUL_Pxk_P_f(poly: PNum, k: int) -> PNum:
    """
    Умножает многочлен на x^k

    poly - значение типа PNum.

    Возврат - PNum.
    """
    if k >= 0:
        zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))
        new_poly = [zero_rational] * k + poly.C
        return PNum(poly.m + k, new_poly)
    else:
        raise ValueError('k отрицательное.')
