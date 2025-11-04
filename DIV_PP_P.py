from modules.P_NUM import PNum
from modules.DIV_QQ_Q import DIV_QQ_Q
from modules.DEG_P_N import DEG_P_N
from modules.MUL_Pxk_P import MUL_Pxk_P
from modules.SUB_PP_P import SUB_PP_P
from modules.ADD_PP_P import ADD_PP_P


# выполнил Тарасов Юрий гр.4381
def DIV_PP_P(arg1: PNum, arg2:PNum) -> PNum:
    """
                  Частное от деления многочлена на многочлен при делении с остатком
                  arg1 - первый многочлен
                  arg2 - второй многочлен, не может быть 0
                  Возврат - PNum
    """
    if arg2.m == -1:
        raise ValueError("Ошибка. Делитель равен нулю")
    #получим степени многочленов
    deg1 = DEG_P_N(arg1)
    deg2 = DEG_P_N(arg2)
    #инициализируем результат
    res = PNum()
    res.m, res.C = -1, 0
    #алгоритм деления
    while deg1 >= deg2:
        #если степени одинаковые, то прибавляем к результату коэфицент равный частному старших коэфов многочленов
        if deg1 == deg2:
            res = ADD_PP_P(res, PNum(0, list(DIV_QQ_Q(arg1.C[-1], arg2.C[-1]))))
        else:
        #иначе вычитаем из делимого делитель умноженный x^(разница их степеней)
            res = ADD_PP_P(res, SUB_PP_P(arg1, MUL_Pxk_P(arg2, deg1 - deg2)))
            arg1 = SUB_PP_P(arg1, MUL_Pxk_P(arg2, deg1 - deg2))
        deg1 = DEG_P_N(arg1)
        deg2 = DEG_P_N(arg2)
    return res