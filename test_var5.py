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
    assert DEG_P_N_f(p1) == 1
    assert DEG_P_N_f(p2) == 0
    assert DEG_P_N_f(p3) == 2
    assert DEG_P_N_f(p4) == 0


def test_for_DER_P_P():
    p1 = PNum(1, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))]) # x + 1
    p2 = PNum(0, [QNum(ZNum(1, NNum(1, [5])), NNum(1, [1]))]) # 5
    p3 = PNum(2, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), \
    QNum(ZNum(1, NNum(1, [2])), NNum(1, [1]))]) # 2x^2 + x + 1
    p4 = PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))]) # 0
    assert DER_P_P_f(p1) == PNum(0, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))])
    assert DER_P_P_f(p2) == PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))])
    assert DER_P_P_f(p3) == PNum(1, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [4])), NNum(1, [1]))])
    assert DER_P_P_f(p4) == PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))])


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