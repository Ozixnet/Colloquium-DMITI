# Тарасов Юрий Романович, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.SUB_ZZ_Z import SUB_ZZ_Z_f
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.Z.DIV_ZZ_Z import DIV_ZZ_Z_f
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f


def MOD_ZZ_Z_f(arg1: ZNum, arg2: ZNum)-> ZNum:
    """
    Остаток от деления целых чисел(делитель отличен от нуля)

    arg1 - первое целое число

    arg2 - делитель, целое число, не может быть 0

    Возврат - Znum
    """
    if arg2.n == 1 and arg2.A[0] == 0:
        raise ValueError("Ошибка. Делитель равен нулю")
    if POZ_Z_D_f(arg1) == 1 and POZ_Z_D_f(arg2) == 1 or POZ_Z_D_f(arg1) != 1 and POZ_Z_D_f(arg2) == 1:
        arg1 = MUL_ZM_Z_f(arg1)
        arg2 = MUL_ZM_Z_f(arg2)
    # если делимое является 0
    if arg1.n == 1 and arg1.A[0] == 0:
        return ZNum(0, NNum(1, [0]))
    # найдем частное от деления
    k = DIV_ZZ_Z_f(arg1, arg2)
    # умножим 2 аргумент на частное
    arg2_s = arg2
    arg2 = MUL_ZZ_Z_f(arg2, k)
    res = SUB_ZZ_Z_f(arg1, arg2)
    if POZ_Z_D_f(res) == 1:
        arg2_s = MUL_ZM_Z_f(arg2_s)
        res = SUB_ZZ_Z_f(res, arg2_s)
    # получаем и возвращаем остаток
    return res


