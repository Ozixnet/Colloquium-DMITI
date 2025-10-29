# Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.com_nn_d import COM_NN_D_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f


def DIV_NN_Dk_f(a: NNum, b: NNum) -> tuple[int, int]:
    """
    Вычисление первой цифры деления большего натурального на меньшее,
    домноженное на 10^k, где k - номер позиции этой цифры (номер считается с нуля).

    a - делимое (большее натуральное число).

    b - делитель (меньшее натуральное число).

    Возврат - tuple (digit, power), где:
        digit - найденная цифра (0-9)
        power - степень 10^k
    """

    # Проверка, что первое число больше или равно второму
    if COM_NN_D_f(a, b) == 1:
        raise ValueError("Первое число должно быть больше или равно второму")

    # Если числа равны, возвращаем (1, 0)
    if COM_NN_D_f(a, b) == 0:
        return (1, 0)

    # Определяем начальную степень k (разница в количестве цифр)
    k = a.n - b.n

    # Корректируем k: умножаем b на 10^k и проверяем, не превышает ли a
    b_shifted = MUL_Nk_N_f(b, k)
    if COM_NN_D_f(a, b_shifted) == 1:
        # Если a < (b * 10^k), уменьшаем k
        k -= 1

    # Подбираем цифру от 9 до 1
    # Ищем максимальную цифру, при которой (b * digit * 10^k) <= a
    for digit in range(9, 0, -1):
        # Умножаем b на digit (MUL_ND_N)
        b_times_digit = MUL_ND_N_f(b, digit)
        
        # Умножаем на 10^k (MUL_Nk_N)
        temp_result = MUL_Nk_N_f(b_times_digit, k)
        
        # Проверяем условие (COM_NN_D)
        comparison = COM_NN_D_f(a, temp_result)
        if comparison == 2 or comparison == 0:  # a >= (b * digit * 10^k)
            return (digit, k)

    return (0, k)