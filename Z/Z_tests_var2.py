import pytest
from ABS_Z_N import ABS_Z_N_f # TODO: импорт позднее прикрутить из адекватной директории!

# -----------------------------------------------------------------------------
# test_ADD_1N_N
# -----------------------------------------------------------------------------

def test_abs_z_n_normal_cases(): # обычные случаи
    result = ABS_Z_N_f({'a': [1, 2, 3], 'sign': 1}) # положительное число
    assert result == {'a': [1, 2, 3]}

    result = ABS_Z_N_f({'a': [4, 5, 6], 'sign': -1}) # отрицательное число
    assert result == {'a': [4, 5, 6]}

def test_abs_z_n_large_number(): # большое число с отрицательным знаком
    big_num = {'a': [9] * 1000, 'sign': -1}
    result = ABS_Z_N_f(big_num)
    assert len(result['a']) == 1000
    assert result['a'] == [9] * 1000

def test_abs_z_n_invalid_cases(): # отлов ошибок
    with pytest.raises(ValueError): # пустой список
        ABS_Z_N_f({'a': [], 'sign': 1})

    with pytest.raises(ValueError): # цифры не int
        ABS_Z_N_f({'a': [1, '2', 3], 'sign': 1})

    with pytest.raises(ValueError): # число не словарь
        ABS_Z_N_f([1, 2, 3])
