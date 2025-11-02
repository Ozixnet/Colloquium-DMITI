# Вакух Виктор Сергеевич, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.P.FAC_P_Q import FAC_P_Q_f
from modules.P.MUL_PP_P import MUL_PP_P_f

def create_rational(num: int, den: int = 1) -> QNum:
    """
    Создает рациональное число вида num/den
    """
    num_natural = NNum(1, [abs(num)])
    num_z = ZNum(1 if num < 0 else 0, num_natural)
    den_natural = NNum(1, [abs(den)])
    return QNum(num_z, den_natural)


def test_for_FAC_P_Q():
    poly1 = PNum(1, [
        create_rational(4, 5),  # свободный член 4/5
        create_rational(2, 3)  # коэффициент при x: 2/3
    ])
    result1 = FAC_P_Q_f(poly1)
    assert result1.num_tor.A == [2]  # НОД числителей = 2
    assert result1.den_tor.A == [5, 1]  # НОК знаменателей = 15

    poly2 = PNum(2, [
        create_rational(12, 8),  # 12/8
        create_rational(9, 6),  # 9/6
        create_rational(6, 4)  # 6/4
    ])
    result2 = FAC_P_Q_f(poly2)
    assert result2.num_tor.A == [3]  # НОД числителей = 3
    assert result2.den_tor.A == [4, 2]  # НОК знаменателей = 24

    poly3 = PNum(1, [
        create_rational(4, 7),
        create_rational(2, 7)
    ])
    result3 = FAC_P_Q_f(poly3)
    assert result3.num_tor.A == [2]  # НОД = 2
    assert result3.den_tor.A == [7]  # НОК = 7

    # Нулевой полином - должен вернуть 1/1
    zero_poly = PNum(-1, [create_rational(0)])
    result4 = FAC_P_Q_f(zero_poly)
    assert result4.num_tor.A == [1]  # числитель = 1
    assert result4.den_tor.A == [1]  # знаменатель = 1

def test_for_MUL_PP_P():
    # (x + 1) * (x + 2) = x^2 + 3x + 2
    poly1 = PNum(1, [create_rational(1), create_rational(1)])
    poly2 = PNum(1, [create_rational(2), create_rational(1)])
    result1 = MUL_PP_P_f(poly1, poly2)
    assert result1.m == 2
    assert result1.C[0].num_tor.A == [2]
    assert result1.C[1].num_tor.A == [3]
    assert result1.C[2].num_tor.A == [1]

    # (2x + 3) * (x - 1) = 2x^2 + x - 3
    poly3 = PNum(1, [create_rational(3), create_rational(2)])
    poly4 = PNum(1, [create_rational(-1), create_rational(1)])
    result2 = MUL_PP_P_f(poly3, poly4)
    assert result2.m == 2
    assert result2.C[0].num_tor.A == [3] and result2.C[0].num_tor.b == 1
    assert result2.C[1].num_tor.A == [1]
    assert result2.C[2].num_tor.A == [2]

    # (x^2 + 1) * (x + 1) = x^3 + x^2 + x + 1
    poly5 = PNum(2, [create_rational(1), create_rational(0), create_rational(1)])
    poly6 = PNum(1, [create_rational(1), create_rational(1)])
    result3 = MUL_PP_P_f(poly5, poly6)
    assert result3.m == 3
    assert result3.C[0].num_tor.A == [1]
    assert result3.C[1].num_tor.A == [1]
    assert result3.C[2].num_tor.A == [1]
    assert result3.C[3].num_tor.A == [1]

    # Умножение на нулевой полином = нулевой полином
    zero_poly = PNum(-1, [create_rational(0)])
    result4 = MUL_PP_P_f(poly1, zero_poly)
    assert result4.m == -1

    # Умножение нулевого полинома на ненулевой = нулевой полином
    result5 = MUL_PP_P_f(zero_poly, poly2)
    assert result5.m == -1

    # Умножение на константу: (2) * (x + 1) = 2x + 2
    const_poly = PNum(0, [create_rational(2)])
    result6 = MUL_PP_P_f(const_poly, poly1)
    assert result6.m == 1
    assert result6.C[0].num_tor.A == [2]
    assert result6.C[1].num_tor.A == [2]

test_for_FAC_P_Q()
test_for_MUL_PP_P()