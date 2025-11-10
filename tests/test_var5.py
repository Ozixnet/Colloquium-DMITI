# Хохряков Пётр, гр. 4381

import pytest
from modules.N.N_NUM import NNum
from modules.Z.Z_NUM import ZNum
from modules.Q.Q_NUM import QNum
from modules.P.P_NUM import PNum
from modules.P.DEG_P_N import DEG_P_N_f
from modules.P.DER_P_P import DER_P_P_f
from modules.P.LED_P_Q import LED_P_Q_f

def test_for_DEG_P_N():
    p1 = PNum(1,[QNum(ZNum(1,NNum(1,[1])),NNum(1,[1])),QNum(ZNum(1,NNum(1,[1])),NNum(1,[1]))])
    p2 = PNum(0,[QNum(ZNum(1, NNum(1, [5])), NNum(1, [1]))]) #5
    p3 = PNum(2,[QNum(ZNum(1,NNum(1,[1])),NNum(1,[1])),QNum(ZNum(1,NNum(1,[1])),NNum(1,[1])),QNum(ZNum(1,NNum(1,[2])),NNum(1,[1]))])
    p4 = PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))]) #0

    q = [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])),
         QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])),
         QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])),
         QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])),
         QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])),
         QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))
         ]
    # >=10 - двухзначное и более
    p5 = PNum(len(q)-1, q)
    # (11, [x^11 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1])
    d1 = DEG_P_N_f(p1)
    d2 = DEG_P_N_f(p2)
    d3 = DEG_P_N_f(p3)
    d4 = DEG_P_N_f(p4)
    d5 = DEG_P_N_f(p5)

    n1 = NNum(1, [1])
    n2 = NNum(1, [0])
    n3 = NNum(1, [2])
    n4 = NNum(1, [0])
    n5 = NNum(2, [1, 1])

    assert d1.n == n1.n #1
    assert d1.A == n1.A
    assert d2.n == n2.n #2
    assert d2.A == n2.A
    assert d3.n == n3.n #3
    assert d3.A == n3.A
    assert d4.n == n4.n #4
    assert d4.A == n4.A
    assert d5.n == n5.n #5
    assert d5.A == n5.A



def test_for_DER_P_P():
    # Тест 1: Производная от (x + 1) должна быть 1
    p1 = PNum(1, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))]) # x + 1
    result1 = DER_P_P_f(p1)
    expected1 = PNum(0, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))]) # 1
    assert result1.m == expected1.m
    assert len(result1.C) == len(expected1.C)
    for i in range(len(result1.C)):
        assert result1.C[i].num_tor.A == expected1.C[i].num_tor.A
        assert result1.C[i].den_tor.A == expected1.C[i].den_tor.A

    # Тест 2: Производная от константы 5 должна быть 0
    p2 = PNum(0, [QNum(ZNum(0, NNum(1, [5])), NNum(1, [1]))]) # 5
    result2 = DER_P_P_f(p2)
    expected2 = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))]) # 0
    assert result2.m == expected2.m
    assert len(result2.C) == len(expected2.C)
    assert result2.C[0].num_tor.A == expected2.C[0].num_tor.A
    assert result2.C[0].den_tor.A == expected2.C[0].den_tor.A

    # Тест 3: Производная от (2x^2 + x + 1) должна быть (4x + 1)
    p3 = PNum(2, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])),
                QNum(ZNum(0, NNum(1, [2])), NNum(1, [1]))]) # 2x^2 + x + 1
    result3 = DER_P_P_f(p3)
    expected3 = PNum(1, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [4])), NNum(1, [1]))]) # 4x + 1
    assert result3.m == expected3.m
    assert len(result3.C) == len(expected3.C)
    for i in range(len(result3.C)):
        assert result3.C[i].num_tor.A == expected3.C[i].num_tor.A
        assert result3.C[i].den_tor.A == expected3.C[i].den_tor.A

    # Тест 4: Производная от 0 должна быть 0
    p4 = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))]) # 0
    result4 = DER_P_P_f(p4)
    expected4 = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))]) # 0
    assert result4.m == expected4.m
    assert len(result4.C) == len(expected4.C)
    assert result4.C[0].num_tor.A == expected4.C[0].num_tor.A
    assert result4.C[0].den_tor.A == expected4.C[0].den_tor.A


def test_for_LED_P_Q():
    p1 = PNum(1, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))])
    p2 = PNum(0, [QNum(ZNum(1, NNum(1, [5])), NNum(1, [1]))])
    p3 = PNum(2, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [2])), NNum(1, [1]))])
    p4 = PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))])

    assert LED_P_Q_f(p1) == p1.C[-1]
    assert LED_P_Q_f(p2) == p2.C[-1]
    assert LED_P_Q_f(p3) == p3.C[-1]
    assert LED_P_Q_f(p4) == p4.C[-1]

# Запуски функций
test_for_DEG_P_N()
test_for_DER_P_P()
test_for_LED_P_Q()