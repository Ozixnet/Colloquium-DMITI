from modules.С.C_NUM import Permutation


def IDENTITY_P_P_f(n: int) -> Permutation:
    """
    Тождественная перестановка в S_n.

    n - размер перестановки (int).

    Возврат - Permutation (тождественная перестановка).
    """
    return Permutation(list(range(1, n + 1)))

