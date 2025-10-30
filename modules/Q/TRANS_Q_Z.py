# Ишамчурин Данил Ильфирович, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

def TRANS_Q_Z_f(num: QNum) -> ZNum:
    """
    Преобразует дробное число в целое

    num - значение типа QNum

    Возврат - ZNum
    """
    if num.den_tor.n == 1 and num.den_tor.A[0] == 1:
        return ZNum(num.num_tor.b, NNum(num.num_tor.n, num.num_tor.A))
    else:
        raise ValueError("Знаменатель не равен 1")
