import pytest
import sys
import os

# Добавляем пути к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules', 'P'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules', 'Q'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules', 'Z'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules', 'N'))

from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.P.DIV_PP_P import DIV_PP_P_f
from modules.P.MOD_PP_P import MOD_PP_P_f


class TestSimplePolynomialDivision:

    def create_nnum(self, value: int) -> NNum:
        """Создает NNum из целого числа"""
        if value == 0:
            return NNum(1, [0])
        return NNum(1, [value])

    def create_znum(self, value: int) -> ZNum:
        """Создает ZNum из целого числа"""
        if value == 0:
            nnum = self.create_nnum(0)
            return ZNum(0, nnum)

        sign = 1 if value < 0 else 0
        nnum = self.create_nnum(abs(value))
        return ZNum(sign, nnum)

    def create_qnum(self, numerator: int, denominator: int = 1) -> QNum:
        """Создает QNum из целых чисел"""
        num_z = self.create_znum(numerator)
        den_n = self.create_nnum(denominator)
        return QNum(num_z, den_n)

    def create_pnum(self, coefficients: list) -> PNum:
        """Создает PNum из списка коэффициентов"""
        # Убираем ведущие нули
        while coefficients and coefficients[-1] == 0:
            coefficients.pop()

        if not coefficients:
            return self.create_zero_poly()

        qnum_coeffs = [self.create_qnum(coeff) for coeff in coefficients]
        degree = len(coefficients) - 1
        return PNum(degree, qnum_coeffs)

    def create_zero_poly(self) -> PNum:
        """Создает нулевой многочлен"""
        zero_q = self.create_qnum(0)
        return PNum(-1, [zero_q])

    def test_division_by_zero(self):
        """Тест деления на нулевой многочлен"""
        poly1 = self.create_pnum([1, 2, 1])
        zero_poly = self.create_zero_poly()

        with pytest.raises(ValueError, match="Ошибка. Делитель равен нулю"):
            DIV_PP_P_f(poly1, zero_poly)

        with pytest.raises(ValueError, match="Ошибка. Делитель равен нулю"):
            MOD_PP_P_f(poly1, zero_poly)

    def test_lower_degree_dividend(self):
        """Тест когда степень делимого меньше степени делителя"""
        poly1 = self.create_pnum([1, 1])  # x + 1
        poly2 = self.create_pnum([1, 0, 1])  # x^2 + 1

        quotient = DIV_PP_P_f(poly1, poly2)

        # Частное должно быть нулевым
        zero_poly = self.create_zero_poly()
        assert quotient.m == -1  # Проверяем что это нулевой многочлен

    def test_simple_const_division(self):
        """Тест простого деления констант"""
        # 4 / 2 = 2
        poly1 = self.create_pnum([4])  # 4
        poly2 = self.create_pnum([2])  # 2

        quotient = DIV_PP_P_f(poly1, poly2)

        # Проверяем что результат не нулевой и имеет правильную степень
        assert quotient.m == 0  # Константа имеет степень 0
        # Проверяем что коэффициент не нулевой
        assert quotient.C[0].num_tor.A[0] != 0

    def test_basic_division_consistency(self):
        """Тест базовой согласованности DIV_PP_P_f и MOD_PP_P_f"""
        # Простой случай: (x^2 + 2x + 1) / (x + 1) = (x + 1)
        poly1 = self.create_pnum([1, 2, 1])  # x^2 + 2x + 1
        poly2 = self.create_pnum([1, 1])  # x + 1

        quotient = DIV_PP_P_f(poly1, poly2)
        remainder = MOD_PP_P_f(poly1, poly2)

        # Остаток должен быть нулевым для точного деления
        assert remainder.m == -1  # Нулевой многочлен


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
