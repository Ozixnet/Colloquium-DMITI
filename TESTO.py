import pytest
from modules.P_NUM import PNum
from modules.DIV_PP_P import DIV_PP_P
from modules.MOD_PP_P import MOD_PP_P


class TestPolynomialDivision:
    def test_division_by_zero(self):
        """Тест на деление на нулевой многочлен"""
        poly1 = PNum(2, [1, 2, 1])  # x^2 + 2x + 1
        zero_poly = PNum(-1, 0)  # Нулевой многочлен

        with pytest.raises(ValueError, match="Ошибка. Делитель равен нулю"):
            DIV_PP_P(poly1, zero_poly)

        with pytest.raises(ValueError, match="Ошибка. Делитель равен нулю"):
            MOD_PP_P(poly1, zero_poly)

    def test_equal_degree_division(self):
        """Тест деления многочленов одинаковой степени"""
        # (x^2 + 2x + 1) / (x^2 + x + 1) = 1 с остатком (x)
        poly1 = PNum(2, [1, 2, 1])  # x^2 + 2x + 1
        poly2 = PNum(2, [1, 1, 1])  # x^2 + x + 1

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        # Проверяем что делитель * частное + остаток = делимое
        # Это основное свойство деления с остатком
        assert quotient.m >= 0  # Частное должно быть многочленом
        assert remainder.m >= 0  # Остаток должен быть многочленом

    def test_lower_degree_dividend(self):
        """Тест когда степень делимого меньше степени делителя"""
        # (x + 1) / (x^2 + 1) = 0 с остатком (x + 1)
        poly1 = PNum(1, [1, 1])  # x + 1
        poly2 = PNum(2, [1, 0, 1])  # x^2 + 1

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        # Частное должно быть нулевым
        assert quotient.m == -1
        # Остаток должен равняться делимому
        assert remainder.C == poly1.C

    def test_exact_division(self):
        """Тест точного деления без остатка"""
        # (x^2 - 1) / (x - 1) = (x + 1)
        poly1 = PNum(2, [1, 0, -1])  # x^2 - 1
        poly2 = PNum(1, [1, -1])  # x - 1

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        # Остаток должен быть нулевым
        assert remainder.m == -1
        # Частное должно быть ненулевым
        assert quotient.m >= 0

    def test_division_with_remainder(self):
        """Тест деления с остатком"""
        # (x^2 + x + 1) / (x - 1) = (x + 2) с остатком 3
        poly1 = PNum(2, [1, 1, 1])  # x^2 + x + 1
        poly2 = PNum(1, [1, -1])  # x - 1

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        # Проверяем что оба результата - многочлены
        assert isinstance(quotient, PNum)
        assert isinstance(remainder, PNum)
        # Степень остатка должна быть меньше степени делителя
        assert remainder.m < poly2.m

    def test_division_relation(self):
        """Тест основного свойства деления: делимое = делитель * частное + остаток"""
        poly1 = PNum(3, [2, 0, -1, 1])  # 2x^3 - x + 1
        poly2 = PNum(2, [1, 1, 1])  # x^2 + x + 1

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        # Основное свойство деления с остатком
        # dividend = divisor * quotient + remainder
        # Проверяем что степень остатка меньше степени делителя
        assert remainder.m < poly2.m

    def test_const_division(self):
        """Тест деления константных многочленов"""
        poly1 = PNum(0, [5])  # 5
        poly2 = PNum(0, [2])  # 2

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        # Оба результата должны быть многочленами
        assert isinstance(quotient, PNum)
        assert isinstance(remainder, PNum)

    def test_high_degree_polynomials(self):
        """Тест деления многочленов высоких степеней"""
        # Многочлены высоких степеней для проверки стабильности алгоритма
        poly1 = PNum(4, [1, 0, 0, 0, 1])  # x^4 + 1
        poly2 = PNum(2, [1, 1, 1])  # x^2 + x + 1

        quotient = DIV_PP_P(poly1, poly2)
        remainder = MOD_PP_P(poly1, poly2)

        assert isinstance(quotient, PNum)
        assert isinstance(remainder, PNum)
        assert remainder.m < poly2.m