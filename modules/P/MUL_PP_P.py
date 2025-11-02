# Вакух Виктор Сергеевич, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.P.MUL_PQ_P import MUL_PQ_P_f
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
from modules.P.ADD_PP_P import ADD_PP_P_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


def MUL_PP_P_f(poly1: PNum, poly2: PNum) -> PNum:
    """
    Умножение многочленов

    poly1, poly2 - многочлены для умножения
    Возврат - произведение многочленов
    """
    zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))

    # если один из многочленов нулевой, возвращаем нулевой многочлен
    if poly1.m == -1 or poly2.m == -1:
        return PNum(-1, [zero_rational])
    result_poly = PNum(-1, [zero_rational])
    # проходим по всем степеням первого многочлена
    for i in range(poly1.m + 1):
        # проходим по всем степеням второго многочлена
        for j in range(poly2.m + 1):
            # умножаем коэффициенты при текущих степенях
            coeff_product = MUL_QQ_Q_f(poly1.C[i], poly2.C[j])
            # создаем многочлен с одним коэффициентом
            single_term = PNum(0, [coeff_product])
            # умножаем на x^(i+j) - сдвигаем степень
            shifted_term = MUL_Pxk_P_f(single_term, i + j)
            result_poly = ADD_PP_P_f(result_poly, shifted_term)

    return result_poly