# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from module.N.NZER_N_B import NZER_N_B_f
from module.N.MUL_NN_N import MUL_NN_N_f

def MOD_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля).
    a - первое натуральное число.
    b - второе натуральное число.
    Возврат - NNum.
    """

    #NZER_N_B
    #Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
    if (NZER_N_B_f(b) == "нет"):
        raise ValueError("Делитель не должен быть равен нулю")

    # DIV_NN_N
    #Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
    quotient = DIV_NN_N_f(a, b)

    if type(quotient) != NNum:
        raise TypeError("Неполное частное не является натуральным числом")

    # MUL_NN_N
    # Умножение натуральных чисел
    multi = MUL_NN_N_f(b,quotient)

    # SUB_NN_N
    # Вычитание из первого большего натурального числа второго меньшего или равного
    remainder = SUB_NN_N_f(a, multi)


    return NNum(remainder.n, remainder.A)

