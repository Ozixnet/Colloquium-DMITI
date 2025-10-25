#Хведынич Варвара Андреевна, гр. 4381

from modules.N.N_NUM import NNum
from com_nn_d import COM_NN_D

def SUB_NN_N(a: NNum, b: NNum) -> NNum:
    """
    Функция вычитания из большего натуарльного числа 
    меньшее или равное ему натуралдьное число
    a -- первое натуральное число (уменьшаемое, a ≥ b)
    b -- второе натуральное число (вычитаемое)
    """

    if COM_NN_D(a, b) == 1:
        raise ValueError("Первое число должно быть больше или равно второму")
    
    # создание нового массива для результата
    # длина результата <= длина большего числа 
    # borrow -- заем из старешго разряда 
    result_digits = []
    borrow = 0

    # цикл для поразрядного вычитания , начиная смладших разрядов 
    for i in range(a.n):
        digit_a = a.A[i]
        digit_b = b.A[i] if i < b.n else 0

        # происходит вычитание с учетом заема
        # если результат вычиания отрицательный то 
        # занимается десяток 
        tmp_result = digit_a - digit_b - borrow

        if tmp_result < 0:
            tmp_result += 10
            borrow = 1
        else:
            borrow = 0

        result_digits.append(tmp_result)

    result_len = len(result_digits)

    # цикл для удаления ведущих нулей, начиная со старщего разряда 
    while result_len > 1 and result_digits[result_len - 1] == 0:
        result_digits.pop()
        result_len -= 1

    return NNum(result_len, result_digits)