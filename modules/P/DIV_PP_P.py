from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.P.DEG_P_N import DEG_P_N_f
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f
from modules.P.ADD_PP_P import ADD_PP_P_f


def DIV_PP_P_f(arg1: PNum, arg2: PNum) -> PNum:
    """
    Частное от деления многочлена arg1 на многочлен arg2 (деление с остатком)

    Возвращает PNum — частное.

    Делитель arg2 не может быть нулевым (m == -1).
    """
    # Проверка делителя
    if arg2.m == -1:
        raise ValueError("Ошибка. Делитель равен нулю")

    # Функция для преобразования NNum в int с проверкой на нулевой многочлен
    def get_degree(poly):
        deg_nnum = DEG_P_N_f(poly)
        # Преобразуем NNum в int
        if deg_nnum.A == [0]:
            deg = 0
        else:
            deg = int(''.join(map(str, deg_nnum.A)))
        # Дополнительная проверка на нулевой многочлен
        if deg == 0 and poly.C[0].num_tor.A[0] == 0:
            return -1
        return deg

    deg1 = get_degree(arg1)
    deg2 = get_degree(arg2)

    # Q_ZERO и Q_ONE в терминах ваших конструкторов ZNum/NNum
    Q_ZERO = QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))  # 0/1
    Q_ONE = QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))   # 1/1

    # если степень делимого меньше делителя — частное равно 0
    if deg1 < deg2 or deg1 == -1:
        return PNum(-1, [Q_ZERO])

    q_deg = deg1 - deg2
    # инициализация коэффициентов частного нулями (индекс 0 — свободный член)
    q_coeffs = [Q_ZERO for _ in range(q_deg + 1)]

    # создаём рабочую копию остатка (не изменяем входной arg1)
    remainder = PNum(arg1.m, [c for c in arg1.C])

    # основной цикл деления
    while True:
        r_deg = get_degree(remainder)
        if r_deg < deg2 or r_deg == -1:
            break

        # ведущие коэффициенты остатка и делителя
        lead_r = remainder.C[r_deg]  # используем r_deg как индекс
        lead_d = arg2.C[deg2]

        # коэффициент текущего шага: t = lead_r / lead_d
        t = DIV_QQ_Q_f(lead_r, lead_d)
        k = r_deg - deg2  # степень смещения для этого коэффициента в частном

        # проверка на выход за границы
        if k < 0 or k >= len(q_coeffs):
            break

        # записываем коэффициент в частное (позиция k)
        q_coeffs[k] = t

        # масштабируем делитель на t: scaled_divisor = arg2 * t
        # умножаем каждый коэффициент arg2.C на t через деление на (1/t):
        # c * t = c / (1/t)
        recip_t = DIV_QQ_Q_f(Q_ONE, t)   # 1 / t
        scaled_C = [DIV_QQ_Q_f(c, recip_t) for c in arg2.C]
        scaled_divisor = PNum(arg2.m, scaled_C)

        # сдвигаем на x^k
        subtrahend = MUL_Pxk_P_f(scaled_divisor, k)

        # remainder = remainder - subtrahend
        remainder = SUB_PP_P_f(remainder, subtrahend)

    # собираем результат (частное). PNum проверит корректность коэффициентов.
    return PNum(q_deg, q_coeffs)
