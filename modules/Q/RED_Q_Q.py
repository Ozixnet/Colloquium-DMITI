# Хведынич Варвара Андреевна, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.Z.DIV_ZZ_Z import DIV_ZZ_Z_f

def RED_Q_Q_f(fraction: QNum) -> QNum:
    """
    Сокращение дроби.
    
    fraction - дробь для сокращения
    
    Возвращает - QNum: сокращенная дробь
    """
    # Если числитель равен 0, возвращаем тот же ноль
    #if fraction.num_tor.A == [0]: Для однозначных воркает, а если бахнуть [0,0] то не будет
    #    return fraction
    if all(digit == 0 for digit in fraction.num_tor.A):
    
    # нод принимает два натуральных, в рац мы храним числитель как целый, 
    # поэтому сначала привод к натуральному. знам и так натуральным хранится
    #num_natural = NNum(fraction.num_tor.n, fraction.num_tor.A.copy())  # Ручкное копирование нафиг, если есть ABS_Z_N_f 
    num_natural = ABS_Z_N_f(fraction.num_tor) 
    gcf = GCF_NN_N_f(num_natural, fraction.den_tor)

    # деление числителя на нод
    new_numerator = DIV_ZZ_Z_f(fraction.num_tor, ZNum(0, gcf))
    
    # деление знаменателя на нод
    new_denominator = DIV_ZZ_Z_f(ZNum(0, fraction.den_tor), ZNum(0, gcf))
 
    denominator_natural = NNum(new_denominator.n, new_denominator.A)

    return QNum(new_numerator, denominator_natural)
