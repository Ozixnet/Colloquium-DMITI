# Ишамчурин Данил Ильфирович, гр. 4381

import pytest
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.Q_NUM import QNum
from modules.Q.ADD_QQ_Q import ADD_QQ_Q_f
from modules.Q.SUB_QQ_Q import SUB_QQ_Q_f
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f


# Функция проверки сложения дробей
def test_ADD_QQ_Q_f():
    num1 = QNum(ZNum(0, NNum(1, [7])), NNum(1, [2]))
    num2 = QNum(ZNum(1, NNum(1, [3])), NNum(1, [5]))
    func1 = ADD_QQ_Q_f(num1, num2)
    assert func1.num_tor.A == [9, 2] and func1.den_tor.A == [0, 1] and func1.num_tor.b == 0

# Функция проверки вычитания дроби из дроби
def test_SUB_QQ_Q_f():
    num1 = QNum(ZNum(1, NNum(1, [7])), NNum(1, [2]))
    num2 = QNum(ZNum(1, NNum(1, [3])), NNum(1, [5]))
    func1 = SUB_QQ_Q_f(num1, num2)
    assert func1.num_tor.A == [9, 2] and func1.den_tor.A == [0, 1] and func1.num_tor.b == 1

# Функция проверки деления дробей
def test_DIV_QQ_Q_f():
    num1 = QNum(ZNum(0, NNum(1, [7])), NNum(1, [2]))
    num2 = QNum(ZNum(1, NNum(1, [3])), NNum(1, [5]))
    func1 = DIV_QQ_Q_f(num1, num2)
    assert func1.num_tor.A == [5, 3] and func1.den_tor.A == [6] and func1.num_tor.b == 1


# Функция проверки умножения дробей
def test_MUL_QQ_Q_f():
    num1 = QNum(ZNum(0, NNum(1, [6])), NNum(1, [5]))
    num2 = QNum(ZNum(0, NNum(1, [4])), NNum(1, [5]))
    func1 = MUL_QQ_Q_f(num1, num2)
    assert func1.num_tor.A == [4, 2] and func1.den_tor.A == [5, 2] and func1.num_tor.b == 0



test_MUL_QQ_Q_f()
test_DIV_QQ_Q_f()
test_SUB_QQ_Q_f()
test_ADD_QQ_Q_f()
