# Ишамчурин Данил, гр. 4381

import pytest
from modules.P.P_NUM import PNum
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f


# Функция проверки умножения многочлена на x^k
def test_MUL_Pxk_P_f():
    poly1 = PNum(3, [7, 2, 1, 1])
    poly2 = PNum(0, [1])
    poly3 = PNum(2, [0, 2, 1])
    poly4 = PNum(2, [1, 3, 1])
    assert MUL_Pxk_P_f(poly1, 5).m == 8 and MUL_Pxk_P_f(poly1, 5).C == [0, 0, 0, 0, 0, 7, 2, 1, 1]
    assert MUL_Pxk_P_f(poly2, 3).m == 3 and MUL_Pxk_P_f(poly2, 3).C == [0, 0, 0, 1]
    assert MUL_Pxk_P_f(poly3, 0).m == 2 and MUL_Pxk_P_f(poly3, 0).C == [0, 2 ,1]
    with pytest.raises(Exception, match="k отрицательное."):
        MUL_Pxk_P_f(poly4, -1)


test_MUL_Pxk_P_f()
