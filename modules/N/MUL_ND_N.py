# Двойникова Валерия Алексеевна, гр. 4381.

from modules.N.N_NUM import NNum


def MUL_ND_N_f(num: NNum, k: int) -> NNum:
    if not isinstance(k, int) or k < 0 or k > 9: #<-- Добавил проверку на цифру до 9
        raise ValueError("k должно быть натуральным числом от 0 до 9")
    if k == 0:
        return NNum(1,[0]) # проверка на ноль

    a = num.A
    result = []
    carry = 0

    for digit in a:
        total = digit * k + carry
        result.append(total % 10)
        carry = total // 10

    while carry:
        result.append(carry % 10)
        carry //= 10

    return NNum(len(result), result)
