# Хохряков Пётр Николаевич, гр. 4381

from modules.N.N_NUM import NNum
import pytest
from modules.N.MOD_NN_N import MOD_NN_N_f
from modules.N.GCF_NN_N import GCF_NN_N_f
from modules.N.LCM_NN_N import LCM_NN_N_f


def test_for_MOD_NN_N():
    """Тесты для функции MOD_NN_N_f - остаток от деления натуральных чисел"""

    # Обычные случаи деления
    result = MOD_NN_N_f(NNum(2, [0, 1]), NNum(1, [3]))  # 10 % 3 = 1
    assert result.n == 1 and result.A == [1]

    result = MOD_NN_N_f(NNum(2, [5, 1]), NNum(1, [4]))  # 15 % 4 = 3
    assert result.n == 1 and result.A == [3]

    result = MOD_NN_N_f(NNum(2, [5, 2]), NNum(1, [7]))  # 25 % 7 = 4
    assert result.n == 1 and result.A == [4]

    # Деление равных чисел
    result = MOD_NN_N_f(NNum(2, [3, 1]), NNum(2, [3, 1]))  # 13 % 13 = 0
    assert result.n == 1 and result.A == [0]

    result = MOD_NN_N_f(NNum(1, [5]), NNum(1, [5]))  # 5 % 5 = 0
    assert result.n == 1 and result.A == [0]

    # Когда делимое меньше делителя
    result = MOD_NN_N_f(NNum(1, [3]), NNum(1, [5]))  # 3 % 5 = 3
    assert result.n == 1 and result.A == [3]

    result = MOD_NN_N_f(NNum(1, [7]), NNum(2, [0, 1]))  # 7 % 10 = 7
    assert result.n == 1 and result.A == [7]

    # Случаи с нулевым остатком
    result = MOD_NN_N_f(NNum(2, [5, 1]), NNum(1, [5]))  # 15 % 5 = 0
    assert result.n == 1 and result.A == [0]

    result = MOD_NN_N_f(NNum(3, [0, 0, 1]), NNum(2, [0, 1]))  # 100 % 10 = 0
    assert result.n == 1 and result.A == [0]

    # Большие числа
    result = MOD_NN_N_f(NNum(3, [0, 0, 1]), NNum(2, [9, 9]))  # 100 % 99 = 1
    assert result.n == 1 and result.A == [1]

    result = MOD_NN_N_f(NNum(3, [9, 9, 9]), NNum(3, [0, 0, 1]))  # 999 % 100 = 99
    assert result.n == 2 and result.A == [9, 9]

    # Сложные случаи с многозначными числами
    result = MOD_NN_N_f(NNum(3, [3, 2, 1]), NNum(2, [5, 4]))  # 123 % 45 = 33
    assert result.n == 2 and result.A == [3, 3]

    result = MOD_NN_N_f(NNum(3, [6, 5, 2]), NNum(2, [3, 1]))  # 256 % 13 = 9
    assert result.n == 1 and result.A == [9]

    # Деление нуля на число
    zero = NNum(1, [0])
    result = MOD_NN_N_f(zero, NNum(1, [5]))  # 0 % 5 = 0
    assert result.n == 1 and result.A == [0]

    result = MOD_NN_N_f(zero, NNum(3, [3, 2, 1]))  # 0 % 123 = 0
    assert result.n == 1 and result.A == [0]

    # Деление на 1
    result = MOD_NN_N_f(NNum(2, [5, 1]), NNum(1, [1]))  # 15 % 1 = 0
    assert result.n == 1 and result.A == [0]

    result = MOD_NN_N_f(NNum(3, [3, 2, 1]), NNum(1, [1]))  # 123 % 1 = 0
    assert result.n == 1 and result.A == [0]

    # Граничные случаи
    result = MOD_NN_N_f(NNum(1, [1]), NNum(1, [2]))  # 1 % 2 = 1
    assert result.n == 1 and result.A == [1]

    result = MOD_NN_N_f(NNum(1, [9]), NNum(2, [0, 1]))  # 9 % 10 = 9
    assert result.n == 1 and result.A == [9]

    # Проверка корректного использования COM_NN_D (должно работать независимо от порядка аргументов)
    result1 = MOD_NN_N_f(NNum(1, [5]), NNum(1, [3]))  # 5 % 3 = 2
    result2 = MOD_NN_N_f(NNum(1, [3]), NNum(1, [5]))  # 3 % 5 = 3
    assert result1.A == [2]
    assert result2.A == [3]

    # Деление на ноль должно вызывать ошибку
    with pytest.raises(ValueError, match="Деление на ноль"):
        MOD_NN_N_f(NNum(1, [5]), zero)

    with pytest.raises(ValueError, match="Деление на ноль"):
        MOD_NN_N_f(zero, zero)


