# Двойникова Валерия Алексеевна, гр. 4381

import pytest
from modules.Z.Z_NUM import ZNum
from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.N_NUM import NNum


# проверка функциональности модуля
def test_abs_z_n_normal_cases():
    result = ABS_Z_N_f(ZNum(1, NNum(3, [1, 2, 3])))
    assert result.A == [1, 2, 3]

    result = ABS_Z_N_f(ZNum(1, NNum(3, [4, 5, 6])))
    assert result.A == [4, 5, 6]


# тестирование на больших кейсах
def test_abs_z_n_large_number(): 
    big_num = ZNum(1, NNum(1000, [9] * 1000))
    result = ABS_Z_N_f(big_num)
    assert len(result.A) == 1000
    assert result.A == [9] * 1000
