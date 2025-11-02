# Хведынич Варвара Андреевна, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f

def MUL_PQ_P_f(poly: PNum, number: QNum) -> PNum:
    """
    Умножение многочлена на рациональное число.
    
    poly - многочлен
    number - рациональное число
    
    Возвращает - PNum: многочлен, умноженный на число
    """
    # создание нулеового рац числа 
    zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))

    # если умножаем на ноль или полином нулевой изначально 
    # возвращаем нулевой полином 
    if number.num_tor.A == [0] or poly.m == -1:
        return PNum(-1, [zero_rational])
    
    result_coeffs = []

    # проход оп всем степеням и умножение коэффициентов. 
    # после возврат результата 
    for i in range(poly.m + 1):
        product_coeff = MUL_QQ_Q_f(poly.C[i], number)
        result_coeffs.append(product_coeff)
    
    return PNum(poly.m, result_coeffs)