def test_for_GCF_NN_N():
    """Тесты для функции GCF_NN_N_f - НОД натуральных чисел"""

    # Обычные случаи
    result = GCF_NN_N_f(NNum(1, [6]), NNum(1, [8]))  # НОД(6, 8) = 2
    assert result.n == 1 and result.A == [2]

    result = GCF_NN_N_f(NNum(2, [2,1]), NNum(2, [8,1]))  # НОД(12, 18) = 6
    assert result.n == 1 and result.A == [6]

    result = GCF_NN_N_f(NNum(2, [5,1]), NNum(2, [5,2]))  # НОД(15, 25) = 5
    assert result.n == 1 and result.A == [5]

    # Взаимно простые числа
    result = GCF_NN_N_f(NNum(1, [7]), NNum(2, [3,1]))  # НОД(7, 13) = 1
    assert result.n == 1 and result.A == [1]

    result = GCF_NN_N_f(NNum(1, [8]), NNum(1, [9]))  # НОД(8, 9) = 1
    assert result.n == 1 and result.A == [1]

    # Равные числа
    result = GCF_NN_N_f(NNum(1, [5]), NNum(1, [5]))  # НОД(5, 5) = 5
    assert result.n == 1 and result.A == [5]

    result = GCF_NN_N_f(NNum(2, [1, 2]), NNum(2, [1, 2]))  # НОД(21, 21) = 21
    assert result.n == 2 and result.A == [1, 2]

    # Одно число является делителем другого
    result = GCF_NN_N_f(NNum(1, [3]), NNum(2, [2,1]))  # НОД(3, 12) = 3
    assert result.n == 1 and result.A == [3]

    result = GCF_NN_N_f(NNum(2, [0, 1]), NNum(1, [5]))  # НОД(10, 5) = 5
    assert result.n == 1 and result.A == [5]

    # Большие числа
    result = GCF_NN_N_f(NNum(2, [5, 2]), NNum(2, [0, 3]))  # НОД(25, 30) = 5
    assert result.n == 1 and result.A == [5]

    result = GCF_NN_N_f(NNum(3, [2, 4, 1]), NNum(3, [8, 6, 1]))  # НОД(142, 168) = 2
    assert result.n == 1 and result.A == [2]

    # Многозначные числа
    result = GCF_NN_N_f(NNum(3, [5, 3, 2]), NNum(3, [0, 5, 1]))  # НОД(235, 150) = 5
    assert result.n == 1 and result.A == [5]

    result = GCF_NN_N_f(NNum(3, [6, 2, 1]), NNum(3, [2, 8, 1]))  # НОД(126, 182) = 14
    assert result.n == 2 and result.A == [4, 1]  # 14 = [4, 1] так как цифры хранятся в обратном порядке

    # Числа в разном порядке (должны давать одинаковый результат)
    result1 = GCF_NN_N_f(NNum(1, [8]), NNum(2, [2, 1]))  # НОД(8, 12) = 4
    result2 = GCF_NN_N_f(NNum(2, [2,1]), NNum(1, [8]))  # НОД(12, 8) = 4
    assert result1.n == 1 and result1.A == [4]
    assert result2.n == 1 and result2.A == [4]
    assert result1.A == result2.A

    # Граничные случаи с единицей
    result = GCF_NN_N_f(NNum(1, [1]), NNum(1, [5]))  # НОД(1, 5) = 1
    assert result.n == 1 and result.A == [1]

    result = GCF_NN_N_f(NNum(1, [1]), NNum(1, [1]))  # НОД(1, 1) = 1
    assert result.n == 1 and result.A == [1]

    # Случай с нулем в одном из чисел (должна быть ошибка)
    zero = NNum(1, [0])

    with pytest.raises(ValueError, match="b равно нулю"):
        GCF_NN_N_f(zero, NNum(1, [5]))

    with pytest.raises(ValueError, match="b равно нулю"):
        GCF_NN_N_f(NNum(1, [5]), zero)

    with pytest.raises(ValueError, match="b равно нулю"):
        GCF_NN_N_f(zero, zero)

    # Алгоритм Евклида - последовательные шаги
    result = GCF_NN_N_f(NNum(2, [8,4]), NNum(2, [8,1]))  # НОД(48, 18) = 6
    assert result.n == 1 and result.A == [6]

    result = GCF_NN_N_f(NNum(2, [6,5]), NNum(2, [2,4]))  # НОД(56, 42) = 14
    assert result.n == 2 and result.A == [4, 1]  # 14 = [4, 1]

    # Большие взаимно простые числа
    result = GCF_NN_N_f(NNum(2, [7, 1]), NNum(2, [9,1]))  # НОД(17, 19) = 1
    assert result.n == 1 and result.A == [1]

    # Дополнительные тесты с корректной записью чисел
    result = GCF_NN_N_f(NNum(2, [0, 4]), NNum(2, [0, 6]))  # НОД(40, 60) = 20
    assert result.n == 2 and result.A == [0, 2]  # 20 = [0, 2]

    result = GCF_NN_N_f(NNum(2, [5, 3]), NNum(2, [0, 2]))  # НОД(35, 20) = 5
    assert result.n == 1 and result.A == [5]


