# Хохряков Пётр, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum

def LED_P_Q_f(p : PNum)->QNum:
    """
    Возвращает старший коэффициент многочлена

    p - многочлен (типа PNum)

    Возврат — QNum.
    """

    led_coef = p.C[-1]
    return led_coef