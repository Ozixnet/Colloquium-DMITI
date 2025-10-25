import pytest
from modules.N.ADD_1N_N import ADD_1N_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f
from modules.N.N_NUM import NNum

# test_ADD_1N_N
def test_add_1n_n_valid_cases():
    assert ADD_1N_N_f(NNum(3, [9,2,1])).A == [0,3,1]
    assert ADD_1N_N_f(NNum(1, [9])).A == [0,1]
    assert ADD_1N_N_f(NNum(4, [7,6,5,4])).A == [8,6,5,4]

def test_add_1n_n_very_large():
    big_num = NNum(1000, [9]*1000)
    result = ADD_1N_N_f(big_num)
    assert result.A == [0]*1000 + [1]

# test_MUL_ND_N_f
def test_mul_nd_n_normal():
    assert MUL_ND_N_f(NNum(3,[3,2,1]), 2).A == [6,4,2]
    assert MUL_ND_N_f(NNum(1,[9]), 9).A == [1,8]

# test_MUL_Nk_N_f
def test_mul_nk_n_normal():
    assert MUL_Nk_N_f(NNum(3,[3,2,1]), 2).A == [0,0,3,2,1]
    assert MUL_Nk_N_f(NNum(1,[9]), 1).A == [0,9]

def test_mul_nk_n_large_number():
    big_num = NNum(1000, [1]*1000)
    result = MUL_Nk_N_f(big_num, 5)
    assert len(result.A) == 1005
    assert result.A[5:] == [1]*1000
    assert result.A[:5] == [0]*5

#valid/invalid tests
def test_nnum_invalid_n():
    with pytest.raises(ValueError):
        NNum(0, [1])  # n < 1
    with pytest.raises(ValueError):
        NNum(-5, [1,2,3])  # n отрицательное

def test_nnum_invalid_length():
    with pytest.raises(ValueError):
        NNum(3, [1,2])  # длина a != n
    with pytest.raises(ValueError):
        NNum(2, [1,2,3])  # длина a != n

def test_nnum_leading_zero():
    with pytest.raises(ValueError):
        NNum(2, [1,0])  # ок, последний 0 допустим только если n=1
    with pytest.raises(ValueError):
        NNum(3, [1,2,0])  # последний 0 при n>1 → ошибка

def test_nnum_invalid_digits():
    with pytest.raises(ValueError):
        NNum(3, [-1,2,3])  # отрицательная цифра
    with pytest.raises(ValueError):
        NNum(3, [1,2,10])  # цифра >9
