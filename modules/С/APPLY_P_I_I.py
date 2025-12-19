from modules.С.C_NUM import Permutation


def APPLY_P_I_I_f(p: Permutation, i: int) -> int:
    """
    Применение перестановки к элементу i из {1..n}.

    p - перестановка типа Permutation.

    i - элемент из {1..n}.

    Возврат - int (результат применения перестановки).
    """
    if not 1 <= i <= p.n:
        raise IndexError(f"Элемент {i} вне диапазона 1..{p.n}")
    # минус один, потому что список Python 0-индексный
    return p._mapping[i - 1]

