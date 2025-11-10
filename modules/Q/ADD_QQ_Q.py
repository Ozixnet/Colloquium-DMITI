# Сложение рациональных чисел
# Формула: (a/b) + (c/d) = (a*d + c*b) / (b*d)

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f
from modules.Q.RED_Q_Q import RED_Q_Q_f


def ADD_QQ_Q_f(a: QNum, b: QNum) -> QNum:
    """
    Сложение рациональных чисел (дробей).
    
    Вычисляет сумму двух рациональных чисел по формуле:
    (a/b) + (c/d) = (a*d + c*b) / (b*d)
    
    После сложения результат сокращается через НОД для нормализации.
    
    Args:
        a: Первое рациональное число
        b: Второе рациональное число
        
    Returns:
        QNum: Сумма a + b (сокращенная дробь)
        
    Examples:
        >>> a = QNum(ZNum(0, NNum(1, [1])), NNum(1, [2]))  # 1/2
        >>> b = QNum(ZNum(0, NNum(1, [1])), NNum(1, [3]))  # 1/3
        >>> ADD_QQ_Q_f(a, b)
        QNum(ZNum(0, NNum(1, [5])), NNum(1, [6]))  # 5/6
        
    Raises:
        TypeError: Если аргументы не являются объектами QNum
    """
    # Валидация входных данных
    if a is None or not isinstance(a, QNum):
        raise TypeError("Первый аргумент должен быть типа QNum")
    
    if b is None or not isinstance(b, QNum):
        raise TypeError("Второй аргумент должен быть типа QNum")
    
    # Приводим к общему знаменателю: (a*d + c*b) / (b*d)
    # a*d
    a_times_d = MUL_ZZ_Z_f(a.num_tor, ZNum(0, b.den_tor))
    
    # c*b (где c = b.num_tor, b = a.den_tor)
    c_times_b = MUL_ZZ_Z_f(b.num_tor, ZNum(0, a.den_tor))
    
    # a*d + c*b
    numerator = ADD_ZZ_Z_f(a_times_d, c_times_b)
    
    # b*d
    denominator = MUL_NN_N_f(a.den_tor, b.den_tor)
    
    # Создаем новое рациональное число
    result = QNum(numerator, denominator)
    
    # Сокращаем дробь через НОД
    result = RED_Q_Q_f(result)
    
    return result