def test_for_LCM_NN_N():
    """Тесты для функции LCM_NN_N_f - НОК натуральных чисел"""

    # Обычные случаи
    result = LCM_NN_N_f(NNum(1, [6]), NNum(1, [8]))  # НОК(6, 8) = 24 = [4, 2]
    assert result.n == 2 and result.A == [4, 2]

    result = LCM_NN_N_f(NNum(1, [2]), NNum(1, [3]))  # НОК(2, 3) = 6 = [6]
    assert result.n == 1 and result.A == [6]

    result = LCM_NN_N_f(NNum(1, [4]), NNum(1, [6]))  # НОК(4, 6) = 12 = [2, 1]
    assert result.n == 2 and result.A == [2, 1]

    # Равные числа
    result = LCM_NN_N_f(NNum(1, [5]), NNum(1, [5]))  # НОК(5, 5) = 5 = [5]
    assert result.n == 1 and result.A == [5]

    result = LCM_NN_N_f(NNum(2, [3, 1]), NNum(2, [3, 1]))  # НОК(13, 13) = 13 = [3, 1]
    assert result.n == 2 and result.A == [3, 1]

    # Одно число является делителем другого
    result = LCM_NN_N_f(NNum(1, [3]), NNum(1, [2]))  # НОК(3, 2) = 6 = [6]
    assert result.n == 1 and result.A == [6]

    result = LCM_NN_N_f(NNum(1, [4]), NNum(1, [2]))  # НОК(4, 2) = 4 = [4]
    assert result.n == 1 and result.A == [4]

    result = LCM_NN_N_f(NNum(2, [0, 1]), NNum(1, [5]))  # НОК(10, 5) = 10 = [0, 1]
    assert result.n == 2 and result.A == [0, 1]

    # Взаимно простые числа
    result = LCM_NN_N_f(NNum(1, [7]), NNum(1, [3]))  # НОК(7, 3) = 21 = [1, 2]
    assert result.n == 2 and result.A == [1, 2]

    result = LCM_NN_N_f(NNum(1, [8]), NNum(1, [9]))  # НОК(8, 9) = 72 = [2, 7]
    assert result.n == 2 and result.A == [2, 7]

    # Большие числа
    result = LCM_NN_N_f(NNum(1, [2]), NNum(1, [5]))  # НОК(2, 5) = 10 = [0, 1]
    assert result.n == 2 and result.A == [0, 1]

    result = LCM_NN_N_f(NNum(2, [5, 2]), NNum(2, [0, 3]))  # НОК(25, 30) = 150 = [0, 5, 1]
    assert result.n == 3 and result.A == [0, 5, 1]

    # Многозначные числа
    result = LCM_NN_N_f(NNum(2, [2, 1]), NNum(2, [4, 1]))  # НОК(12, 14) = 84 = [4, 8]
    assert result.n == 2 and result.A == [4, 8]

    result = LCM_NN_N_f(NNum(2, [5, 3]), NNum(2, [0, 2]))  # НОК(35, 20) = 140 = [0, 4, 1]
    assert result.n == 3 and result.A == [0, 4, 1]

    # Числа в разном порядке (должны давать одинаковый результат)
    result1 = LCM_NN_N_f(NNum(1, [4]), NNum(1, [6]))  # НОК(4, 6) = 12
    result2 = LCM_NN_N_f(NNum(1, [6]), NNum(1, [4]))  # НОК(6, 4) = 12
    assert result1.n == 2 and result1.A == [2, 1]
    assert result2.n == 2 and result2.A == [2, 1]
    assert result1.A == result2.A

    # Граничные случаи с единицей
    result = LCM_NN_N_f(NNum(1, [1]), NNum(1, [5]))  # НОК(1, 5) = 5 = [5]
    assert result.n == 1 and result.A == [5]

    result = LCM_NN_N_f(NNum(1, [1]), NNum(1, [1]))  # НОК(1, 1) = 1 = [1]
    assert result.n == 1 and result.A == [1]

    # Случай с нулем в одном из чисел (должна быть ошибка)
    zero = NNum(1, [0])

    with pytest.raises(ValueError, match="b равно нулю"):
        LCM_NN_N_f(zero, NNum(1, [5]))

    with pytest.raises(ValueError, match="b равно нулю"):
        LCM_NN_N_f(NNum(1, [5]), zero)

    with pytest.raises(ValueError, match="b равно нулю"):
        LCM_NN_N_f(zero, zero)

    # Алгоритм проверки: НОК(a, b) × НОД(a, b) = a × b
    a = NNum(2, [3, 1])  # 13
    b = NNum(2, [4, 1])  # 14
    lcm_result = LCM_NN_N_f(a, b)  # НОК(13, 14) = 182
    assert lcm_result.n == 3 and lcm_result.A == [2, 8, 1]  # 182 = [2, 8, 1]



# Запуски функций
test_for_MOD_NN_N()
test_for_GCF_NN_N()
test_for_LCM_NN_N()