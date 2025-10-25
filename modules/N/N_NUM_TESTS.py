from modules.N.N_NUM import NNum
import pytest


def test_for_valid_NNum():
    # Обычные числа
    zero = NNum(1, [0])
    assert zero.n == 1 and zero.A == [0]

    num = NNum(1, [5])
    assert num.n == 1 and num.A == [5]

    num = NNum(3, [1, 2, 3])
    assert num.n == 3 and num.A == [1, 2, 3]

    num = NNum(5, [9, 8, 7, 6, 5])
    assert num.n == 5 and num.A == [9, 8, 7, 6, 5]

    # Некорректный ввод 
    with pytest.raises(ValueError):
        NNum(0, []) 
    
    with pytest.raises(ValueError):
        NNum(-1, [1])  

    # Несовпадение вводимой длинны массива и фактической 
    with pytest.raises(ValueError):
        NNum(3, [1, 2]) 
    
    with pytest.raises(ValueError):
        NNum(2, [1, 2, 3])  

    # Ведущий ноль
    with pytest.raises(ValueError):
        NNum(3, [1, 2, 0]) 

    # Ввод чисел вместо цифр или отрицательных цифр 
    with pytest.raises(ValueError):
        NNum(2, [1, -1]) 
    
    with pytest.raises(ValueError):
        NNum(2, [1, 10])  
    

test_for_valid_NNum()