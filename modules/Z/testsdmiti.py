import pytest
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.Z.DIV_ZZ_Z import DIV_ZZ_Z_f
from modules.Z.MOD_ZZ_Z import MOD_ZZ_Z_f
from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f


# Тарасов Юрий Романович, гр. 4381
class TestMUL_ZZ_Z:
    """Тесты для функции умножения целых чисел MUL_ZZ_Z"""

    def test_positive_multiplication(self):
        """Умножение двух положительных чисел"""
        num1 = ZNum(0, NNum(1, [5]))  # 5
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.b == 0  # положительный результат
        assert result.A == [5, 1]  # 15 -> [5, 1] в правильном порядке?
        # Примечание: нужно уточнить формат хранения цифр

    def test_negative_multiplication(self):
        """Умножение положительного на отрицательное"""
        num1 = ZNum(0, NNum(1, [4]))  # 4
        num2 = ZNum(1, NNum(1, [3]))  # -3
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.b == 1  # отрицательный результат

    def test_double_negative_multiplication(self):
        """Умножение двух отрицательных чисел"""
        num1 = ZNum(1, NNum(1, [2]))  # -2
        num2 = ZNum(1, NNum(1, [3]))  # -3
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.b == 0  # положительный результат

    def test_zero_multiplication(self):
        """Умножение на ноль"""
        num1 = ZNum(0, NNum(1, [7]))  # 7
        num2 = ZNum(0, NNum(1, [0]))  # 0
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.A == [0]  # результат 0
        assert result.b == 0  # знак 0 для нуля

    def test_multiplication_by_one(self):
        """Умножение на единицу"""
        num1 = ZNum(0, NNum(1, [9]))  # 9
        num2 = ZNum(0, NNum(1, [1]))  # 1
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.A == [9]  # результат 9


class TestDIV_ZZ_Z:
    """Тесты для функции частного от деления целых чисел DIV_ZZ_Z"""

    def test_even_division(self):
        """Деление без остатка"""
        num1 = ZNum(0, NNum(1, [6]))  # 6
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 0  # положительный результат
        assert result.A == [2]  # 6 / 3 = 2

    def test_division_with_remainder(self):
        """Деление с остатком (должно округляться в меньшую сторону)"""
        num1 = ZNum(0, NNum(1, [7]))  # 7
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.A == [2]  # 7 / 3 = 2 (целая часть)

    def test_negative_dividend(self):
        """Деление отрицательного делимого на положительный делитель"""
        num1 = ZNum(1, NNum(1, [8]))  # -8
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 1  # отрицательный результат

    def test_negative_divisor(self):
        """Деление положительного делимого на отрицательный делитель"""
        num1 = ZNum(0, NNum(1, [8]))  # 8
        num2 = ZNum(1, NNum(1, [2]))  # -2
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 1  # отрицательный результат

    def test_double_negative_division(self):
        """Деление двух отрицательных чисел"""
        num1 = ZNum(1, NNum(1, [9]))  # -9
        num2 = ZNum(1, NNum(1, [3]))  # -3
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 0  # положительный результат

    def test_zero_dividend(self):
        """Деление нуля на ненулевое число"""
        num1 = ZNum(0, NNum(1, [0]))  # 0
        num2 = ZNum(0, NNum(1, [5]))  # 5
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.A == [0]  # результат 0

    def test_division_by_zero(self):
        """Попытка деления на ноль (должна вызывать ошибку)"""
        num1 = ZNum(0, NNum(1, [5]))  # 5
        num2 = ZNum(0, NNum(1, [0]))  # 0
        with pytest.raises(ValueError):
            DIV_ZZ_Z_f(num1, num2)


class TestMOD_ZZ_Z:
    """Тесты для функции остатка от деления целых чисел MOD_ZZ_Z"""

    def test_positive_remainder(self):
        """Остаток от деления положительных чисел"""
        num1 = ZNum(0, NNum(1, [7]))  # 7
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = MOD_ZZ_Z_f(num1, num2)
        assert result.b == 0  # положительный остаток
        assert result.A == [1]  # 7 % 3 = 1

    def test_zero_remainder(self):
        """Деление без остатка"""
        num1 = ZNum(0, NNum(1, [6]))  # 6
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = MOD_ZZ_Z_f(num1, num2)
        assert result.A == [0]  # остаток 0

    def test_negative_dividend_remainder(self):
        """Остаток при отрицательном делимом"""
        num1 = ZNum(1, NNum(1, [7]))  # -7
        num2 = ZNum(0, NNum(1, [3]))  # 3
        result = MOD_ZZ_Z_f(num1, num2)
        # Ожидаемое поведение зависит от реализации - может быть -1 или 2

    def test_negative_divisor_remainder(self):
        """Остаток при отрицательном делителе"""
        num1 = ZNum(0, NNum(1, [7]))  # 7
        num2 = ZNum(1, NNum(1, [3]))  # -3
        result = MOD_ZZ_Z_f(num1, num2)
        # Ожидаемое поведение зависит от реализации

    def test_zero_dividend_remainder(self):
        """Остаток от деления нуля"""
        num1 = ZNum(0, NNum(1, [0]))  # 0
        num2 = ZNum(0, NNum(1, [5]))  # 5
        result = MOD_ZZ_Z_f(num1, num2)
        assert result.A == [0]  # остаток 0

    def test_mod_by_zero(self):
        """Попытка взятия остатка от деления на ноль"""
        num1 = ZNum(0, NNum(1, [5]))  # 5
        num2 = ZNum(0, NNum(1, [0]))  # 0
        with pytest.raises(ValueError):
            MOD_ZZ_Z_f(num1, num2)


