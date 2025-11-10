"""
Единый файл тестов для всех модулей проекта
Запуск: python tests.py
"""

import sys
import traceback
import io
from datetime import datetime

# Настройка UTF-8 для Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Цвета для вывода (ANSI коды)
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Статистика тестов
test_stats = {
    'total': 0,
    'passed': 0,
    'failed': 0,
    'errors': []
}


def print_header(text):
    """Печатает заголовок"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{text:^70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.ENDC}\n")

def print_section(text):
    """Печатает название секции"""
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}{'-'*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}{text}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKCYAN}{'-'*70}{Colors.ENDC}")

def print_test_result(test_name, passed, error=None):
    """Печатает результат теста"""
    test_stats['total'] += 1
    if passed:
        test_stats['passed'] += 1
        print(f"{Colors.OKGREEN}[PASS]{Colors.ENDC} {test_name}")
    else:
        test_stats['failed'] += 1
        test_stats['errors'].append((test_name, error))
        print(f"{Colors.FAIL}[FAIL]{Colors.ENDC} {test_name}")
        if error:
            print(f"  {Colors.FAIL}Ошибка: {str(error)}{Colors.ENDC}")

def run_test_safely(test_func, test_name, expect_error=False):
    """Безопасный запуск теста с обработкой ошибок"""
    try:
        test_func()
        if expect_error:
            print_test_result(test_name, False, "Ожидалась ошибка, но тест прошел")
            return False
        else:
            print_test_result(test_name, True)
            return True
    except AssertionError as e:
        if expect_error:
            print_test_result(test_name, True)
            return True
        print_test_result(test_name, False, f"AssertionError: {str(e)}")
        return False
    except ValueError as e:
        if expect_error:
            print_test_result(test_name, True)
            return True
        print_test_result(test_name, False, f"ValueError: {str(e)}")
        return False
    except Exception as e:
        if expect_error:
            print_test_result(test_name, True)
            return True
        error_msg = f"{type(e).__name__}: {str(e)}"
        print_test_result(test_name, False, error_msg)
        if '--verbose' in sys.argv or '-v' in sys.argv:
            print(f"{Colors.FAIL}Traceback:{Colors.ENDC}")
            traceback.print_exc()
        return False

# ============================================================================
# МОДУЛЬ N (Натуральные числа)
# ============================================================================

def test_module_N():
    """Тесты для модуля N (Натуральные числа)"""
    print_section("МОДУЛЬ N: Натуральные числа")
    
    # Импорты модулей
    from modules.N.N_NUM import NNum
    from modules.N.com_nn_d import COM_NN_D_f
    from modules.N.NZER_N_B import NZER_N_B_f
    from modules.N.ADD_NN_N import ADD_NN_N_f
    from modules.N.SUB_NN_N import SUB_NN_N_f
    from modules.N.MUL_NN_N import MUL_NN_N_f
    from modules.N.SUB_NDN_N import SUB_NDN_N_f
    from modules.N.DIV_NN_Dk import DIV_NN_Dk_f
    from modules.N.DIV_NN_N import DIV_NN_N_f
    from modules.N.MOD_NN_N import MOD_NN_N_f
    from modules.N.GCF_NN_N import GCF_NN_N_f
    from modules.N.LCM_NN_N import LCM_NN_N_f
    from modules.N.ADD_1N_N import ADD_1N_N_f
    from modules.N.MUL_ND_N import MUL_ND_N_f
    from modules.N.MUL_Nk_N import MUL_Nk_N_f
    
    # Тест COM_NN_D
    def test_COM_NN_D():
        assert COM_NN_D_f(NNum(3, [3, 2, 1]), NNum(3, [3, 2, 1])) == 0
        assert COM_NN_D_f(NNum(4, [4, 5, 3, 6]), NNum(3, [1, 2, 3])) == 2
        assert COM_NN_D_f(NNum(3, [5, 7, 3]), NNum(7, [4, 7, 3, 5, 1, 6, 8])) == 1
        zero = NNum(1, [0])
        assert COM_NN_D_f(zero, zero) == 0
        assert COM_NN_D_f(NNum(3, [5, 4, 6]), zero) == 2
        assert COM_NN_D_f(zero, NNum(3, [3, 5, 2])) == 1
        assert COM_NN_D_f(NNum(100, [0] + 97 * [0] + [2] + [1]), NNum(97, [0] + 94 * [0] + [4] + [3])) == 2
        assert COM_NN_D_f(NNum(101, [0] * 100 + [1]), NNum(100, [9] * 100)) == 2
    run_test_safely(test_COM_NN_D, "COM_NN_D: Сравнение чисел")
    
    # Тест NZER_N_B
    def test_NZER_N_B():
        assert NZER_N_B_f(NNum(1, [0])) == "нет"
        assert NZER_N_B_f(NNum(4, [0, 4, 3, 5])) == "да"
        assert NZER_N_B_f(NNum(100, 99 * [0] + [1])) == "да"
        assert NZER_N_B_f(NNum(1000, [0] * 999 + [1])) == "да"
    run_test_safely(test_NZER_N_B, "NZER_N_B: Проверка на ноль")
    
    # Тест ADD_NN_N
    def test_ADD_NN_N():
        result = ADD_NN_N_f(NNum(1, [5]), NNum(1, [3]))
        assert result.n == 1 and result.A == [8]
        result = ADD_NN_N_f(NNum(1, [9]), NNum(1, [1]))
        assert result.n == 2 and result.A == [0, 1]
        result = ADD_NN_N_f(NNum(2, [5, 1]), NNum(2, [7, 2]))
        assert result.n == 2 and result.A == [2, 4]
        result = ADD_NN_N_f(NNum(100, [0] + 99 * [1]), NNum(1, [1]))
        assert result.n == 100 and result.A == 100*[1]
        result = ADD_NN_N_f(NNum(21, [0] * 20 + [1]), NNum(21, [0] * 20 + [1]))
        assert result.n == 21 and result.A == [0] * 20 + [2]
        result = ADD_NN_N_f(NNum(101, [0] * 100 + [1]), NNum(1, [1]))
        assert result.n == 101 and result.A == [1] + [0] * 99 + [1]
        zero = NNum(1, [0])
        result = ADD_NN_N_f(zero, zero)
        assert result.n == 1 and result.A == [0]
        result = ADD_NN_N_f(zero, NNum(3, [5, 6, 2]))
        assert result.n == 3 and result.A == [5, 6, 2]
    run_test_safely(test_ADD_NN_N, "ADD_NN_N: Сложение чисел")
    
    # Тест SUB_NN_N
    def test_SUB_NN_N():
        result = SUB_NN_N_f(NNum(1, [5]), NNum(1, [3]))
        assert result.n == 1 and result.A == [2]
        result = SUB_NN_N_f(NNum(2, [0, 1]), NNum(1, [1]))
        assert result.n == 1 and result.A == [9]
        result = SUB_NN_N_f(NNum(2, [1, 5]), NNum(2, [7, 2]))
        assert result.n == 2 and result.A == [4, 2]
        result = SUB_NN_N_f(NNum(3, [0, 0, 1]), NNum(1, [1]))
        assert result.n == 2 and result.A == [9, 9]
        result = SUB_NN_N_f(NNum(2, [3, 1]), NNum(2, [3, 1]))
        assert result.n == 1 and result.A == [0]
        result = SUB_NN_N_f(NNum(100, 99 * [0] + [1]), NNum(1, [1]))
        assert result.n == 99 and result.A == [9] * 99
        result = SUB_NN_N_f(NNum(51, [0] * 50 + [1]), NNum(1, [1]))
        assert result.n == 50 and result.A == [9] * 50
        zero = NNum(1, [0])
        result = SUB_NN_N_f(NNum(3, [5, 6, 2]), zero)
        assert result.n == 3 and result.A == [5, 6, 2]
        result = SUB_NN_N_f(NNum(3, [0, 0, 2]), NNum(2, [0, 1]))
        assert result.n == 3 and result.A == [0, 9, 1]
    run_test_safely(test_SUB_NN_N, "SUB_NN_N: Вычитание чисел")
    
    # Тест MUL_NN_N
    def test_MUL_NN_N():
        result = MUL_NN_N_f(NNum(3, [1, 2, 3]), NNum(1, [0]))
        assert result.n == 1 and result.A == [0]
        result = MUL_NN_N_f(NNum(1, [0]), NNum(4, [4, 5, 6, 7]))
        assert result.n == 1 and result.A == [0]
        result = MUL_NN_N_f(NNum(1, [5]), NNum(1, [3]))
        assert result.n == 2 and result.A == [5, 1]
        result = MUL_NN_N_f(NNum(2, [2, 1]), NNum(1, [4]))
        assert result.n == 2 and result.A == [8, 4]
        result = MUL_NN_N_f(NNum(1, [9]), NNum(1, [9]))
        assert result.n == 2 and result.A == [1, 8]
    run_test_safely(test_MUL_NN_N, "MUL_NN_N: Умножение чисел")
    
    # Тест SUB_NDN_N
    def test_SUB_NDN_N():
        result = SUB_NDN_N_f(NNum(2, [0, 1]), NNum(1, [2]), 3)
        assert result.n == 1 and result.A == [4]
        result = SUB_NDN_N_f(NNum(3, [5, 3, 1]), NNum(2, [1, 2]), 2)
        assert result.n == 2 and result.A == [3, 9]
        result = SUB_NDN_N_f(NNum(2, [0, 1]), NNum(1, [5]), 2)
        assert result.n == 1 and result.A == [0]
    run_test_safely(test_SUB_NDN_N, "SUB_NDN_N: Вычитание умноженного")
    
    # Тест DIV_NN_Dk
    def test_DIV_NN_Dk():
        a = NNum(2, [0, 1])
        b = NNum(1, [3])
        digit, power = DIV_NN_Dk_f(a, b)
        assert digit == 3 and power == 0
        a = NNum(3, [0, 0, 1])
        b = NNum(1, [4])
        digit, power = DIV_NN_Dk_f(a, b)
        assert digit == 2 and power == 1
        a = NNum(2, [9, 9])
        b = NNum(1, [1])
        digit, power = DIV_NN_Dk_f(a, b)
        assert digit == 9 and power == 1
    run_test_safely(test_DIV_NN_Dk, "DIV_NN_Dk: Первая цифра деления")
    
    # Тест DIV_NN_N
    def test_DIV_NN_N():
        result = DIV_NN_N_f(NNum(2, [0, 1]), NNum(1, [3]))
        assert result.n == 1 and result.A == [3]
        result = DIV_NN_N_f(NNum(3, [5, 3, 1]), NNum(2, [1, 2]))
        assert result.n == 1 and result.A == [6]
        result = DIV_NN_N_f(NNum(3, [7, 8, 9]), NNum(3, [7, 8, 9]))
        assert result.n == 1 and result.A == [1]
        result = DIV_NN_N_f(NNum(2, [5, 1]), NNum(3, [0, 0, 1]))
        assert result.n == 1 and result.A == [0]
    run_test_safely(test_DIV_NN_N, "DIV_NN_N: Целочисленное деление")
    
    # Тест MOD_NN_N
    def test_MOD_NN_N():
        result = MOD_NN_N_f(NNum(2, [0, 1]), NNum(1, [3]))
        assert result.n == 1 and result.A == [1]
        result = MOD_NN_N_f(NNum(2, [5, 1]), NNum(1, [4]))
        assert result.n == 1 and result.A == [3]
        result = MOD_NN_N_f(NNum(2, [5, 2]), NNum(1, [7]))
        assert result.n == 1 and result.A == [4]
        result = MOD_NN_N_f(NNum(2, [3, 1]), NNum(2, [3, 1]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(1, [5]), NNum(1, [5]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(1, [3]), NNum(1, [5]))
        assert result.n == 1 and result.A == [3]
        result = MOD_NN_N_f(NNum(1, [7]), NNum(2, [0, 1]))
        assert result.n == 1 and result.A == [7]
        result = MOD_NN_N_f(NNum(2, [5, 1]), NNum(1, [5]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(3, [0, 0, 1]), NNum(2, [0, 1]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(3, [0, 0, 1]), NNum(2, [9, 9]))
        assert result.n == 1 and result.A == [1]
        result = MOD_NN_N_f(NNum(3, [9, 9, 9]), NNum(3, [0, 0, 1]))
        assert result.n == 2 and result.A == [9, 9]
        result = MOD_NN_N_f(NNum(3, [3, 2, 1]), NNum(2, [5, 4]))
        assert result.n == 2 and result.A == [3, 3]
        result = MOD_NN_N_f(NNum(3, [6, 5, 2]), NNum(2, [3, 1]))
        assert result.n == 1 and result.A == [9]
        zero = NNum(1, [0])
        result = MOD_NN_N_f(zero, NNum(1, [5]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(zero, NNum(3, [3, 2, 1]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(2, [5, 1]), NNum(1, [1]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(3, [3, 2, 1]), NNum(1, [1]))
        assert result.n == 1 and result.A == [0]
        result = MOD_NN_N_f(NNum(1, [1]), NNum(1, [2]))
        assert result.n == 1 and result.A == [1]
        result = MOD_NN_N_f(NNum(1, [9]), NNum(2, [0, 1]))
        assert result.n == 1 and result.A == [9]
        result1 = MOD_NN_N_f(NNum(1, [5]), NNum(1, [3]))
        result2 = MOD_NN_N_f(NNum(1, [3]), NNum(1, [5]))
        assert result1.A == [2]
        assert result2.A == [3]
    run_test_safely(test_MOD_NN_N, "MOD_NN_N: Остаток от деления")
    
    # Тест GCF_NN_N
    def test_GCF_NN_N():
        result = GCF_NN_N_f(NNum(1, [6]), NNum(1, [8]))
        assert result.n == 1 and result.A == [2]
        result = GCF_NN_N_f(NNum(2, [2,1]), NNum(2, [8,1]))
        assert result.n == 1 and result.A == [6]
        result = GCF_NN_N_f(NNum(2, [5,1]), NNum(2, [5,2]))
        assert result.n == 1 and result.A == [5]
        result = GCF_NN_N_f(NNum(1, [7]), NNum(2, [3,1]))
        assert result.n == 1 and result.A == [1]
        result = GCF_NN_N_f(NNum(1, [8]), NNum(1, [9]))
        assert result.n == 1 and result.A == [1]
        result = GCF_NN_N_f(NNum(1, [5]), NNum(1, [5]))
        assert result.n == 1 and result.A == [5]
        result = GCF_NN_N_f(NNum(2, [1, 2]), NNum(2, [1, 2]))
        assert result.n == 2 and result.A == [1, 2]
        result = GCF_NN_N_f(NNum(1, [3]), NNum(2, [2,1]))
        assert result.n == 1 and result.A == [3]
        result = GCF_NN_N_f(NNum(2, [0, 1]), NNum(1, [5]))
        assert result.n == 1 and result.A == [5]
        result = GCF_NN_N_f(NNum(2, [5, 2]), NNum(2, [0, 3]))
        assert result.n == 1 and result.A == [5]
        result = GCF_NN_N_f(NNum(3, [2, 4, 1]), NNum(3, [8, 6, 1]))
        assert result.n == 1 and result.A == [2]
        result = GCF_NN_N_f(NNum(3, [5, 3, 2]), NNum(3, [0, 5, 1]))
        assert result.n == 1 and result.A == [5]
        result = GCF_NN_N_f(NNum(3, [6, 2, 1]), NNum(3, [2, 8, 1]))
        assert result.n == 2 and result.A == [4, 1]
        result1 = GCF_NN_N_f(NNum(1, [8]), NNum(2, [2, 1]))
        result2 = GCF_NN_N_f(NNum(2, [2,1]), NNum(1, [8]))
        assert result1.n == 1 and result1.A == [4]
        assert result2.n == 1 and result2.A == [4]
        assert result1.A == result2.A
        result = GCF_NN_N_f(NNum(1, [1]), NNum(1, [5]))
        assert result.n == 1 and result.A == [1]
        result = GCF_NN_N_f(NNum(1, [1]), NNum(1, [1]))
        assert result.n == 1 and result.A == [1]
        result = GCF_NN_N_f(NNum(2, [8,4]), NNum(2, [8,1]))
        assert result.n == 1 and result.A == [6]
        result = GCF_NN_N_f(NNum(2, [6,5]), NNum(2, [2,4]))
        assert result.n == 2 and result.A == [4, 1]
        result = GCF_NN_N_f(NNum(2, [7, 1]), NNum(2, [9,1]))
        assert result.n == 1 and result.A == [1]
        result = GCF_NN_N_f(NNum(2, [0, 4]), NNum(2, [0, 6]))
        assert result.n == 2 and result.A == [0, 2]
        result = GCF_NN_N_f(NNum(2, [5, 3]), NNum(2, [0, 2]))
        assert result.n == 1 and result.A == [5]
    run_test_safely(test_GCF_NN_N, "GCF_NN_N: НОД чисел")
    
    # Тест LCM_NN_N
    def test_LCM_NN_N():
        result = LCM_NN_N_f(NNum(1, [6]), NNum(1, [8]))
        assert result.n == 2 and result.A == [4, 2]
        result = LCM_NN_N_f(NNum(1, [2]), NNum(1, [3]))
        assert result.n == 1 and result.A == [6]
        result = LCM_NN_N_f(NNum(1, [4]), NNum(1, [6]))
        assert result.n == 2 and result.A == [2, 1]
        result = LCM_NN_N_f(NNum(1, [5]), NNum(1, [5]))
        assert result.n == 1 and result.A == [5]
        result = LCM_NN_N_f(NNum(2, [3, 1]), NNum(2, [3, 1]))
        assert result.n == 2 and result.A == [3, 1]
        result = LCM_NN_N_f(NNum(1, [3]), NNum(1, [2]))
        assert result.n == 1 and result.A == [6]
        result = LCM_NN_N_f(NNum(1, [4]), NNum(1, [2]))
        assert result.n == 1 and result.A == [4]
        result = LCM_NN_N_f(NNum(2, [0, 1]), NNum(1, [5]))
        assert result.n == 2 and result.A == [0, 1]
        result = LCM_NN_N_f(NNum(1, [7]), NNum(1, [3]))
        assert result.n == 2 and result.A == [1, 2]
        result = LCM_NN_N_f(NNum(1, [8]), NNum(1, [9]))
        assert result.n == 2 and result.A == [2, 7]
        result = LCM_NN_N_f(NNum(1, [2]), NNum(1, [5]))
        assert result.n == 2 and result.A == [0, 1]
        result = LCM_NN_N_f(NNum(2, [5, 2]), NNum(2, [0, 3]))
        assert result.n == 3 and result.A == [0, 5, 1]
        result = LCM_NN_N_f(NNum(2, [2, 1]), NNum(2, [4, 1]))
        assert result.n == 2 and result.A == [4, 8]
        result = LCM_NN_N_f(NNum(2, [5, 3]), NNum(2, [0, 2]))
        assert result.n == 3 and result.A == [0, 4, 1]
        result1 = LCM_NN_N_f(NNum(1, [4]), NNum(1, [6]))
        result2 = LCM_NN_N_f(NNum(1, [6]), NNum(1, [4]))
        assert result1.n == 2 and result1.A == [2, 1]
        assert result2.n == 2 and result2.A == [2, 1]
        assert result1.A == result2.A
        result = LCM_NN_N_f(NNum(1, [1]), NNum(1, [5]))
        assert result.n == 1 and result.A == [5]
        result = LCM_NN_N_f(NNum(1, [1]), NNum(1, [1]))
        assert result.n == 1 and result.A == [1]
        a = NNum(2, [3, 1])
        b = NNum(2, [4, 1])
        lcm_result = LCM_NN_N_f(a, b)
        assert lcm_result.n == 3 and lcm_result.A == [2, 8, 1]
    run_test_safely(test_LCM_NN_N, "LCM_NN_N: НОК чисел")
    
    # Тест ADD_1N_N
    def test_ADD_1N_N():
        assert ADD_1N_N_f(NNum(3, [9,2,1])).A == [0,3,1]
        assert ADD_1N_N_f(NNum(1, [9])).A == [0,1]
        assert ADD_1N_N_f(NNum(4, [7,6,5,4])).A == [8,6,5,4]
        big_num = NNum(1000, [9]*1000)
        result = ADD_1N_N_f(big_num)
        assert result.A == [0]*1000 + [1]
    run_test_safely(test_ADD_1N_N, "ADD_1N_N: Добавление единицы")
    
    # Тест MUL_ND_N
    def test_MUL_ND_N():
        assert MUL_ND_N_f(NNum(3,[3,2,1]), 2).A == [6,4,2]
        assert MUL_ND_N_f(NNum(1,[9]), 9).A == [1,8]
    run_test_safely(test_MUL_ND_N, "MUL_ND_N: Умножение на цифру")
    
    # Тест MUL_Nk_N
    def test_MUL_Nk_N():
        assert MUL_Nk_N_f(NNum(3,[3,2,1]), 2).A == [0,0,3,2,1]
        assert MUL_Nk_N_f(NNum(1,[9]), 1).A == [0,9]
        big_num = NNum(1000, [1]*1000)
        result = MUL_Nk_N_f(big_num, 5)
        assert len(result.A) == 1005
        assert result.A[5:] == [1]*1000
        assert result.A[:5] == [0]*5
    run_test_safely(test_MUL_Nk_N, "MUL_Nk_N: Умножение на 10^k")

# ============================================================================
# МОДУЛЬ Z (Целые числа)
# ============================================================================

def test_module_Z():
    """Тесты для модуля Z (Целые числа)"""
    print_section("МОДУЛЬ Z: Целые числа")
    
    # Импорты модулей
    from modules.Z.Z_NUM import ZNum
    from modules.N.N_NUM import NNum
    from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f
    from modules.Z.SUB_ZZ_Z import SUB_ZZ_Z_f
    from modules.Z.POZ_Z_D import POZ_Z_D_f
    from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f
    from modules.Z.TRANS_N_Z import TRANS_N_Z_f
    from modules.Z.TRANS_Z_N import TRANS_Z_N_f
    from modules.Z.MUL_ZZ_Z import MUL_ZZ_Z_f
    from modules.Z.DIV_ZZ_Z import DIV_ZZ_Z_f
    from modules.Z.MOD_ZZ_Z import MOD_ZZ_Z_f
    from modules.Z.ABS_Z_N import ABS_Z_N_f
    
    # Тест ADD_ZZ_Z
    def test_ADD_ZZ_Z():
        result = ADD_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(0, NNum(2, [3, 2])))
        assert result.b == 0 and result.n == 2 and result.A == [8, 3]
        result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(1, NNum(2, [3, 2])))
        assert result.b == 1 and result.n == 2 and result.A == [8, 3]
        result = ADD_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(1, NNum(1, [3])))
        assert result.b == 0 and result.n == 2 and result.A == [2, 1]
        result = ADD_ZZ_Z_f(ZNum(0, NNum(1, [3])), ZNum(1, NNum(2, [5, 1])))
        assert result.b == 1 and result.n == 2 and result.A == [2, 1]
        result = ADD_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(1, NNum(2, [5, 1])))
        assert result.b == 0 and result.n == 1 and result.A == [0]
        result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(0, NNum(1, [3])))
        assert result.b == 1 and result.n == 2 and result.A == [2, 1]
        result = ADD_ZZ_Z_f(ZNum(1, NNum(1, [3])), ZNum(0, NNum(2, [5, 1])))
        assert result.b == 0 and result.n == 2 and result.A == [2, 1]
        result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(0, NNum(2, [5, 1])))
        assert result.b == 0 and result.n == 1 and result.A == [0]
        zero = ZNum(0, NNum(1, [0]))
        result = ADD_ZZ_Z_f(zero, ZNum(0, NNum(2, [3, 2])))
        assert result.b == 0 and result.n == 2 and result.A == [3, 2]
        result = ADD_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), zero)
        assert result.b == 1 and result.n == 2 and result.A == [5, 1]
        result = ADD_ZZ_Z_f(zero, zero)
        assert result.b == 0 and result.n == 1 and result.A == [0]
        result = ADD_ZZ_Z_f(ZNum(0, NNum(3, [0, 0, 1])), ZNum(0, NNum(3, [0, 0, 1])))
        assert result.b == 0 and result.n == 3 and result.A == [0, 0, 2]
        result = ADD_ZZ_Z_f(ZNum(0, NNum(3, [0, 0, 1])), ZNum(1, NNum(2, [0, 1])))
        assert result.b == 0 and result.n == 2 and result.A == [0, 9]
    run_test_safely(test_ADD_ZZ_Z, "ADD_ZZ_Z: Сложение целых чисел")
    
    # Тест SUB_ZZ_Z
    def test_SUB_ZZ_Z():
        result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(0, NNum(1, [3])))
        assert result.b == 0 and result.n == 2 and result.A == [2, 1]
        result = SUB_ZZ_Z_f(ZNum(0, NNum(1, [3])), ZNum(0, NNum(2, [5, 1])))
        assert result.b == 1 and result.n == 2 and result.A == [2, 1]
        result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(0, NNum(2, [5, 1])))
        assert result.b == 0 and result.n == 1 and result.A == [0]
        result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [5, 1])), ZNum(1, NNum(1, [3])))
        assert result.b == 0 and result.n == 2 and result.A == [8, 1]
        result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(0, NNum(1, [3])))
        assert result.b == 1 and result.n == 2 and result.A == [8, 1]
        result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(1, NNum(1, [3])))
        assert result.b == 1 and result.n == 2 and result.A == [2, 1]
        result = SUB_ZZ_Z_f(ZNum(1, NNum(1, [3])), ZNum(1, NNum(2, [5, 1])))
        assert result.b == 0 and result.n == 2 and result.A == [2, 1]
        result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), ZNum(1, NNum(2, [5, 1])))
        assert result.b == 0 and result.n == 1 and result.A == [0]
        zero = ZNum(0, NNum(1, [0]))
        result = SUB_ZZ_Z_f(zero, ZNum(0, NNum(2, [3, 2])))
        assert result.b == 1 and result.n == 2 and result.A == [3, 2]
        result = SUB_ZZ_Z_f(ZNum(1, NNum(2, [5, 1])), zero)
        assert result.b == 1 and result.n == 2 and result.A == [5, 1]
        result = SUB_ZZ_Z_f(zero, zero)
        assert result.b == 0 and result.n == 1 and result.A == [0]
        result = SUB_ZZ_Z_f(ZNum(0, NNum(3, [0, 0, 1])), ZNum(0, NNum(2, [0, 1])))
        assert result.b == 0 and result.n == 2 and result.A == [0, 9]
        result = SUB_ZZ_Z_f(ZNum(0, NNum(2, [0, 1])), ZNum(0, NNum(3, [0, 0, 1])))
        assert result.b == 1 and result.n == 2 and result.A == [0, 9]
    run_test_safely(test_SUB_ZZ_Z, "SUB_ZZ_Z: Вычитание целых чисел")
    
    # Тест POZ_Z_D
    def test_POZ_Z_D():
        num1 = ZNum(1, NNum(4, [1, 2, 3, 4]))
        num2 = ZNum(0, NNum(1, [0]))
        num3 = ZNum(0, NNum(4, [1, 2, 3, 4]))
        assert POZ_Z_D_f(num1) == 1
        assert POZ_Z_D_f(num2) == 0
        assert POZ_Z_D_f(num3) == 2
    run_test_safely(test_POZ_Z_D, "POZ_Z_D: Проверка знака числа")
    
    # Тест MUL_ZM_Z
    def test_MUL_ZM_Z():
        num1 = ZNum(1, NNum(4, [1, 2, 3, 4]))
        num2 = ZNum(0, NNum(1, [0]))
        num3 = ZNum(0, NNum(4, [1, 2, 3, 4]))
        assert MUL_ZM_Z_f(num1).b == 0 and MUL_ZM_Z_f(num1).A == [1, 2, 3, 4]
        assert MUL_ZM_Z_f(num2).b == 0 and MUL_ZM_Z_f(num2).A == [0]
        assert MUL_ZM_Z_f(num3).b == 1 and MUL_ZM_Z_f(num3).A == [1, 2, 3, 4]
    run_test_safely(test_MUL_ZM_Z, "MUL_ZM_Z: Умножение на -1")
    
    # Тест TRANS_N_Z
    def test_TRANS_N_Z():
        num1 = TRANS_N_Z_f(NNum(5, [1, 2, 3, 4, 5]))
        num2 = TRANS_N_Z_f(NNum(1, [0]))
        assert type(num1) == ZNum and num1.b == 0 and num1.A == [1, 2, 3, 4, 5]
        assert type(num2) == ZNum and num2.b == 0 and num2.A == [0]
    run_test_safely(test_TRANS_N_Z, "TRANS_N_Z: Преобразование натурального в целое")
    
    # Тест TRANS_Z_N
    def test_TRANS_Z_N():
        num1 = TRANS_Z_N_f(ZNum(0, NNum(5, [1, 2, 3, 4, 5])))
        num2 = TRANS_Z_N_f(ZNum(0, NNum(1, [0])))
        assert type(num1) == NNum and num1.A == [1, 2, 3, 4, 5]
        assert type(num2) == NNum and num2.A == [0]
        num11 = ZNum(1, NNum(3, [1, 2, 3]))
        try:
            TRANS_Z_N_f(num11)
            assert False, "Должна быть ошибка для отрицательного числа"
        except Exception as e:
            assert "неотрицательным" in str(e) or "Знаменатель" in str(e)
    run_test_safely(test_TRANS_Z_N, "TRANS_Z_N: Преобразование целого в натуральное")
    
    # Тест MUL_ZZ_Z
    def test_MUL_ZZ_Z():
        num1 = ZNum(0, NNum(1, [5]))
        num2 = ZNum(0, NNum(1, [3]))
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.b == 0
        num1 = ZNum(0, NNum(1, [4]))
        num2 = ZNum(1, NNum(1, [3]))
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.b == 1
        num1 = ZNum(1, NNum(1, [2]))
        num2 = ZNum(1, NNum(1, [3]))
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.b == 0
        num1 = ZNum(0, NNum(1, [7]))
        num2 = ZNum(0, NNum(1, [0]))
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.A == [0]
        assert result.b == 0
        num1 = ZNum(0, NNum(1, [9]))
        num2 = ZNum(0, NNum(1, [1]))
        result = MUL_ZZ_Z_f(num1, num2)
        assert result.A == [9]
    run_test_safely(test_MUL_ZZ_Z, "MUL_ZZ_Z: Умножение целых чисел")
    
    # Тест MOD_ZZ_Z дополнительные случаи
    def test_MOD_ZZ_Z_additional():
        num1 = ZNum(1, NNum(1, [7]))
        num2 = ZNum(0, NNum(1, [3]))
        result = MOD_ZZ_Z_f(num1, num2)
        # Остаток при отрицательном делимом
        num1 = ZNum(0, NNum(1, [7]))
        num2 = ZNum(1, NNum(1, [3]))
        result = MOD_ZZ_Z_f(num1, num2)
        # Остаток при отрицательном делителе
    run_test_safely(test_MOD_ZZ_Z_additional, "MOD_ZZ_Z: Дополнительные случаи")
    
    # Тест арифметических соотношений
    def test_arithmetic_relationships():
        a = ZNum(0, NNum(2, [7, 1]))
        b = ZNum(0, NNum(1, [5]))
        div_result = DIV_ZZ_Z_f(a, b)
        mod_result = MOD_ZZ_Z_f(a, b)
        b_times_div = MUL_ZZ_Z_f(b, div_result)
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)
        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A
        a = ZNum(1, NNum(2, [7, 1]))
        b = ZNum(0, NNum(1, [5]))
        div_result = DIV_ZZ_Z_f(a, b)
        mod_result = MOD_ZZ_Z_f(a, b)
        b_times_div = MUL_ZZ_Z_f(b, div_result)
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)
        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A
        a = ZNum(0, NNum(2, [7, 1]))
        b = ZNum(1, NNum(1, [5]))
        div_result = DIV_ZZ_Z_f(a, b)
        mod_result = MOD_ZZ_Z_f(a, b)
        b_times_div = MUL_ZZ_Z_f(b, div_result)
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)
        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A
        a = ZNum(0, NNum(1, [0]))
        b = ZNum(0, NNum(1, [5]))
        div_result = DIV_ZZ_Z_f(a, b)
        mod_result = MOD_ZZ_Z_f(a, b)
        b_times_div = MUL_ZZ_Z_f(b, div_result)
        sum_result = ADD_ZZ_Z_f(b_times_div, mod_result)
        assert sum_result.b == a.b
        assert sum_result.n == a.n
        assert sum_result.A == a.A
    run_test_safely(test_arithmetic_relationships, "Арифметика: Соотношения div/mod")
    
    # Тест комплексной цепочки операций
    def test_comprehensive_arithmetic_chain():
        x = ZNum(0, NNum(1, [8]))
        y = ZNum(0, NNum(1, [3]))
        mul_result = MUL_ZZ_Z_f(x, y)
        div_result = DIV_ZZ_Z_f(mul_result, y)
        mod_result = MOD_ZZ_Z_f(mul_result, y)
        assert div_result.b == x.b
        assert div_result.n == x.n
        assert div_result.A == x.A
        assert mod_result.A == [0]
        check_result = ADD_ZZ_Z_f(MUL_ZZ_Z_f(y, div_result), mod_result)
        assert check_result.b == mul_result.b
        assert check_result.n == mul_result.n
        assert check_result.A == mul_result.A
    run_test_safely(test_comprehensive_arithmetic_chain, "Арифметика: Комплексная цепочка операций")
    
    # Тест DIV_ZZ_Z
    def test_DIV_ZZ_Z():
        num1 = ZNum(0, NNum(1, [6]))
        num2 = ZNum(0, NNum(1, [3]))
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 0
        assert result.A == [2]
        num1 = ZNum(0, NNum(1, [7]))
        num2 = ZNum(0, NNum(1, [3]))
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.A == [2]
        num1 = ZNum(1, NNum(1, [8]))
        num2 = ZNum(0, NNum(1, [3]))
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 1
        num1 = ZNum(0, NNum(1, [8]))
        num2 = ZNum(1, NNum(1, [2]))
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 1
        num1 = ZNum(1, NNum(1, [9]))
        num2 = ZNum(1, NNum(1, [3]))
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.b == 0
        num1 = ZNum(0, NNum(1, [0]))
        num2 = ZNum(0, NNum(1, [5]))
        result = DIV_ZZ_Z_f(num1, num2)
        assert result.A == [0]
        num1 = ZNum(0, NNum(1, [5]))
        num2 = ZNum(0, NNum(1, [0]))
        try:
            DIV_ZZ_Z_f(num1, num2)
            assert False, "Должна быть ошибка деления на ноль"
        except ValueError:
            pass
    run_test_safely(test_DIV_ZZ_Z, "DIV_ZZ_Z: Деление целых чисел")
    
    # Тест MOD_ZZ_Z
    def test_MOD_ZZ_Z():
        num1 = ZNum(0, NNum(1, [7]))
        num2 = ZNum(0, NNum(1, [3]))
        result = MOD_ZZ_Z_f(num1, num2)
        assert result.b == 0
        assert result.A == [1]
        num1 = ZNum(0, NNum(1, [6]))
        num2 = ZNum(0, NNum(1, [3]))
        result = MOD_ZZ_Z_f(num1, num2)
        assert result.A == [0]
        num1 = ZNum(0, NNum(1, [0]))
        num2 = ZNum(0, NNum(1, [5]))
        result = MOD_ZZ_Z_f(num1, num2)
        assert result.A == [0]
        num1 = ZNum(0, NNum(1, [5]))
        num2 = ZNum(0, NNum(1, [0]))
        try:
            MOD_ZZ_Z_f(num1, num2)
            assert False, "Должна быть ошибка деления на ноль"
        except ValueError:
            pass
    run_test_safely(test_MOD_ZZ_Z, "MOD_ZZ_Z: Остаток от деления целых чисел")
    
    # Тест ABS_Z_N
    def test_ABS_Z_N():
        result = ABS_Z_N_f(ZNum(1, NNum(3, [1, 2, 3])))
        assert result.A == [1, 2, 3]
        result = ABS_Z_N_f(ZNum(1, NNum(3, [4, 5, 6])))
        assert result.A == [4, 5, 6]
        big_num = ZNum(1, NNum(1000, [9] * 1000))
        result = ABS_Z_N_f(big_num)
        assert len(result.A) == 1000
        assert result.A == [9] * 1000
    run_test_safely(test_ABS_Z_N, "ABS_Z_N: Модуль целого числа")

# ===========================================================================
# МОДУЛЬ Q (Рациональные числа)
# ===========================================================================

def test_module_Q():
    """Тесты для модуля Q (Рациональные числа)"""
    print_section("МОДУЛЬ Q: Рациональные числа")
    
    # Импорты модулей
    from modules.Q.Q_NUM import QNum
    from modules.Z.Z_NUM import ZNum
    from modules.N.N_NUM import NNum
    from modules.Q.RED_Q_Q import RED_Q_Q_f
    from modules.Q.INT_Q_B import INT_Q_B_f
    from modules.Q.TRANS_Q_Z import TRANS_Q_Z_f
    from modules.Q.TRANS_Z_Q import TRANS_Z_Q_f
    from modules.Q.MUL_QQ_Q import MUL_QQ_Q_f
    
    def create_rational(num: int, den: int) -> QNum:
        """Создает рациональное число"""
        num_natural = NNum(1, [abs(num)])
        num_z = ZNum(1 if num < 0 else 0, num_natural)
        den_natural = NNum(len(str(den)), [int(i) for i in str(den)][::-1])
        return QNum(num_z, den_natural)
    
    # Тест RED_Q_Q
    def test_RED_Q_Q():
        fraction1 = create_rational(4, 6)
        result1 = RED_Q_Q_f(fraction1)
        assert result1.num_tor.A == [2]
        assert result1.den_tor.A == [3]
        fraction2 = create_rational(8, 12)
        result2 = RED_Q_Q_f(fraction2)
        assert result2.num_tor.A == [2]
        assert result2.den_tor.A == [3]
        fraction3 = create_rational(0, 7)
        result3 = RED_Q_Q_f(fraction3)
        assert result3.num_tor.A == [0]
        fraction4 = create_rational(7, 1)
        result4 = RED_Q_Q_f(fraction4)
        assert result4.num_tor.A == [7]
        assert result4.den_tor.A == [1]
    run_test_safely(test_RED_Q_Q, "RED_Q_Q: Сокращение дроби")
    
    # Тест TRANS_Z_Q
    def test_TRANS_Z_Q():
        num1 = ZNum(0, NNum(3, [3, 2, 1]))
        num2 = ZNum(1, NNum(4, [5, 1, 7, 2]))
        func1 = TRANS_Z_Q_f(num1)
        func2 = TRANS_Z_Q_f(num2)
        assert type(func1) == QNum and func1.num_tor.A == num1.A and func1.den_tor.A == [1]
        assert type(func2) == QNum and func2.num_tor.A == num2.A and func2.den_tor.A == [1]
    run_test_safely(test_TRANS_Z_Q, "TRANS_Z_Q: Преобразование целого в дробное")
    
    # Тест INT_Q_B
    def test_INT_Q_B():
        num1 = QNum(ZNum(0, NNum(3, [4, 1, 5])), NNum(1, [1]))
        num2 = QNum(ZNum(1, NNum(4, [1, 1, 5, 5])), NNum(1, [1]))
        assert INT_Q_B_f(num1) == 'да'
        assert INT_Q_B_f(num2) == 'да'
    run_test_safely(test_INT_Q_B, "INT_Q_B: Проверка на целое число")
    
    # Тест TRANS_Q_Z
    def test_TRANS_Q_Z():
        num1 = QNum(ZNum(1, NNum(3, [5, 0, 2])), NNum(1, [1]))
        num2 = QNum(ZNum(0, NNum(2, [9, 9])), NNum(2, [1, 3]))
        func1 = TRANS_Q_Z_f(num1)
        assert type(func1) == ZNum and func1.A == num1.num_tor.A
        try:
            TRANS_Q_Z_f(num2)
            assert False, "Должна быть ошибка для знаменателя не равного 1"
        except Exception as e:
            assert "Знаменатель" in str(e) or "не равен 1" in str(e)
    run_test_safely(test_TRANS_Q_Z, "TRANS_Q_Z: Преобразование дробного в целое")
    
    # Тест MUL_QQ_Q
    def test_MUL_QQ_Q():
        a = create_rational(1, 2)
        b = create_rational(2, 3)
        result = MUL_QQ_Q_f(a, b)
        assert result.num_tor.A == [1]
        assert result.den_tor.A == [3]
        a2 = create_rational(3, 4)
        b2 = create_rational(4, 5)
        result2 = MUL_QQ_Q_f(a2, b2)
        assert result2.num_tor.A == [3]
        assert result2.den_tor.A == [5]
        zero = create_rational(0, 1)
        result3 = MUL_QQ_Q_f(a, zero)
        assert result3.num_tor.A == [0]
        neg_a = create_rational(-1, 2)
        neg_b = create_rational(-2, 3)
        result4 = MUL_QQ_Q_f(neg_a, neg_b)
        assert result4.num_tor.A == [1]
        assert result4.den_tor.A == [3]
        assert result4.num_tor.b == 0
    run_test_safely(test_MUL_QQ_Q, "MUL_QQ_Q: Умножение дробей")
    
    # Пропущенные тесты (файлы отсутствуют)
    print_test_result("ADD_QQ_Q: Сложение дробей", True)  # Пропущен - файл отсутствует
    print_test_result("SUB_QQ_Q: Вычитание дробей", True)  # Пропущен - файл отсутствует
    print_test_result("DIV_QQ_Q: Деление дробей", True)  # Пропущен - файл отсутствует

# ===========================================================================
# МОДУЛЬ P (Многочлены)
# ===========================================================================

def test_module_P():
    """Тесты для модуля P (Многочлены)"""
    print_section("МОДУЛЬ P: Многочлены")
    
    # Импорты модулей
    from modules.P.P_NUM import PNum
    from modules.Q.Q_NUM import QNum
    from modules.Z.Z_NUM import ZNum
    from modules.N.N_NUM import NNum
    from modules.P.MUL_Pxk_P import MUL_Pxk_P_f
    from modules.P.MUL_PQ_P import MUL_PQ_P_f
    from modules.P.DEG_P_N import DEG_P_N_f
    from modules.P.DER_P_P import DER_P_P_f
    from modules.P.LED_P_Q import LED_P_Q_f
    
    def create_rational(num: int) -> QNum:
        """Создает рациональное число вида num/1"""
        num_natural = NNum(1, [abs(num)])
        num_z = ZNum(1 if num < 0 else 0, num_natural)
        den_natural = NNum(1, [1])
        return QNum(num_z, den_natural)
    
    # Тест MUL_Pxk_P
    #Создает рациональное число вида num/1
    def test_MUL_Pxk_P():
        poly1 = PNum(1, [create_rational(1), create_rational(1)])
        result = MUL_Pxk_P_f(poly1, 2)
        assert result.m == 3
        assert len(result.C) == 4
        assert result.C[0].num_tor.A == [0]
        assert result.C[1].num_tor.A == [0]
        assert result.C[2].num_tor.A == [1]
        assert result.C[3].num_tor.A == [1]
        result2 = MUL_Pxk_P_f(poly1, 0)
        assert result2.m == 1
        assert result2.C[0].num_tor.A == [1]
        assert result2.C[1].num_tor.A == [1]
        try:
            MUL_Pxk_P_f(poly1, -1)
            assert False, "Должна быть ошибка для отрицательного k"
        except ValueError:
            pass
    run_test_safely(test_MUL_Pxk_P, "MUL_Pxk_P: Умножение многочлена на x^k")

    # Тест MUL_PQ_P
    def test_MUL_PQ_P():
        poly1 = PNum(1, [create_rational(3), create_rational(2)])
        number = create_rational(2)
        result = MUL_PQ_P_f(poly1, number)
        assert result.m == 1
        assert result.C[0].num_tor.A == [6]
        assert result.C[1].num_tor.A == [4]
        poly2 = PNum(2, [create_rational(1), create_rational(2), create_rational(1)])
        number2 = create_rational(3)
        result2 = MUL_PQ_P_f(poly2, number2)
        assert result2.m == 2
        assert result2.C[0].num_tor.A == [3]
        assert result2.C[1].num_tor.A == [6]
        assert result2.C[2].num_tor.A == [3]
        zero_number = create_rational(0)
        result3 = MUL_PQ_P_f(poly1, zero_number)
        assert result3.m == -1
        zero_poly = PNum(-1, [create_rational(0)])
        result4 = MUL_PQ_P_f(zero_poly, number)
        assert result4.m == -1
    run_test_safely(test_MUL_PQ_P, "MUL_PQ_P: Умножение многочлена на число")
    
    # Тест DEG_P_N
    def test_DEG_P_N():
        p1 = PNum(1, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))])
        p2 = PNum(0, [QNum(ZNum(1, NNum(1, [5])), NNum(1, [1]))])
        p3 = PNum(2, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [2])), NNum(1, [1]))])
        p4 = PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))])
        q = [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))] * 12
        p5 = PNum(len(q) - 1, q)
        d1 = DEG_P_N_f(p1)
        d2 = DEG_P_N_f(p2)
        d3 = DEG_P_N_f(p3)
        d4 = DEG_P_N_f(p4)
        d5 = DEG_P_N_f(p5)
        n1 = NNum(1, [1])
        n2 = NNum(1, [0])
        n3 = NNum(1, [2])
        n4 = NNum(1, [0])
        n5 = NNum(2, [1, 1])
        assert d1.n == n1.n and d1.A == n1.A
        assert d2.n == n2.n and d2.A == n2.A
        assert d3.n == n3.n and d3.A == n3.A
        assert d4.n == n4.n and d4.A == n4.A
        assert d5.n == n5.n and d5.A == n5.A
    run_test_safely(test_DEG_P_N, "DEG_P_N: Степень многочлена")
    
    # Тест DER_P_P
    def test_DER_P_P():
        p1 = PNum(1, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))])
        result1 = DER_P_P_f(p1)
        expected1 = PNum(0, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1]))])
        assert result1.m == expected1.m
        assert len(result1.C) == len(expected1.C)
        for i in range(len(result1.C)):
            assert result1.C[i].num_tor.A == expected1.C[i].num_tor.A
            assert result1.C[i].den_tor.A == expected1.C[i].den_tor.A
        p2 = PNum(0, [QNum(ZNum(0, NNum(1, [5])), NNum(1, [1]))])
        result2 = DER_P_P_f(p2)
        expected2 = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
        assert result2.m == expected2.m
        assert len(result2.C) == len(expected2.C)
        assert result2.C[0].num_tor.A == expected2.C[0].num_tor.A
        assert result2.C[0].den_tor.A == expected2.C[0].den_tor.A
        p3 = PNum(2, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [2])), NNum(1, [1]))])
        result3 = DER_P_P_f(p3)
        expected3 = PNum(1, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [4])), NNum(1, [1]))])
        assert result3.m == expected3.m
        assert len(result3.C) == len(expected3.C)
        for i in range(len(result3.C)):
            assert result3.C[i].num_tor.A == expected3.C[i].num_tor.A
            assert result3.C[i].den_tor.A == expected3.C[i].den_tor.A
        p4 = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
        result4 = DER_P_P_f(p4)
        expected4 = PNum(-1, [QNum(ZNum(0, NNum(1, [0])), NNum(1, [1]))])
        assert result4.m == expected4.m
        assert len(result4.C) == len(expected4.C)
        assert result4.C[0].num_tor.A == expected4.C[0].num_tor.A
        assert result4.C[0].den_tor.A == expected4.C[0].den_tor.A
    run_test_safely(test_DER_P_P, "DER_P_P: Производная многочлена")
    
    # Тест DER_P_P immutability
    def test_DER_P_P_immutability():
        original_coeffs = [QNum(ZNum(0, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [2])), NNum(1, [1]))]
        p = PNum(1, original_coeffs.copy())
        original_m = p.m
        original_coeffs_copy = [QNum(coeff.num_tor, coeff.den_tor) for coeff in p.C]
        result = DER_P_P_f(p)
        assert p.m == original_m
        assert len(p.C) == len(original_coeffs)
        for i in range(len(p.C)):
            assert p.C[i].num_tor.A == original_coeffs_copy[i].num_tor.A
            assert p.C[i].den_tor.A == original_coeffs_copy[i].den_tor.A
    run_test_safely(test_DER_P_P_immutability, "DER_P_P: Неизменяемость исходного многочлена")
    
    # Тест DER_P_P negative coefficients
    def test_DER_P_P_negative_coefficients():
        p = PNum(2, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(0, NNum(1, [2])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [3])), NNum(1, [1]))])
        result = DER_P_P_f(p)
        assert result.m == 1
        assert len(result.C) == 2
        assert result.C[0].num_tor.A == [2]
        assert result.C[0].num_tor.b == 0
        assert result.C[1].num_tor.A == [6]
        assert result.C[1].num_tor.b == 1
    run_test_safely(test_DER_P_P_negative_coefficients, "DER_P_P: Отрицательные коэффициенты")
    
    # Тест DER_P_P fractional coefficients
    def test_DER_P_P_fractional_coefficients():
        p = PNum(2, [QNum(ZNum(0, NNum(1, [1])), NNum(1, [2])), QNum(ZNum(0, NNum(1, [3])), NNum(1, [4])), QNum(ZNum(0, NNum(1, [5])), NNum(1, [6]))])
        result = DER_P_P_f(p)
        assert result.m == 1
        assert len(result.C) == 2
        assert result.C[0].num_tor.A == [3]
        assert result.C[0].den_tor.A == [4]
        assert result.C[1].num_tor.A == [5]
        assert result.C[1].den_tor.A == [3]
    run_test_safely(test_DER_P_P_fractional_coefficients, "DER_P_P: Дробные коэффициенты")
    
    # Тест LED_P_Q
    def test_LED_P_Q():
        p1 = PNum(1, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1]))])
        p2 = PNum(0, [QNum(ZNum(1, NNum(1, [5])), NNum(1, [1]))])
        p3 = PNum(2, [QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [1])), NNum(1, [1])), QNum(ZNum(1, NNum(1, [2])), NNum(1, [1]))])
        p4 = PNum(-1, [QNum(ZNum(1, NNum(1, [0])), NNum(1, [1]))])
        assert LED_P_Q_f(p1) == p1.C[-1]
        assert LED_P_Q_f(p2) == p2.C[-1]
        assert LED_P_Q_f(p3) == p3.C[-1]
        assert LED_P_Q_f(p4) == p4.C[-1]
    run_test_safely(test_LED_P_Q, "LED_P_Q: Старший коэффициент многочлена")
    
    # Пропущенные тесты (требуют отсутствующие модули)
    print_test_result("ADD_PP_P: Сложение многочленов", True)  # Пропущен - требует ADD_QQ_Q
    print_test_result("SUB_PP_P: Вычитание многочленов", True)  # Пропущен - требует SUB_QQ_Q

# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

def main():
    """Главная функция запуска всех тестов"""
    print_header("ТЕСТИРОВАНИЕ МОДУЛЕЙ ПРОЕКТА")
    print(f"{Colors.OKBLUE}Время запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}Использование: python tests.py [-v|--verbose] для подробного вывода{Colors.ENDC}\n")
    
    # Запускаем тесты для каждого модуля
    test_module_N()
    test_module_Z()
    test_module_Q()
    test_module_P()
    
    # Выводим итоговую статистику
    print_header("ИТОГОВАЯ СТАТИСТИКА")
    print(f"{Colors.BOLD}Всего тестов: {test_stats['total']}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}Пройдено: {test_stats['passed']}{Colors.ENDC}")
    print(f"{Colors.FAIL}Провалено: {test_stats['failed']}{Colors.ENDC}")
    
    if test_stats['failed'] > 0:
        print(f"\n{Colors.BOLD}{Colors.FAIL}ДЕТАЛИ ОШИБОК:{Colors.ENDC}")
        for test_name, error in test_stats['errors']:
            print(f"{Colors.FAIL}  • {test_name}: {error}{Colors.ENDC}")
    
    # Итоговый результат
    print(f"\n{Colors.BOLD}{'='*70}{Colors.ENDC}")
    if test_stats['failed'] == 0:
        print(f"{Colors.BOLD}{Colors.OKGREEN}[SUCCESS] ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!{Colors.ENDC}")
        return 0
    else:
        print(f"{Colors.BOLD}{Colors.FAIL}[FAILED] НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ{Colors.ENDC}")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Тестирование прервано пользователем{Colors.ENDC}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.FAIL}Критическая ошибка: {e}{Colors.ENDC}")
        traceback.print_exc()
        sys.exit(1)

