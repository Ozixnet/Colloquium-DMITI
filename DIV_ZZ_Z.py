from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import Nnum
from modules.Z.POZ_Z_D import POZ_Z_D
from modules.N.ABS_Z_N import ABS_Z_N
from modules.N.DIV_N_N import DIV_N_N
from modules.Z.MUL_ZM_Z import MUL_ZM_Z


# Тарасов Юрий Романович, гр. 4381
def DIZ_ZZ_Z(arg1: ZNum, arg2:ZNum)-> ZNum:
    """
            Частное от деления целого на целое(делитель отличен от нуля)
            arg1 - первое целое число
            arg2 - делитель, целое число, не может быть 0
            Возврат - Znum
            """
    if arg2 == ZNum(0, Nnum(1, [0])):
        raise ValueError("ОШИБКА: Делитель должен быть отличен от нуля")
    # если делимое является 0
    if arg1 == ZNum(0, Nnum(1, [0])):
        return ZNum(0, Nnum(1, [0]))
    # получаем знаки двух чисел
    flag1, flag2 = POZ_Z_D(arg1), POZ_Z_D(arg2)
    # получаем абсолютное значение двух чисел
    marg1, marg2 = ABS_Z_N(arg1), ABS_Z_N(arg2)
    # получаем модуль частное от деления
    res = DIV_N_N(marg1, marg2)
    # сравниваем флаги
    # если == -> положительный znum
    if flag1 == flag2:
        return ZNum(0, res)
    # если != то -> отрицательное целое
    else:
        return MUL_ZM_Z(res)
