# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum


class PNum:
    """
    Структура хранения параметров для P-модулей

    m — степень многочлена.

    C — массив рациональных коэффициентов.
    """
    def __init__(self, m: int, c: list[QNum]):
        self.m = m
        self.C = c