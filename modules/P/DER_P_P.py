# Хохряков Пётр, гр. 4381

from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum
from modules.Q.Q_NUM import QNum
from modules.P.P_NUM import PNum
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f

def DER_P_P_f(p : PNum)->PNum:
    """
    Производная многочлена

    p - многочлен (типа PNum)

    Возврат - PNum.
    """
    M = p.m
    if M in [-1,0]:
        return PNum(0,[QNum( ZNum(1, NNum(1, [0])), NNum(1, [1]))])

    #удаляем свободный член ввиду взятия производной
    p.C.pop(0)
    M -= 1
    for i in range(M):
        q = p.C[i]
        num = list(map(int,str(i+1)))[::-1]
        deg_of_preDer = QNum(ZNum(1,NNum(len(num),num)),NNum(1,[1])) #N->Q

        #MUL_QQ_Q
        #Умножение дробей
        p = MUL_QQ_Q_f(p,deg_of_preDer)

    p.m = M
    return p


