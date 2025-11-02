# Вакух Виктор Сергеевич, гр. 4381

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f
from modules.Z.SUB_ZZ_Z import SUB_ZZ_Z_f
import pytest


def test_for_ADD_ZZ_Z():
    # Случай 1: Оба положительные
    result = ADD_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(0, NNum(2, [3, 2])))  # 15 + 23 = 38
    assert result.b == 0 and result.n == 2 and result.A == [8, 3]

    # Случай 2: Оба отрицательные
    result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(1, NNum(2, [3, 2])))  # -15 + (-23) = -38
    assert result.b == 1 and result.n == 2 and result.A == [8, 3]

    # Случай 3: Первое положительное, второе отрицательное (|a| > |b|)
    result = ADD_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(1, NNum(1, [3])))  # 15 + (-3) = 12
    assert result.b == 0 and result.n == 2 and result.A == [2, 1]

    # Случай 4: Первое положительное, второе отрицательное (|a| < |b|)
    result = ADD_ZZ_Z_f(ZNum(0, NNum(1, [3])), ZNum(1, NNum(2, [5, 1])))  # 3 + (-15) = -12
    assert result.b == 1 and result.n == 2 and result.A == [2, 1]

    # Случай 5: Первое положительное, второе отрицательное (|a| = |b|)
    result = ADD_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(1, NNum(2, [5, 1])))  # 15 + (-15) = 0
    assert result.b == 0 and result.n == 1 and result.A == [0]

    # Случай 6: Первое отрицательное, второе положительное (|a| > |b|)
    result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(0, NNum(1, [3])))  # -15 + 3 = -12
    assert result.b == 1 and result.n == 2 and result.A == [2, 1]

    # Случай 7: Первое отрицательное, второе положительное (|a| < |b|)
    result = ADD_ZZ_Z_f(ZNum(1, NNum(1, [3])), ZNum(0, NNum(2, [5, 1])))  # -3 + 15 = 12
    assert result.b == 0 and result.n == 2 and result.A == [2, 1]

    # Случай 8: Первое отрицательное, второе положительное (|a| = |b|)
    result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(0, NNum(2, [5, 1])))  # -15 + 15 = 0
    assert result.b == 0 and result.n == 1 and result.A == [0]

    # Случай 9: С нулем (первое число ноль)
    zero = ZNum(0, NNum(1, [0]))
    result = ADD_ZZ_Z_f(zero, ZNum(0, NNum(2, [3, 2])))  # 0 + 23 = 23
    assert result.b == 0 and result.n == 2 and result.A == [3, 2]

    # Случай 10: С нулем (второе число ноль)
    result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), zero)  # -15 + 0 = -15
    assert result.b == 1 and result.n == 2 and result.A == [5, 1]

    # Случай 11: Оба нуля
    result = ADD_ZZ_Z_f(zero, zero)  # 0 + 0 = 0
    assert result.b == 0 and result.n == 1 and result.A == [0]

    # Случай 12: Большие числа
    result = ADD_ZZ_Z_f(ZNum(0, NNum(3, [0, 0, 1])), ZNum(0, NNum(3, [0, 0, 1])))  # 100 + 100 = 200
    assert result.b == 0 and result.n == 3 and result.A == [0, 0, 2]

    # Случай 13: Большие числа с разными знаками
    result = ADD_ZZ_Z_f(ZNum(0, NNum(3, [0, 0, 1])), ZNum(1, NNum(2, [0, 1])))  # 100 + (-10) = 90
    assert result.b == 0 and result.n == 2 and result.A == [0, 9]


def test_for_SUB_ZZ_Z():
    # Случай 1: Оба положительные (a > b)
    result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(0, NNum(1, [3])))  # 15 - 3 = 12
    assert result.b == 0 and result.n == 2 and result.A == [2, 1]

    # Случай 2: Оба положительные (a < b)
    result = SUB_ZZ_Z_f(ZNum(0, NNum(1, [3])), ZNum(0, NNum(2, [5, 1])))  # 3 - 15 = -12
    assert result.b == 1 and result.n == 2 and result.A == [2, 1]

    # Случай 3: Оба положительные (a = b)
    result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(0, NNum(2, [5, 1])))  # 15 - 15 = 0
    assert result.b == 0 and result.n == 1 and result.A == [0]

    # Случай 4: Первое положительное, второе отрицательное
    result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(1, NNum(1, [3])))  # 15 - (-3) = 18
    assert result.b == 0 and result.n == 2 and result.A == [8, 1]

    # Случай 5: Первое отрицательное, второе положительное
    result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(0, NNum(1, [3])))  # -15 - 3 = -18
    assert result.b == 1 and result.n == 2 and result.A == [8, 1]

    # Случай 6: Оба отрицательные (|a| > |b|)
    result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(1, NNum(1, [3])))  # -15 - (-3) = -12
    assert result.b == 1 and result.n == 2 and result.A == [2, 1]

    # Случай 7: Оба отрицательные (|a| < |b|)
    result = SUB_ZZ_Z_f(ZNum(1, NNum(1, [3])), ZNum(1, NNum(2, [5, 1])))  # -3 - (-15) = 12
    assert result.b == 0 and result.n == 2 and result.A == [2, 1]

    # Случай 8: Оба отрицательные (|a| = |b|)
    result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(1, NNum(2, [5, 1])))  # -15 - (-15) = 0
    assert result.b == 0 and result.n == 1 and result.A == [0]

    # Случай 9: С нулем (вычитание из нуля)
    zero = ZNum(0, NNum(1, [0]))
    result = SUB_ZZ_Z_f(zero, ZNum(0, NNum(2, [3, 2])))  # 0 - 23 = -23
    assert result.b == 1 and result.n == 2 and result.A == [3, 2]

    # Случай 10: С нулем (вычитание нуля)
    result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), zero)  # -15 - 0 = -15
    assert result.b == 1 and result.n == 2 and result.A == [5, 1]

    # Случай 11: Оба нуля
    result = SUB_ZZ_Z_f(zero, zero)  # 0 - 0 = 0
    assert result.b == 0 and result.n == 1 and result.A == [0]

    # Случай 12: Большие числа
    result = SUB_ZZ_Z_f(ZNum(0, NNum(3, [0, 0, 1])), ZNum(0, NNum(2, [0, 1])))  # 100 - 10 = 90
    assert result.b == 0 and result.n == 2 and result.A == [0, 9]

    # Случай 13: Большие числа с отрицательным результатом
    result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [0, 1])), ZNum(0, NNum(3, [0, 0, 1])))  # 10 - 100 = -90
    assert result.b == 1 and result.n == 2 and result.A == [0, 9]


test_for_ADD_ZZ_Z()
test_for_SUB_ZZ_Z()