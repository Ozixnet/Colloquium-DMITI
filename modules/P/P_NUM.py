# Бердичевский Максим, гр. 4381

from modules.Q.Q_NUM import QNum


class PNum:
    """
    Структура хранения параметров для P-модулей

    m — степень многочлена.

    C — массив рациональных коэффициентов (первый коэффициент - свободный член).
    """
    def __init__(self, m: int, c: list[QNum]):
        if m < -1 or len(c) == 0 or (c[-1] == 0 and m != -1) or len(c) != m + 1:
            raise ValueError
        self.m = m
        self.C = c