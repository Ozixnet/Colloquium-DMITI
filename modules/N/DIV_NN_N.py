#Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.com_nn_d import COM_NN_D_f
from modules.N.DIV_NN_Dk import DIV_NN_Dk_f
from modules.N.SUB_NDN_N import SUB_NDN_N_f
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f

def DIV_NN_N_f(a: NNum, b: NNum) -> NNum:
    """
    Неполное частное от деления первого натурального числа на второе
    с остатком (делитель отличен от нуля).
    
    a - делимое
    b - делитель (не ноль)
    
    Возврат - NNum (неполное частное)
    """
    
    # Проверка, что делитель не ноль
    if b.n == 1 and b.A[0] == 0:
        raise ValueError("Division by zero")
    
    # Если a < b, возвращаем 0 (COM_NN_D)
    if COM_NN_D_f(a, b) == 1:
        return NNum(1, [0])
    
    # Начинаем с частного = 0
    quotient = NNum(1, [0])
    remainder = a
    
    # Пока остаток >= b
    while COM_NN_D_f(remainder, b) >= 0:
        try:
            # Находим следующую цифру и ее позицию (DIV_NN_Dk)
            digit, power = DIV_NN_Dk_f(remainder, b)
        except ValueError:
            # Если remainder стал меньше b, выходим из цикла
            break
        
        if digit == 0:
            break
        
        # Создаем число, которое представляет digit на позиции power
        # (это эквивалентно digit * 10^power)
        digit_value = NNum(1, [digit])
        if power > 0:
            digit_at_position = MUL_Nk_N_f(digit_value, power)
        else:
            digit_at_position = digit_value
        
        # Добавляем эту цифру к частному (ADD_NN_N)
        quotient = ADD_NN_N_f(quotient, digit_at_position)
        
        # Вычитаем из остатка b * digit * 10^power
        # Правильный способ: создаем b * 10^power, затем умножаем на digit
        b_shifted = MUL_Nk_N_f(b, power)
        b_times_digit = MUL_ND_N_f(b_shifted, digit)
        
        # Вычитаем из остатка (SUB_NN_N)
        remainder = SUB_NN_N_f(remainder, b_times_digit)
    
    return quotient