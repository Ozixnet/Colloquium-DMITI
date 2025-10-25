from modules.N.N_NUM import NNum
import pytest 
#импортирование тестируемых функций 
from com_nn_d import COM_NN_D
from NZER_N_B import NZER_N_B
from ADD_NN_N import ADD_NN_N
from SUB_NN_N import SUB_NN_N


# Функция для теста сравнения чисел  
def test_for_COM_NN_D():
    # Обычные случаи ( числа стандартных длин )
    assert COM_NN_D(NNum(3, [3, 2, 1]), NNum(3, [3, 2, 1])) == 0
    assert COM_NN_D(NNum(4, [4, 5, 3, 6]), NNum(3, [1,2,3])) == 2
    assert COM_NN_D(NNum(3, [5, 7, 3]), NNum(7, [4, 7, 3, 5, 1, 6, 8])) == 1
    # Случаи с нулем 
    zero = NNum(1, [0])
    assert COM_NN_D(zero, zero) == 0
    assert COM_NN_D(NNum(3, [5, 4, 6]), zero) == 2
    assert COM_NN_D(zero, NNum(3, [3, 5, 2])) == 1
    # Случаи с очень большими числами 
    assert COM_NN_D(NNum(100, [0] + 97*[0] + [2] + [1]), NNum(97, [0] + 94*[0] + [4] + [3])) == 2
    assert COM_NN_D(NNum(101, [0] * 100 + [1]), NNum(100, [9] * 100)) == 2


# Функция для теста проверки числа на ноль 
def test_for_NZER_N_B():
    assert NZER_N_B(NNum(1, [0])) == "нет"
    assert NZER_N_B(NNum(4, [0, 4, 3, 5])) == "да"
    assert NZER_N_B(NNum(100, 99*[0] + [1])) == "да"
    assert NZER_N_B(NNum(1000, [0] * 999 + [1])) == "да"


# Функция для теста суммирования двух чисел 
def test_for_ADD_NN_N():
    # обычные случаи 
    result = ADD_NN_N(NNum(1, [5]), NNum(1, [3]))
    assert result.n == 1 and result.A == [8]  
    
    result = ADD_NN_N(NNum(1, [9]), NNum(1, [1]))
    assert result.n == 2 and result.A == [0, 1]  
    
    result = ADD_NN_N(NNum(2, [5, 1]), NNum(2, [7, 2]))
    assert result.n == 2 and result.A == [2, 4] 
    # большое число 
    result = ADD_NN_N(NNum(100, [0] + 99*[1]), NNum(1, [1]))
    assert result.n == 100 and result.A == 100*[1]

    result = ADD_NN_N(NNum(21, [0] * 20 + [1]), NNum(21, [0] * 20 + [1]))
    assert result.n == 21 and result.A == [0] * 20 + [2]
    
    result = ADD_NN_N(NNum(101, [0] * 100 + [1]), NNum(1, [1]))
    assert result.n == 101 and result.A == [1] + [0] * 99 + [1]
    # суммирование с нулем 
    zero = NNum(1, [0])
    result = ADD_NN_N(zero, zero)
    assert result.n == 1 and result.A == [0]

    result = ADD_NN_N(zero, NNum(3, [5, 6, 2]))
    assert result.n == 3 and result.A == [5, 6, 2]


# Функция для теста вычитания из большего числа меньшее или равное ему 
def test_for_SUB_NN_N():
    # обычные случаи 
    result = SUB_NN_N(NNum(1, [5]), NNum(1, [3]))
    assert result.n == 1 and result.A == [2]  

    result = SUB_NN_N(NNum(2, [0, 1]), NNum(1, [1]))
    assert result.n == 1 and result.A == [9]  

    result = SUB_NN_N(NNum(2, [1, 5]), NNum(2, [7, 2]))
    assert result.n == 2 and result.A == [4, 2]  
    
    # вычитание с заёмом 
    result = SUB_NN_N(NNum(3, [0, 0, 1]), NNum(1, [1]))
    assert result.n == 2 and result.A == [9, 9]  
    
    # одинаковые числа 
    result = SUB_NN_N(NNum(2, [3, 1]), NNum(2, [3, 1]))
    assert result.n == 1 and result.A == [0]  
    
    # большое число 
    result = SUB_NN_N(NNum(100, 99*[0] + [1]), NNum(1, [1]))
    assert result.n == 99 and result.A == [9] * 99

    result = SUB_NN_N(NNum(51, [0] * 50 + [1]), NNum(1, [1]))
    assert result.n == 50 and result.A == [9] * 50
    
    # ноль 
    zero = NNum(1, [0])
    result = SUB_NN_N(NNum(3, [5, 6, 2]), zero)
    assert result.n == 3 and result.A == [5, 6, 2]  
       
    # сложный случай с несколькими заёмами
    result = SUB_NN_N(NNum(3, [0, 0, 2]), NNum(2, [0, 1]))
    assert result.n == 3 and result.A == [0, 9, 1]  


# Запуски функций 
test_for_COM_NN_D()
test_for_NZER_N_B()
test_for_ADD_NN_N()
test_for_SUB_NN_N()