class TestArithmeticRelationships:
    """Тесты на арифметические соотношения между операциями"""

    def test_relationship_between_div_and_mod_positive(self):
        """Проверка соотношения a = b * div(a,b) + mod(a,b) для положительных чисел"""
        # Тестируем: 17 = 5 * 3 + 2
        a = ZNum(0, NNum(2, [7, 1]))  # 17 (предполагаем младшие разряды первыми)
        b = ZNum(0, NNum(1, [5]))  # 5

        div_result = DIV_ZZ_Z_f(a, b)  # 17 // 5 = 3
        mod_result = MOD_ZZ_Z_f(a, b)  # 17 % 5 = 2

        # Вычисляем b * div_result
        b_times_div = MUL_ZZ_Z_f(b, div_result)  # 5 * 3 = 15

        # Вычисляем b * div_result + mod_result
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)  # 15 + 2 = 17

        # Проверяем, что результат равен исходному a
        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A

    def test_relationship_between_div_and_mod_negative_dividend(self):
        """Проверка соотношения для отрицательного делимого"""
        # Тестируем: -17 = 5 * (-4) + 3 или -17 = 5 * (-3) + (-2)
        # Зависит от реализации целочисленного деления
        a = ZNum(1, NNum(2, [7, 1]))  # -17
        b = ZNum(0, NNum(1, [5]))  # 5

        div_result = DIV_ZZ_Z_f(a, b)  # -17 // 5
        mod_result = MOD_ZZ_Z_f(a, b)  # -17 % 5

        # Проверяем соотношение: a = b * div_result + mod_result
        b_times_div = MUL_ZZ_Z_f(b, div_result)
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)

        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A

    def test_relationship_between_div_and_mod_negative_divisor(self):
        """Проверка соотношения для отрицательного делителя"""
        # Тестируем: 17 = (-5) * (-3) + 2 или 17 = (-5) * (-4) + (-3)
        # Зависит от реализации целочисленного деления
        a = ZNum(0, NNum(2, [7, 1]))  # 17
        b = ZNum(1, NNum(1, [5]))  # -5

        div_result = DIV_ZZ_Z_f(a, b)  # 17 // (-5)
        mod_result = MOD_ZZ_Z_f(a, b)  # 17 % (-5)

        # Проверяем соотношение: a = b * div_result + mod_result
        b_times_div = MUL_ZZ_Z_f(b, div_result)
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)

        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A

    def test_relationship_between_div_and_mod_zero_dividend(self):
        """Проверка соотношения для нулевого делимого"""
        a = ZNum(0, NNum(1, [0]))  # 0
        b = ZNum(0, NNum(1, [5]))  # 5

        div_result = DIV_ZZ_Z_f(a, b)  # 0 // 5 = 0
        mod_result = MOD_ZZ_Z_f(a, b)  # 0 % 5 = 0

        # Проверяем соотношение: 0 = 5 * 0 + 0
        b_times_div = MUL_ZZ_Z_f(b, div_result)  # 5 * 0 = 0
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)  # 0 + 0 = 0

        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A


def test_comprehensive_arithmetic_chain():
    """Комплексный тест арифметической цепочки операций"""
    # Создаем тестовые числа
    x = ZNum(0, NNum(1, [8]))  # 8
    y = ZNum(0, NNum(1, [3]))  # 3

    # Выполняем последовательность операций
    mul_result = MUL_ZZ_Z_f(x, y)  # 8 * 3 = 24
    div_result = DIV_ZZ_Z_f(mul_result, y)  # 24 // 3 = 8
    mod_result = MOD_ZZ_Z_f(mul_result, y)  # 24 % 3 = 0

    # Проверяем, что div_result равен исходному x
    assert div_result.b == x.b
    assert div_result.n == x.n
    assert div_result.A == x.A

    # Проверяем, что остаток равен 0
    assert mod_result.A == [0]

    # Проверяем соотношение для mul_result
    check_result = ADD_ZZ_Z_f(MUL_ZZ_Z_f(y, div_result), mod_result)
    assert check_result.b == mul_result.b
    assert check_result.n == mul_result.n
    assert check_result.A == mul_result.A


if __name__ == "__main__":
    pytest.main()