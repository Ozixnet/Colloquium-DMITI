# Двойникова Валерия Алексеевна, гр. 4381.

from modules.N.N_NUM import NNum

def MUL_ND_N_f(num: NNum, k: int) -> NNum:
    """
    Умножает натуральное число на одну цифру (от 0 до 9).
    Принимает экземпляр класса NNum и цифру k,
    возвращает новый экземпляр NNum с результатом умножения.
    Поддерживает корректную обработку переноса разрядов (то есть carry)
    """
    if not isinstance(k, int) or k < 0:
        raise ValueError("k должно быть натуральным числом >= 0")

    a = num.A[::-1]
    result = []
    carry = 0

    for digit in a:
        total = digit * k + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    result.reverse()
    return NNum(len(result), result)
