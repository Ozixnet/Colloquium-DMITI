from modules.С.C_NUM import Permutation
from modules.С.APPLY_P_I_I import APPLY_P_I_I_f


def TO_CYCLES_P_L_f(p: Permutation, include_fixed_points: bool = False) -> list:
    """
    Разложение перестановки на непересекающиеся циклы.
    Возвращает список циклов (каждый цикл — list[int]).
    Если include_fixed_points=False — циклы длины 1 (фиксированные точки) не возвращаются.

    p - перестановка типа Permutation.

    include_fixed_points - булево значение, включать ли фиксированные точки.

    Возврат - list[list[int]] (список циклов).
    """
    n = p.n
    visited = [False] * (n + 1)  # индексируем с 1 до n
    cycles = []

    for start in range(1, n + 1):
        if visited[start]:
            continue

        current = start
        cycle = []

        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = APPLY_P_I_I_f(p, current)

        if len(cycle) > 1 or include_fixed_points:
            cycles.append(cycle)

    return cycles

