# Двойникова Валерия Алексеевна, гр. 4381.

from modules.N.N_NUM import NNum

def MUL_Nk_N_f(num: NNum, k: int) -> NNum:
    """
    Умножает число на 10^k
    Принимает экземпляр класса NNum и (натуральное число)
    k это int >=0, показатель степени 10
    Возвращает новый NNum с цифрами от старшей к младшей
    """
    if not isinstance(k, int) or k < 0:
        raise ValueError("k должно быть натуральным числом >= 0")

    a = num.A[:]        # копируем цифры
    a.extend([0] * k)   # добавляем k нулей в конец (младшие разряды)

    return NNum(len(a), a)
