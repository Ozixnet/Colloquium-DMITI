from modules.P_NUM import PNum
from modules.DIV_PP_P import DIV_PP_P
from modules.MUL_PP_P import MUL_PP_P
from modules.SUB_PP_P import SUB_PP_P


# выполнил Тарасов Юрий гр.4381
def MOD_PP_P(arg1: PNum, arg2: PNum) -> PNum:
    """
                      Остаток от деления многочлена на многочлен при делении с остатком
                      arg1 - первый многочлен
                      arg2 - второй многочлен, не может быть 0
                      Возврат - PNum
    """
    if arg2.m == -1:
        raise ValueError("Ошибка. Делитель равен нулю")
    res = PNum()
    res.m, res.C = -1, 0
    # получим частное
    quotient = DIV_PP_P(arg1, arg2)
    # получаем остаток
    res = SUB_PP_P(arg1, MUL_PP_P(arg2, quotient))
    return res
