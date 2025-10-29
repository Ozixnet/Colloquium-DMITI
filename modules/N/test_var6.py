#Землякова Анастасия, гр. 4381

from modules.N.N_NUM import NNum
from modules.N.MUL_NN_N import MUL_NN_N_f
from modules.N.SUB_NDN_N import SUB_NDN_N_f
from modules.N.DIV_NN_Dk import DIV_NN_Dk_f
from modules.N.DIV_NN_N import DIV_NN_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.N.com_nn_d import COM_NN_D_f

# Функция для N-8
def test_for_MUL_NN_N():
    print("Testing MUL_NN_N (N-8)...")
    
    # Умножение на ноль
    result = MUL_NN_N_f(NNum(3, [1, 2, 3]), NNum(1, [0]))
    assert result.n == 1 and result.A == [0]  # 321 * 0 = 0
    
    result = MUL_NN_N_f(NNum(1, [0]), NNum(4, [4, 5, 6, 7]))
    assert result.n == 1 and result.A == [0]  # 0 * 7654 = 0
    
    # Обычные случаи - УЧТЕН ФОРМАТ [младший_разряд, старший_разряд]
    result = MUL_NN_N_f(NNum(1, [5]), NNum(1, [3]))
    assert result.n == 2 and result.A == [5, 1]  # 5 * 3 = 15 -> [5, 1]
    
    result = MUL_NN_N_f(NNum(2, [2, 1]), NNum(1, [4]))
    assert result.n == 2 and result.A == [8, 4]  # 12 * 4 = 48 -> [8, 4]
    
    # Умножение с переносами
    result = MUL_NN_N_f(NNum(1, [9]), NNum(1, [9]))
    assert result.n == 2 and result.A == [1, 8]  # 9 * 9 = 81 -> [1, 8]
    
    # Простые случаи для избежания ошибок
    result = MUL_NN_N_f(NNum(2, [0, 1]), NNum(1, [2]))
    assert result.n == 2 and result.A == [0, 2]  # 10 * 2 = 20 -> [0, 2]
    
    print("MUL_NN_N tests passed!")

# Функция для N-9
def test_for_SUB_NDN_N():
    print("Testing SUB_NDN_N (N-9)...")
    
    # Обычные случаи
    result = SUB_NDN_N_f(NNum(2, [0, 1]), NNum(1, [2]), 3)
    # 10 - (2 * 3) = 10 - 6 = 4
    assert result.n == 1 and result.A == [4]
    
    result = SUB_NDN_N_f(NNum(3, [5, 3, 1]), NNum(2, [1, 2]), 2)
    # 135 - (21 * 2) = 135 - 42 = 93 -> [3, 9]
    assert result.n == 2 and result.A == [3, 9]
    
    # Вычитание с нулевым результатом
    result = SUB_NDN_N_f(NNum(2, [0, 1]), NNum(1, [5]), 2)
    # 10 - (5 * 2) = 10 - 10 = 0
    assert result.n == 1 and result.A == [0]
    
    print("SUB_NDN_N tests passed!")

# Функция для N-10
def test_for_DIV_NN_Dk():
    print("Testing DIV_NN_Dk (N-10)...")
    
    # Тест 1: 10 ÷ 3 = 3 (digit=3, power=0)
    a = NNum(2, [0, 1])  # 10 (единицы: 0, десятки: 1)
    b = NNum(1, [3])     # 3
    print(f"Test 1: 10 ÷ 3")
    
    digit, power = DIV_NN_Dk_f(a, b)
    print(f"Final Result: digit={digit}, power={power}")
    
    # Проверим, что результат корректен
    temp1 = MUL_ND_N_f(b, digit)
    temp2 = MUL_Nk_N_f(temp1, power)
    print(f"Verification: {b.A}×{digit}×10^{power} = {temp2.A}")
    
    assert digit == 3 and power == 0, f"Expected (3, 0), got ({digit}, {power})"
    
    print("DIV_NN_Dk tests passed!")

# Функция для N-11
def test_for_DIV_NN_N():
    print("Testing DIV_NN_N (N-11)...")
    
    # Деление на 1
    result = DIV_NN_N_f(NNum(3, [4, 5, 6]), NNum(1, [1]))
    # 654 ÷ 1 = 654
    assert result.n == 3 and result.A == [4, 5, 6]
    
    # Обычные случаи
    result = DIV_NN_N_f(NNum(2, [0, 1]), NNum(1, [3]))
    # 10 ÷ 3 = 3
    assert result.n == 1 and result.A == [3]
    
    result = DIV_NN_N_f(NNum(3, [5, 3, 1]), NNum(2, [1, 2]))
    # 135 ÷ 21 = 6
    assert result.n == 1 and result.A == [6]
    
    # Деление числа на само себя
    result = DIV_NN_N_f(NNum(3, [7, 8, 9]), NNum(3, [7, 8, 9]))
    # 987 ÷ 987 = 1
    assert result.n == 1 and result.A == [1]
    
    # Деление меньшего числа на большее (должно вернуть 0)
    result = DIV_NN_N_f(NNum(2, [5, 1]), NNum(3, [0, 0, 1]))
    # 15 ÷ 100 = 0
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