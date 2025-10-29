# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.N.SUB_NDN_N import SUB_NDN_N_f
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
    if(COM_NN_D_f(a,b) not in [0,2]):
        a, b = b, a

    #NZER_N_B
    #Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
    if (NZER_N_B_f(b) == "нет"):
        raise ValueError("Делитель не должен быть равен нулю")

    # DIV_NN_N
    #Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
    quotient = DIV_NN_N_f(a, b)

    #SUB_NDN_N
    #Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
    remainder = SUB_NDN_N_f(a,b,quotient)

    return NNum(remainder.n, remainder.A)