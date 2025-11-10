# Гайнутдинова Зарина, гр. 4381
from modules.P.NMR_P_P import NMR_P_P_f
from modules.P.GCF_PP_P import GCF_PP_P_f
from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

# функция проверки нахождения нода
def test_GCF_PP_P():
    zero_poly = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
    other_poly = PNum(1, [QNum(ZNum(0, NNum(2, [2, 3])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [3])), NNum(1, [1]))])

    # для одного нулевого многочлена
    gcf1 = GCF_PP_P_f(other_poly, zero_poly)
    gcf2 = GCF_PP_P_f(zero_poly, other_poly)
    assert gcf1.m == 1 and gcf1.C[0].num_tor.A == [2, 3] and gcf1.C[1].num_tor.A == [3]
    assert gcf2.m == 1 and gcf2.C[0].num_tor.A == [2, 3] and gcf2.C[1].num_tor.A == [3]

    # для двух нулевых многочленов
    gcf3 = GCF_PP_P_f(zero_poly, zero_poly)
    assert gcf3.m == -1 and gcf3.C[0].num_tor.A == [0]

    # для обычных случаев

    # x^3 - 3x^2 + 2x
    k0 = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))
    k1 = QNum(ZNum(0, NNum(1, [2])), NNum(1, [1]))
    k2 = QNum(ZNum(1, NNum(1, [3])), NNum(1, [1]))
    k3 = QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))
    poly1 = PNum(3, [k0, k1, k2, k3])

    # x^2 - x - 2
    k0 = QNum(ZNum(1, NNum(1, [2])), NNum(1, [1]))
    k1 = QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))
    k2 = QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))
    poly2 = PNum(2, [k0, k1, k2])

    # x - 2 (поскольку полином не нормируется внутри функции, результат - 4x - 8, что то же самое)
    gcf4 = GCF_PP_P_f(poly1, poly2)
    assert gcf4.m == 1
    assert gcf4.C[0].num_tor.A == [8] and gcf4.C[1].num_tor.A == [4] and gcf4.C[0].num_tor.b == 1 and gcf4.C[0].num_tor.b == 1
    assert gcf4.C[0].den_tor.A == [1] and gcf4.C[1].den_tor.A == [1]


def test_NMR_P_P():
    # Коэффициенты от младшей степени к старшей:
    # -8, 12, -6, 1

    k0 = QNum(ZNum(1, NNum(1, [8])), NNum(1, [1]))  # -8/1 = -8
    k1 = QNum(ZNum(0, NNum(2, [2, 1])), NNum(1, [1]))  # 12/1 = 12
    k2 = QNum(ZNum(1, NNum(1, [6])), NNum(1, [1]))  # -6/1 = -6
    k3 = QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))  # 1/1 = 1

    poly = PNum(3, [k0, k1, k2, k3])

    # x - 2 (поскольку полиномы не нормируются внутри функции, результат - (1/3x - 6/9) = (1/3x - 2/3) = x -2)
    res = NMR_P_P_f(poly)
    assert res.C[0].num_tor.A == [6] and res.C[0].num_tor.b == 1 and res.C[0].den_tor.A == [9]
    assert res.C[1].num_tor.A == [1] and res.C[1].num_tor.b == 0 and res.C[1].den_tor.A == [3]
    assert res.m == 1
