import pytest
from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.P.DEG_P_N import DEG_P_N_f
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f
from modules.P.ADD_PP_P import ADD_PP_P_f
from modules.P.MUL_PP_P import MUL_PP_P_f
from modules.P.DIV_PP_P import DIV_PP_P_f
from modules.P.MOD_PP_P import MOD_PP_P_f


class TestDIV_PP_P:
    """Тесты для функции деления многочленов DIV_PP_P_f"""

    def test_division_by_zero(self):
        """Тест деления на нулевой многочлен"""
        poly1 = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])  # x^2 + 2x + 1
        zero_poly = PNum(-1, [QNum(0, 1)])  # нулевой многочлен

        with pytest.raises(ValueError, match="Ошибка. Делитель равен нулю"):
            DIV_PP_P_f(poly1, zero_poly)

    def test_simple_division_no_remainder(self):
        """Тест простого деления без остатка"""
        # (x^2 + 2x + 1) / (x + 1) = x + 1
        dividend = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])
        expected = PNum(1, [QNum(1, 1), QNum(1, 1)])

        result = DIV_PP_P_f(dividend, divisor)
        assert self.poly_equal(result, expected)

    def test_division_with_remainder(self):
        """Тест деления с остатком"""
        # (x^2 + 3x + 5) / (x + 1) = x + 2 (частное)
        dividend = PNum(2, [QNum(5, 1), QNum(3, 1), QNum(1, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])
        expected_quotient = PNum(1, [QNum(2, 1), QNum(1, 1)])  # x + 2

        result = DIV_PP_P_f(dividend, divisor)
        assert self.poly_equal(result, expected_quotient)

    def test_division_same_polynomials(self):
        """Тест деления многочлена на самого себя"""
        # (x^2 + 2x + 1) / (x^2 + 2x + 1) = 1
        poly = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        expected = PNum(0, [QNum(1, 1)])  # 1

        result = DIV_PP_P_f(poly, poly)
        assert self.poly_equal(result, expected)

    def test_division_higher_degree_divisor(self):
        """Тест когда степень делителя больше степени делимого"""
        # (x + 1) / (x^2 + 2x + 1) = 0
        dividend = PNum(1, [QNum(1, 1), QNum(1, 1)])
        divisor = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        expected = PNum(-1, [QNum(0, 1)])  # 0

        result = DIV_PP_P_f(dividend, divisor)
        assert self.poly_equal(result, expected)

    def test_division_by_constant(self):
        """Тест деления на константу"""
        # (2x^2 + 4x + 6) / 2 = x^2 + 2x + 3
        dividend = PNum(2, [QNum(6, 1), QNum(4, 1), QNum(2, 1)])
        divisor = PNum(0, [QNum(2, 1)])
        expected = PNum(2, [QNum(3, 1), QNum(2, 1), QNum(1, 1)])

        result = DIV_PP_P_f(dividend, divisor)
        assert self.poly_equal(result, expected)

    def test_division_complex_case(self):
        """Тест сложного случая деления"""
        # (2x^3 + 3x^2 + 4x + 6) / (x + 1) = 2x^2 + x + 3
        dividend = PNum(3, [QNum(6, 1), QNum(4, 1), QNum(3, 1), QNum(2, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])
        expected = PNum(2, [QNum(3, 1), QNum(1, 1), QNum(2, 1)])

        result = DIV_PP_P_f(dividend, divisor)
        assert self.poly_equal(result, expected)

    def test_division_with_rational_coefficients(self):
        """Тест деления с дробными коэффициентами"""
        # (1/2 x^2 + x + 1/4) / (1/2 x + 1/2) = x + 1/2
        dividend = PNum(2, [QNum(1, 4), QNum(1, 1), QNum(1, 2)])
        divisor = PNum(1, [QNum(1, 2), QNum(1, 2)])
        expected = PNum(1, [QNum(1, 2), QNum(1, 1)])

        result = DIV_PP_P_f(dividend, divisor)
        assert self.poly_equal(result, expected)

    def poly_equal(self, p1: PNum, p2: PNum) -> bool:
        """Вспомогательная функция для сравнения многочленов"""
        if p1.m != p2.m:
            return False

        for i in range(len(p1.C)):
            # Сравниваем числители и знаменатели
            if (p1.C[i].num_tor.A != p2.C[i].num_tor.A or
                    p1.C[i].den_tor.A != p2.C[i].den_tor.A):
                return False

        return True


class TestMOD_PP_P:
    """Тесты для функции вычисления остатка MOD_PP_P_f"""

    def test_mod_by_zero(self):
        """Тест взятия остатка от деления на нулевой многочлен"""
        poly1 = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        zero_poly = PNum(-1, [QNum(0, 1)])

        with pytest.raises(ValueError, match="Ошибка. Делитель равен нулю"):
            MOD_PP_P_f(poly1, zero_poly)

    def test_mod_no_remainder(self):
        """Тест когда остаток равен нулю"""
        # (x^2 + 2x + 1) % (x + 1) = 0
        dividend = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])
        expected = PNum(-1, [QNum(0, 1)])  # 0

        result = MOD_PP_P_f(dividend, divisor)
        assert TestDIV_PP_P.poly_equal(self, result, expected)

    def test_mod_with_remainder(self):
        """Тест когда есть ненулевой остаток"""
        # (x^2 + 3x + 5) % (x + 1) = 3
        dividend = PNum(2, [QNum(5, 1), QNum(3, 1), QNum(1, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])
        expected = PNum(0, [QNum(3, 1)])  # 3

        result = MOD_PP_P_f(dividend, divisor)
        assert TestDIV_PP_P.poly_equal(self, result, expected)

    def test_mod_same_polynomials(self):
        """Тест взятия остатка при делении многочлена на самого себя"""
        # (x^2 + 2x + 1) % (x^2 + 2x + 1) = 0
        poly = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        expected = PNum(-1, [QNum(0, 1)])  # 0

        result = MOD_PP_P_f(poly, poly)
        assert TestDIV_PP_P.poly_equal(self, result, expected)

    def test_mod_higher_degree_divisor(self):
        """Тест когда степень делителя больше степени делимого"""
        # (x + 1) % (x^2 + 2x + 1) = x + 1
        dividend = PNum(1, [QNum(1, 1), QNum(1, 1)])
        divisor = PNum(2, [QNum(1, 1), QNum(2, 1), QNum(1, 1)])
        expected = dividend  # остаток = делимое

        result = MOD_PP_P_f(dividend, divisor)
        assert TestDIV_PP_P.poly_equal(self, result, expected)

    def test_mod_complex_case(self):
        """Тест сложного случая вычисления остатка"""
        # (2x^3 + 3x^2 + 4x + 6) % (x + 1) = 3
        dividend = PNum(3, [QNum(6, 1), QNum(4, 1), QNum(3, 1), QNum(2, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])
        expected = PNum(0, [QNum(3, 1)])  # 3

        result = MOD_PP_P_f(dividend, divisor)
        assert TestDIV_PP_P.poly_equal(self, result, expected)

    def test_division_consistency(self):
        """Тест согласованности DIV_PP_P_f и MOD_PP_P_f"""
        # Проверяем что dividend = divisor * quotient + remainder
        dividend = PNum(3, [QNum(6, 1), QNum(4, 1), QNum(3, 1), QNum(2, 1)])
        divisor = PNum(1, [QNum(1, 1), QNum(1, 1)])

        quotient = DIV_PP_P_f(dividend, divisor)
        remainder = MOD_PP_P_f(dividend, divisor)

        # Вычисляем divisor * quotient + remainder
        product = MUL_PP_P_f(divisor, quotient)
        reconstructed_dividend = ADD_PP_P_f(product, remainder)

        assert TestDIV_PP_P.poly_equal(self, dividend, reconstructed_dividend)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
