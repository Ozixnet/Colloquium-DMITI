# Ишамчурин Данил Ильфирович, гр. 4381

import pytest
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.Q_NUM import QNum
from modules.Q.INT_Q_B import INT_Q_B_f
from modules.Q.TRANS_Q_Z import TRANS_Q_Z_f
from modules.Q.TRANS_Z_Q import TRANS_Z_Q_f


# Функция проверки преобразования целого числа в дробное
def test_TRANS_Z_Q_f():
    num1 = ZNum(0, NNum(3, [3, 2, 1]))
    num2 = ZNum(1, NNum(4, [5, 1, 7, 2]))
    func1 = TRANS_Z_Q_f(num1)
    func2 = TRANS_Z_Q_f(num2)
    assert type(func1) == QNum and func1.num_tor.A == num1.A and func1.den_tor.A == [1]
    assert type(func2) == QNum and func2.num_tor.A == num2.A and func2.den_tor.A == [1]


# Функция проверки функции, которая проверяет сокращенное дробное на целое
def test_INT_Q_B_f():
    num1 = QNum(ZNum(0, NNum(3, [4, 1, 5])), NNum(1, [1]))
    num2 = QNum(ZNum(1, NNum(4, [1, 1, 5, 5])), NNum(1, [1]))
    assert INT_Q_B_f(num1) == 'да'
    assert INT_Q_B_f(num2) == 'да'


# Функция проверки преобразования дробного числа в целое
def test_TRANS_Q_Z_f():
    num1 = QNum(ZNum(1, NNum(3, [5, 0, 2])), NNum(1, [1]))
    num2 = QNum(ZNum(0, NNum(2, [9, 9])), NNum(2, [1, 3]))
    func1 = TRANS_Q_Z_f(num1)
    assert type(func1) == ZNum and func1.A == num1.num_tor.A
    with pytest.raises(Exception, match="Знаменатель не равен 1."):
        TRANS_Q_Z_f(num2)


test_TRANS_Z_Q_f()
test_INT_Q_B_f()
test_TRANS_Q_Z_f()