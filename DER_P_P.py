# Хохряков Пётр, гр. 4381

from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum
from modules.Q.Q_NUM import QNum
from modules.P.P_NUM import PNum
from modules.Q.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f

def DER_P_P_f(p : PNum)->PNum:
    """
    Производная многочлена

    p - многочлен (типа PNum)

    Возврат - PNum.
    """
    M = p.m
    if M == 0:
        return PNum(0,[QNum( ZNum(1, NNum(1, [0])), NNum(1, [1]))])

    #удаляем свободный член ввиду взятия производной
    p.C.pop(0)
    M -= 1
    for i in range(M):
        q = p.C[i]
        num = str(i+1).split()[::-1]
        deg_of_preDer = NNum(len(num),num)

        # TRANS_N_Z
        # Преобразование натурального (степени члена) в целое
        deg_of_preDer = TRANS_N_Z_f(deg_of_preDer)

        #MUL_ZZ_Z
        #Умножение целых чисел
        q.num_tor = MUL_ZZ_Z_f(q.num_tor, deg_of_preDer)
    p.m = M
    return p


