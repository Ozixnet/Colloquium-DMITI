# Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.N.SUB_NDN_N import SUB_NDN_N_f
from modules.N.DIV_NN_Dk import DIV_NN_Dk_f
from modules.N.DIV_NN_N import DIV_NN_N_f


# Функция для теста умножения натуральных чисел (N-8)
def test_for_MUL_NN_N():
    print("Testing MUL_NN_N (N-8)...")
    
    # Умножение на ноль
    result = MUL_NN_N_f(NNum(3, [1, 2, 3]), NNum(1, [0]))
    assert result.n == 1 and result.A == [0]  
    
    result = MUL_NN_N_f(NNum(1, [0]), NNum(4, [4, 5, 6, 7]))
    assert result.n == 1 and result.A == [0] 
    
    # Обычные случаи
    result = MUL_NN_N_f(NNum(1, [5]), NNum(1, [3]))
    assert result.n == 2 and result.A == [5, 1]  
    
    result = MUL_NN_N_f(NNum(2, [2, 1]), NNum(1, [4]))
    assert result.n == 2 and result.A == [8, 4]  
    
    # Умножение с переносами
    result = MUL_NN_N_f(NNum(1, [9]), NNum(1, [9]))
    assert result.n == 2 and result.A == [1, 8] 
    
    print("MUL_NN_N tests passed!")


# Функция для теста вычитания умноженного числа (N-9)
def test_for_SUB_NDN_N():
    print("Testing SUB_NDN_N (N-9)...")
    
    # Обычные случаи
    result = SUB_NDN_N_f(NNum(2, [0, 1]), NNum(1, [2]), 3)
   
    assert result.n == 1 and result.A == [4]
    
    result = SUB_NDN_N_f(NNum(3, [5, 3, 1]), NNum(2, [1, 2]), 2)

    assert result.n == 2 and result.A == [3, 9]
    
    # Вычитание с нулевым результатом
    result = SUB_NDN_N_f(NNum(2, [0, 1]), NNum(1, [5]), 2)

    assert result.n == 1 and result.A == [0]
    
    print("SUB_NDN_N tests passed!")


# Функция для теста вычисления первой цифры деления (N-10)
def test_for_DIV_NN_Dk():
    print("Testing DIV_NN_Dk (N-10)...")
    
    a = NNum(2, [0, 1])  
    b = NNum(1, [3])     

    digit, power = DIV_NN_Dk_f(a, b)
    assert digit == 3 and power == 0, f"Expected (3, 0), got ({digit}, {power})"
    
    a = NNum(3, [0, 0, 1])  
    b = NNum(1, [4])        
    
    digit, power = DIV_NN_Dk_f(a, b)
    assert digit == 2 and power == 1, f"Expected (2, 1), got ({digit}, {power})"
    
    a = NNum(2, [9, 9])  
    b = NNum(1, [1])    
    
    digit, power = DIV_NN_Dk_f(a, b)
    assert digit == 9 and power == 1, f"Expected (9, 1), got ({digit}, {power})"
    
    print("DIV_NN_Dk tests passed!")


# Функция для теста неполного частного (N-11)
def test_for_DIV_NN_N():
    print("Testing DIV_NN_N (N-11)...")
    
    # Простые случаи сначала
    result = DIV_NN_N_f(NNum(2, [0, 1]), NNum(1, [3])) 
    assert result.n == 1 and result.A == [3]
    
    result = DIV_NN_N_f(NNum(3, [5, 3, 1]), NNum(2, [1, 2])) 
    assert result.n == 1 and result.A == [6]
    
    # Деление числа на само себя
    result = DIV_NN_N_f(NNum(3, [7, 8, 9]), NNum(3, [7, 8, 9])) 
    assert result.n == 1 and result.A == [1]
    
    # Деление меньшего числа на большее (должно вернуть 0)
    result = DIV_NN_N_f(NNum(2, [5, 1]), NNum(3, [0, 0, 1])) 
    assert result.n == 1 and result.A == [0]
    
    print("DIV_NN_N tests passed!")


# Запуск всех тестов
def run_all_tests():
    print("Running all tests for modules N-8, N-9, N-10, N-11\n")
    
    test_for_MUL_NN_N()
    test_for_SUB_NDN_N()
    test_for_DIV_NN_Dk()
    test_for_DIV_NN_N()
    
    print("\nAll tests passed successfully!")


# Запуск тестов
if __name__ == "__main__":
    run_all_tests()