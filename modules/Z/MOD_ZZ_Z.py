# Тарасов Юрий Романович, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.SUB_ZZ_Z import SUB_ZZ_Z_f
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.Z.DIV_ZZ_Z import DIV_ZZ_Z_f


def MOD_ZZ_Z_f(arg1: ZNum, arg2:ZNum)-> ZNum:
    """
    Остаток от деления целых чисел(делитель отличен от нуля)

    arg1 - первое целое число

    arg2 - делитель, целое число, не может быть 0

    Возврат - Znum
    """
    if arg2.n == 1 and arg2.A[0] == 0:
        raise ValueError("Ошибка. Делитель равен нулю")
    # если делимое является 0
    if arg1.n == 1 and arg1.A[0] == 0:
        return ZNum(0, NNum(1, [0]))
    # найдем частное от деления
    k = DIV_ZZ_Z_f(arg1, arg2)
    # умножим 2 аргумент на частное
    arg2 = MUL_ZZ_Z_f(arg2, k)
    # получаем и возвращаем остаток
    return SUB_ZZ_Z_f(arg1, arg2)


