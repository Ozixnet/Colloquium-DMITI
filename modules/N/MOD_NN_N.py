# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.N.NZER_N_B import NZER_N_B_f
from modules.N.COM_NN_D import COM_NN_D_f

def MOD_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля).
    a - первое натуральное число.
    b - второе натуральное число.
    Возврат - NNum.
        """

    #COM_NN_D
    #Сравнение натуральных чисел: 2 - если первое больше второго; 0, если равно; 1 иначе.
    if (COM_NN_D_f(a,b) not in [0,2]):
        a, b = b, a

    #NZER_N_B
    #Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
    if (NZER_N_B_f(b) == "нет"):
        raise ValueError("Делитель не должен быть равен нулю")

    # DIV_NN_N
    #Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
    quotient = DIV_NN_N_f(a, b)

    if (type(quotient) != NNum):
        raise TypeError("Неполное частное не является натуральным числом")

    # MUL_NN_N
    # Умножение натуральных чисел
    multi = MUL_NN_N_f(b,quotient)

    if (COM_NN_D_f(a,multi) not in [0,2]):
        raise ValueError("Теоретически невозможно, но а < b*q лол")

    # SUB_NN_N
    # Вычитание из первого большего натурального числа второго меньшего или равного
    remainder = SUB_NN_N_f(a,multi)

    return NNum(remainder.n, remainder.A)
