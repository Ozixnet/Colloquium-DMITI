import pytest
from ADD_1N_N import ADD_1N_N_f # TODO: импорт позднее прикрутить из адекватной директории!
from MUL_ND_N import MUL_ND_N_f
from MUL_Nk_N import MUL_Nk_N_f

# -----------------------------------------------------------------------------
# test_ADD_1N_N
# -----------------------------------------------------------------------------

def test_add_1n_n_valid_cases(): # тестирование обычных случаев
    # 129 в 130
    result = ADD_1N_N_f({'n': 3, 'a': [1, 2, 9]})
    assert result == {'n': 3, 'a': [1, 3, 0]}

    # 9 в 10
    result = ADD_1N_N_f({'n': 1, 'a': [9]})
    assert result == {'n': 2, 'a': [1, 0]}

    # 4567 в 4568
    result = ADD_1N_N_f({'n': 4, 'a': [4, 5, 6, 7]})
    assert result == {'n': 4, 'a': [4, 5, 6, 8]}

def test_add_1n_n_very_large(): # тестирование большого числа
    # 999…999 (1000 разрядов) => 1000...0001
    big_num = {'n': 1000, 'a': [9] * 1000}
    result = ADD_1N_N_f(big_num)
    expected = {'n': 1001, 'a': [1] + [0] * 1000}
    assert result == expected

def test_add_1n_n_invalid_cases(): # отлов ошибок
    with pytest.raises(ValueError):
        ADD_1N_N_f({})  # пустой словарь
    with pytest.raises(ValueError):
        ADD_1N_N_f({'n': 0, 'a': []})  # n=0, пустой список
    with pytest.raises(ValueError):
        ADD_1N_N_f({'n': 2, 'a': [1, 12]})  # цифра >9
    with pytest.raises(ValueError):
        ADD_1N_N_f({'n': 2, 'a': [1, -1]})  # цифра <0
    with pytest.raises(ValueError):
        ADD_1N_N_f({'n': 2, 'a': [1, '2']})  # не int
    with pytest.raises(ValueError):
        ADD_1N_N_f({'a': []})  # отсутствует n


# -----------------------------------------------------------------------------
# test_MUL_ND_N_f
# -----------------------------------------------------------------------------

def test_mul_nd_n_very_large():
    big_num = {'a': [9] * 1000} # 999...999 (1000 цифр) * 9 в 8999...991
    result = MUL_ND_N_f(big_num, 9)
    expected = [8] + [9] * 999 + [1]
    assert result == {'a': expected}

    # 123456789... (в общем 1000 цифр) * 5
    big_num = {'a': [i % 10 for i in range(1, 1001)]}  # [1,2,3,...,0,1,2,...]
    result = MUL_ND_N_f(big_num, 5)

    assert result['a'][0] in range(0, 10) # проверяем только длину и первый/последний разряды для быстрого теста
    assert result['a'][-1] in range(0, 10)
    assert len(result['a']) >= 1000

def test_mul_nd_n_large_edge_cases():
    big_zero = {'a': [0] * 500} # 0 * 9 = 0
    result = MUL_ND_N_f(big_zero, 9)
    assert all(d == 0 for d in result['a'])

    one_digit = {'a': [1]} # 1 * 9 = 9
    result = MUL_ND_N_f(one_digit, 9)
    assert result == {'a': [9]}

def test_mul_nd_n_invalid_large_numbers():
    big_invalid = {'a': [9] * 999 + ['a']} # не int в списке большого числа
    with pytest.raises(ValueError):
        MUL_ND_N_f(big_invalid, 3)

    big_num = {'a': [1] * 100} # k не цифра
    with pytest.raises(ValueError):
        MUL_ND_N_f(big_num, 11)

# -----------------------------------------------------------------------------
# test_MUL_Nk_N_f
# -----------------------------------------------------------------------------

def test_mul_nk_n_normal_cases():
    result = MUL_Nk_N_f({'a': [1, 2, 3]}, 2) # 123 * 10^2 = 12300
    assert result == {'a': [1, 2, 3, 0, 0]}

    result = MUL_Nk_N_f({'a': [9]}, 1) # 9 * 10^1 = 90
    assert result == {'a': [9, 0]}

    result = MUL_Nk_N_f({'a': [4, 5, 6, 7]}, 0) # 4567 * 10^0 = 4567 (ничего не меняется)
    assert result == {'a': [4, 5, 6, 7]}

def test_mul_nk_n_large_number():
    big_num = {'a': [1] * 1000} # очень большое число (1000 цифр) * 10^5, то есть 1005 цифр
    result = MUL_Nk_N_f(big_num, 5)
    assert len(result['a']) == 1005
    assert result['a'][:1000] == [1] * 1000
    assert result['a'][-5:] == [0] * 5

def test_mul_nk_n_invalid():
    with pytest.raises(ValueError): # пустой список
        MUL_Nk_N_f({'a': []}, 3)

    with pytest.raises(ValueError): # k отрицательный
        MUL_Nk_N_f({'a': [1, 2, 3]}, -1)

    with pytest.raises(ValueError): # k не int
        MUL_Nk_N_f({'a': [1, 2, 3]}, '2')

    with pytest.raises(ValueError): # число некорректное
        MUL_Nk_N_f({'a': [1, -1, 2]}, 2)