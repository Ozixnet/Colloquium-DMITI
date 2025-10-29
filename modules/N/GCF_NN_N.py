# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.MOD_NN_N import MOD_NN_N_f
from modules.N.COM_NN_D import COM_NN_D_f
from modules.N.NZER_N_B import NZER_N_B_f

def GCF_NN_N_f(a:NNum, b: NNum) ->NNum:
    """
    НОД натуральных чисел
    a - первое натуральное число.
    b - второе натуральное число.
    Возврат - NNum.
    """

    #COM_NN_D
    #Сравнение натуральных чисел: 2 - если первое больше второго; 0, если равно; 1 иначе.
    if(COM_NN_D_f(a,b) not in [0,2]):
        a, b = b, a

    # NZER_N_B
    # Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
    for i in [a,b]:
        if(NZER_N_B_f(i)=="нет"):
            raise ValueError("a или/и b == нулю (0)")

    GCF = NNum(1, [1])

    #MOD_NN_N
    #Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля).
    while(1):
        remainer = MOD_NN_N_f(a,b)
        if(NZER_N_B_f(remainer)=="нет"):
            GCF = b
            break
        a = b
        b = remainer

    return NNum(GCF.n, GCF.A)
