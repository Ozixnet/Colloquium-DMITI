# Ишамчурин Данил Ильфирович, гр. 4381

import pytest
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum


def test_for_QNum():
    # Обычные примеры
    num1 = QNum(ZNum(0, NNum(2, [7, 6])), NNum(3, [6, 2, 6]))
    assert num1.num_tor.A == [7, 6] and num1.den_tor.A == [6, 2, 6] # дробь 67/626

    num2 = QNum(ZNum(1, NNum(3, [1, 0, 7])), NNum(1, [8]))
    assert num2.num_tor.A == [1, 0, 7] and num2.den_tor.A == [8] # дробь -701/8

    num3 = QNum(ZNum(0, NNum(1, [1])), NNum(4, [3, 3, 3, 3]))
    assert num3.num_tor.A == [1] and num3.den_tor.A == [3, 3, 3, 3] # дробь 1/3333

    # Обработка исключения
    with pytest.raises(ValueError):
        QNum(ZNum(0, NNum(3, [2, 2, 2])), NNum(1, [0])) # дробь 222/0 => ошибка: деление на 0

    with pytest.raises(ValueError):
        QNum(ZNum(1, NNum(2, [99])), NNum(1, [0])) # дробь -99/0 => ошибка: деление на 0


test_for_QNum()