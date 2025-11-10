# Умножение рациональных чисел
# Формула: (a/b) * (c/d) = (a*c) / (b*d)

from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.Q.RED_Q_Q import RED_Q_Q_f


def MUL_QQ_Q_f(a: QNum, b: QNum) -> QNum:
    """
    Умножение рациональных чисел (дробей).
    
    Вычисляет произведение двух рациональных чисел по формуле:
    (a/b) * (c/d) = (a*c) / (b*d)
    
    После умножения результат сокращается через НОД для нормализации.
    
    Args:
        a: Первое рациональное число
        b: Второе рациональное число
        
    Returns:
        QNum: Произведение a * b (сокращенная дробь)
        
    Examples:
        >>> a = QNum(ZNum(0, NNum(1, [1])), NNum(1, [2]))  # 1/2
        >>> b = QNum(ZNum(0, NNum(1, [2])), NNum(1, [3]))  # 2/3
        >>> MUL_QQ_Q_f(a, b)
        QNum(ZNum(0, NNum(1, [1])), NNum(1, [3]))  # 1/3
        
    Raises:
        TypeError: Если аргументы не являются объектами QNum
        ValueError: Если знаменатель равен нулю (не должно происходить при корректных QNum)
    """
    # Валидация входных данных
    if a is None or not isinstance(a, QNum):
        raise TypeError("Первый аргумент должен быть типа QNum")
    
    if b is None or not isinstance(b, QNum):
        raise TypeError("Второй аргумент должен быть типа QNum")
    
    # Умножаем числители
    numerator = MUL_ZZ_Z_f(a.num_tor, b.num_tor)
    
    # Умножаем знаменатели
    denominator = MUL_NN_N_f(a.den_tor, b.den_tor)
    
    # Создаем новое рациональное число
    result = QNum(numerator, denominator)
    
    # Сокращаем дробь через НОД
    result = RED_Q_Q_f(result)
    
    return result
