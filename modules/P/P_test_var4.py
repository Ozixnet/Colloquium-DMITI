# Ишамчурин Данил, гр. 4381

import pytest
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.P.P_NUM import PNum
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f


# Функция проверки умножения многочлена на x^k
def test_MUL_Pxk_P_f():
    poly1 = PNum(3, [QNum(ZNum(0, NNum(1, [7])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [2])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))])
    poly2 = PNum(0, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))])
    poly3 = PNum(2, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [2])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))])
    poly4 = PNum(2, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [3])), NNum(1, [1])),
                     QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))])
    assert (MUL_Pxk_P_f(poly1, 5).m == 8 and [q.num_tor.A[0] for q in MUL_Pxk_P_f(poly1, 5).C]
            == [0, 0, 0, 0, 0, 7, 2, 1, 1])
    assert MUL_Pxk_P_f(poly2, 3).m == 3 and [q.num_tor.A[0] for q in MUL_Pxk_P_f(poly2, 3).C] == [0, 0, 0, 1]
    assert MUL_Pxk_P_f(poly3, 0).m == 2 and [q.num_tor.A[0] for q in MUL_Pxk_P_f(poly3, 0).C] == [0, 2, 1]
    with pytest.raises(Exception, match="k отрицательное."):
        MUL_Pxk_P_f(poly4, -1)


test_MUL_Pxk_P_f()
