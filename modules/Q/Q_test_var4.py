# Ишамчурин Данил, гр. 4381

import pytest
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.Q_NUM import QNum

from modules.Q.INT_Q_B import INT_Q_B_f
from modules.Q.TRANS_Q_Z import TRANS_Z_Q_f
from modules.Q.TRANS_Z_Q import TRANS_Z_Q_f

# Функция проверки преобразования целого числа в дробное
def test_TRANS_Z_Q_f():
    num1 = ZNum(0, NNum(3, [3, 2, 1]))
    num2 = ZNum(1, NNum(4, [5, 1, 7, 2]))
    func1 = TRANS_Z_Q_f(num1)
    assert type(func1) == QNum and func1.num_tor.A == num1.A and func1.den_tor.A == [1]

# Функция проверки функции, которая проверяет сокращенное дробное на целое
def test_INT_Q_B_f():
    num1 = []

# Функция проверки преобразования дробного числа в целое
def test_TRANS_Q_Z_f():
    num1 = []

test_TRANS_Z_Q_f()