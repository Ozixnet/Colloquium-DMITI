# Двойникова Валерия Алексеевна, гр. 4381

import pytest
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum


def test_for_valid_ZNum():
    # корректные случаи
    z1 = ZNum(0, NNum(3, [1, 2, 3]))  # +123
    assert z1.b == 0 and z1.n == 3 and z1.A == [1, 2, 3]

    z2 = ZNum(1, NNum(3, [4, 5, 6]))  # -456
    assert z2.b == 1 and z2.n == 3 and z2.A == [4, 5, 6]

    z3 = ZNum(0, NNum(1, [0]))  # +0
    assert z3.b == 0 and z3.n == 1 and z3.A == [0]

    # некорректные знаки
    with pytest.raises(ValueError):
        ZNum(2, NNum(1, [5]))  # недопустимый знак

    with pytest.raises(ValueError):
        ZNum(-1, NNum(1, [5]))  # недопустимый знак

    # некорректное натуральное число
    with pytest.raises(ValueError):
        ZNum(0, NNum(0, []))  # NNum сам выбросит ValueError

    with pytest.raises(ValueError):
        ZNum(1, NNum(3, [1, 2]))  # длина не совпадает

test_for_valid_ZNum()
