# Гайнутдинова Зарина, гр. 4381

import pytest
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f
from modules.Z.TRANS_N_Z import TRANS_N_Z_f
from modules.Z.TRANS_Z_N import TRANS_Z_N_f


# функция для проверки положительности числа
def test_POZ_Z_D_f():
    num1 = ZNum(1, NNum(4, [1, 2, 3, 4]))
    num2 = ZNum(0, NNum(1, [0]))
    num3 = ZNum(0, NNum(4, [1, 2, 3, 4]))
    assert POZ_Z_D_f(num1) == 1     # отрицательное => 1
    assert POZ_Z_D_f(num2) == 0     # 0 => 0
    assert POZ_Z_D_f(num3) == 2    # положительное => 2


# функция для проверки умножения на (-1)
def test_MUL_ZM_Z_f():
    num1 = ZNum(1, NNum(4, [1, 2, 3, 4]))
    num2 = ZNum(0, NNum(1, [0]))
    num3 = ZNum(0, NNum(4, [1, 2, 3, 4]))
    assert MUL_ZM_Z_f(num1).b == 0 and MUL_ZM_Z_f(num1).A == [1, 2, 3, 4]
    assert MUL_ZM_Z_f(num2).b == 0 and MUL_ZM_Z_f(num2).A == [0]
    assert MUL_ZM_Z_f(num3).b == 1 and MUL_ZM_Z_f(num3).A == [1, 2, 3, 4]


# функция для проверки преобразования натурального числа в целое
def test_TRANS_N_Z_f():
    num1 = TRANS_N_Z_f(NNum(5, [1, 2, 3, 4, 5]))
    num2 = TRANS_N_Z_f(NNum(1, [0]))
    assert type(num1) == ZNum and num1.b == 0 and num1.A == [1, 2, 3, 4, 5]
    assert type(num2) == ZNum and num2.b == 0 and num2.A == [0]


# функция для проверки преобразования целого числа в натуральное
def test_TRANS_Z_N_f():
    num1 = TRANS_Z_N_f(ZNum(0, NNum(5, [1, 2, 3, 4, 5])))
    num2 = TRANS_Z_N_f(ZNum(0, NNum(1, [0])))
    num11 = ZNum(1, NNum(3, [1, 2, 3]))

    assert type(num1) == NNum and num1.A == [1, 2, 3, 4, 5]
    assert type(num2) == NNum and num2.A == [0]

    with pytest.raises(Exception, match="Число должно быть неотрицательным"):
        TRANS_Z_N_f(num11)


test_POZ_Z_D_f()
test_MUL_ZM_Z_f()
test_TRANS_N_Z_f()
test_TRANS_Z_N_f()
