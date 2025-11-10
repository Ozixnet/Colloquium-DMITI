from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Q.DIV_QQ_Q import DIV_QQ_Q_f
from modules.P.DEG_P_N import DEG_P_N_f
from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f
from modules.P.ADD_PP_P import ADD_PP_P_f


# выполнил Тарасов Юрий гр.4381
def DIV_PP_P_f(arg1: PNum, arg2: PNum) -> PNum:
    """
    Частное от деления многочлена на многочлен при делении с остатком
    arg1 - первый многочлен.
    arg2 - второй многочлен, не может быть 0.
    Возврат - PNum.
    """
    if arg2.m == -1:
        raise ValueError("Ошибка. Делитель равен нулю")

    # Получим степени многочленов
    deg1 = DEG_P_N_f(arg1)
    deg2 = DEG_P_N_f(arg2)

    # Инициализируем результат как нулевой многочлен
    res = PNum(-1, [QNum(0, 1)])

    # Алгоритм деления
    while deg1 >= deg2:
        # Вычисляем коэффициент: старший коэффициент делимого / старший коэффициент делителя
        coef = DIV_QQ_Q_f(arg1.C[deg1], arg2.C[deg2])

        # Создаем одночлен: coef * x^(deg1 - deg2)
        monomial = PNum(0, [coef])  # Многочлен степени 0 с коэффициентом coef
        if deg1 - deg2 > 0:
            monomial = MUL_Pxk_P_f(monomial, deg1 - deg2)  # Умножаем на x^k

        # Добавляем одночлен к результату
        res = ADD_PP_P_f(res, monomial)

        # Создаем произведение: делитель * одночлен
        # Умножаем делитель на x^k
        shifted_divisor = MUL_Pxk_P_f(arg2, deg1 - deg2)

        # Умножаем shifted_divisor на coef (каждый коэффициент умножаем на coef)
        # Создаем новый многочлен с умноженными коэффициентами
        multiplied_coeffs = []
        for q_num in shifted_divisor.C:
            # Умножение рациональных чисел через деление: a * b = a / (1/b)
            one = QNum(1, 1)
            reciprocal = DIV_QQ_Q_f(one, q_num) if q_num.num_tor.A[0] != 0 else QNum(0, 1)
            multiplied_coef = DIV_QQ_Q_f(coef, reciprocal) if q_num.num_tor.A[0] != 0 else QNum(0, 1)
            multiplied_coeffs.append(multiplied_coef)

        product = PNum(shifted_divisor.m, multiplied_coeffs)

        # Вычитаем произведение из делимого
        arg1 = SUB_PP_P_f(arg1, product)

        # Обновляем степень
        deg1 = DEG_P_N_f(arg1)

    return res
