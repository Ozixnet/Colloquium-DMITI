# Вакух Виктор Сергеевич, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.LCM_NN_N import LCM_NN_N_f
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f


def FAC_P_Q_f(poly: PNum) -> QNum:
    """
    Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей

    poly - многочлен.

    Возврат - рациональное число (НОД числителей / НОК знаменателей).
    """
    zero_rational = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))

    # если полином нулевой, возвращаем 1/1
    if poly.m == -1:
        return QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))
    # собираем все знаменатели в список
    denominators = []
    for i in range(poly.m + 1):
        denominators.append(poly.C[i].den_tor)
    # находим НОК всех знаменателей
    lcm_den = denominators[0]
    for i in range(1, len(denominators)):
        lcm_den = LCM_NN_N_f(lcm_den, denominators[i])
    # собираем все числители в список
    numerators = []
    for i in range(poly.m + 1):
        abs_num = ABS_Z_N_f(poly.C[i].num_tor)
        numerators.append(abs_num)
    # находим НОД всех числителей
    gcd_num = numerators[0]
    for i in range(1, len(numerators)):
        gcd_num = GCF_NN_N_f(gcd_num, numerators[i])
    # преобразуем НОД в целое число
    gcd_num_z = TRANS_N_Z_f(gcd_num)

    return QNum(gcd_num_z, lcm_den)