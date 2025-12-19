from modules.С.C_NUM import Permutation


def INVERSE_P_P_f(p: Permutation) -> Permutation:
    """
    Обратная перестановка: inv(p)(p(i)) = i.

    p - перестановка типа Permutation.

    Возврат - Permutation (обратная перестановка).
    """
    inv = [0] * p.n
    for i, image in enumerate(p._mapping, start=1):
        inv[image - 1] = i
    return Permutation(inv)

