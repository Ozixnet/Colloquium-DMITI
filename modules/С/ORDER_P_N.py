from modules.С.C_NUM import Permutation
from modules.С.TO_CYCLES_P_L import TO_CYCLES_P_L_f

from modules.N.N_NUM import NNum
from modules.N.LCM_NN_N import LCM_NN_N_f


def _int_to_nnum(value: int) -> NNum:
    """Преобразует int в NNum."""
    if value == 0:
        return NNum(1, [0])
    digits = []
    while value > 0:
        digits.append(value % 10)
        value //= 10
    return NNum(len(digits), digits)


def _nnum_to_int(nnum: NNum) -> int:
    """Преобразует NNum в int."""
    result = 0
    for i, digit in enumerate(nnum.A):
        result += digit * (10 ** i)
    return result


def ORDER_P_N_f(p: Permutation) -> int:
    """
    Порядок перестановки: минимальное m > 0, для которого p^m = id.
    Равен НОК длин циклов в разложении.

    p - перестановка типа Permutation.

    Возврат - int (порядок перестановки).
    """
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    if not cycles:
        return 1  # тождественная перестановка

    lcm = _int_to_nnum(1)
    for cycle in cycles:
        length = len(cycle)
        length_nnum = _int_to_nnum(length)
        lcm = LCM_NN_N_f(lcm, length_nnum)
    return _nnum_to_int(lcm)
