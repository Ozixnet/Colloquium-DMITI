from modules.С.C_NUM import Permutation


def SIGN_P_I_f(p: Permutation) -> int:
    """
    Знак перестановки: +1 для чётной, -1 для нечётной.
    Считаем число инверсий N и возвращаем (-1)^N.

    p - перестановка типа Permutation.

    Возврат - int (+1 для чётной, -1 для нечётной).
    """
    inv_count = 0
    a = p._mapping
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inv_count += 1
    return 1 if inv_count % 2 == 0 else -1

