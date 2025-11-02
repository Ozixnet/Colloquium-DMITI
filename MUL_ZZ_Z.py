from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.POZ_Z_D import POZ_Z_D
from modules.N.ABS_Z_N import ABS_Z_N
from modules.Z.MUL_ZM_Z import MUL_ZM_Z
from modules.N.MUL_NN_N import MUL_NN_N


# Тарасов Юрий Романович, гр. 4381
def MUL_ZZ_Z(arg1: ZNum, arg2:ZNum)-> ZNum:
    """
        Умножение целых чисел
        arg1 - первое целое число
        arg2 - второе целое число
        Возврат - Znum
        """
    # получение знаков чисел
    flag1, flag2 = POZ_Z_D(arg1), POZ_Z_D(arg2)
    # получение модулей чисел
    marg1, marg2 = ABS_Z_N(arg1), ABS_Z_N(arg2)
    # получаем произведение модулей
    res = MUL_NN_N(marg1, marg2)
    # если одно из чисел 0
    if flag1 == 0 or flag2 == 0:
        return ZNum(0, NNum(1, [0]))
    # если оба числа с одинаковым знаком
    if flag1 == flag2:
        return ZNum(0, res)
    # знаки не сходятся -> число отрицательное
    else:
        return MUL_ZM_Z(ZNum(0, res))
