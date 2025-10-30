# Хведынич Варвара Андреевна, гр. 4381

from modules.N.N_NUM import NNum
import pytest


def test_for_valid_NNum():
    # Обычные числа
    zero = NNum(1, [0])
    assert zero.n == 1 and zero.A == [0]  # 0 => корректно

    num = NNum(1, [5])
    assert num.n == 1 and num.A == [5]  # 5 => корректно

    num = NNum(3, [1, 2, 3])
    assert num.n == 3 and num.A == [1, 2, 3]  # 123 => корректно

    num = NNum(5, [9, 8, 7, 6, 5])
    assert num.n == 5 and num.A == [9, 8, 7, 6, 5]  # 56789 => корректно

    # Некорректный ввод 
    with pytest.raises(ValueError):
        NNum(0, [])  # n=0 => ошибка (число должно иметь хотя бы одну цифру)
    
    with pytest.raises(ValueError):
        NNum(-1, [1])  # n=-1 => ошибка (отрицательное количество цифр)

    # Несовпадение вводимой длинны массива и фактической 
    with pytest.raises(ValueError):
        NNum(3, [1, 2])  # n=3, массив[2] => ошибка (длина не совпадает)
    
    with pytest.raises(ValueError):
        NNum(2, [1, 2, 3])  # n=2, массив[3] => ошибка (длина не совпадает)

    # Ведущий ноль
    with pytest.raises(ValueError):
        NNum(3, [1, 2, 0])  # 021 => ошибка (ведущий ноль запрещен)

    # Ввод чисел вместо цифр или отрицательных цифр 
    with pytest.raises(ValueError):
        NNum(2, [1, -1])  # цифра -1 => ошибка (отрицательные цифры запрещены)
    
    with pytest.raises(ValueError):
        NNum(2, [1, 10])  # цифра 10 => ошибка (цифры должны быть 0-9)

test_for_valid_NNum()