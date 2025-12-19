from modules.С.C_NUM import Permutation
from modules.С.APPLY_P_I_I import APPLY_P_I_I_f


def COMPOSE_PP_P_f(p1: Permutation, p2: Permutation) -> Permutation:
    """
    Композиция перестановок: p1 ∘ p2.
    Сначала применяем p2, потом p1.
    То есть (p1 ∘ p2)(i) = p1(p2(i)).

    p1 - первая перестановка типа Permutation.

    p2 - вторая перестановка типа Permutation.

    Возврат - Permutation (результат композиции).
    """
    if p1.n != p2.n:
        raise ValueError("Композиция только для перестановок одного размера")
    result = [APPLY_P_I_I_f(p1, APPLY_P_I_I_f(p2, i)) for i in range(1, p1.n + 1)]
    return Permutation(result)

