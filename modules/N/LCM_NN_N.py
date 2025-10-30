# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.COM_NN_D import COM_NN_D_f
from modules.N.NZER_N_B import NZER_N_B_f
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.N.MUL_NDN_N import MUL_NN_N_f
from modules.N.DIV_NN_N import DIV_NN_N_f

def LCM_NN_N_f(a : NNum, b : NNum) -> NNum:
    """
    НОК натуральных чисел
    a - первое натуральное число.
    b - второе натуральное число.
    Возврат - NNum.
    """

    # COM_NN_D
    # Сравнение натуральных чисел: 2 - если первое больше второго; 0, если равно; 1 иначе.
    if (COM_NN_D_f(a, b) not in [0, 2]):
        a, b = b, a

    # NZER_N_B
    # Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
    for i in [a, b]:
        if (NZER_N_B_f(i) == "нет"):
            raise ValueError("a или/и b == нулю (0)")

    # GCF_NN_N
    # НОД натуральных чисел
    GCF = GCF_NN_N_f(a,b)

    #MUL_NN_N
    #Умножение натуральных чисел
    MUL = MUL_NN_N_f(a,b)

    #DIV_NN_N
    #Неполное частное от деления первого натурального числа на второе (делитель отличен от нуля)
    LCM = DIV_NN_N_f(MUL,GCF)

    return NNum(LCM.n,LCM.A)
