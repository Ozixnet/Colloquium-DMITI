# Хведынич Варвара Андреевна, гр. 4381

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Q.RED_Q_Q import RED_Q_Q_f


def create_rational(num: int, den: int) -> QNum:
    # Создает рациональное число
    num_natural = NNum(1, [abs(num)])
    num_z = ZNum(1 if num < 0 else 0, num_natural)
    den_natural = NNum(len(str(den)), [int(i) for i in str(den)][::-1])
    return QNum(num_z, den_natural)


def test_for_RED_Q_Q():
    # 4/6 -> 2/3
    fraction1 = create_rational(4, 6)
    result1 = RED_Q_Q_f(fraction1)
    assert result1.num_tor.A == [2]  
    assert result1.den_tor.A == [3]  

    # 8/12 -> 2/3
    fraction2 = create_rational(8, 12)
    result2 = RED_Q_Q_f(fraction2)
    assert result2.num_tor.A == [2]  
    assert result2.den_tor.A == [3]  

    # 0/7 -> 0/7 
    fraction3 = create_rational(0, 7)
    result3 = RED_Q_Q_f(fraction3)
    assert result3.num_tor.A == [0]

    # 7/1 -> 7/1
    fraction4 = create_rational(7, 1)
    result4 = RED_Q_Q_f(fraction4)
    assert result4.num_tor.A == [7]
    assert result4.den_tor.A == [1]


test_for_RED_Q_Q()