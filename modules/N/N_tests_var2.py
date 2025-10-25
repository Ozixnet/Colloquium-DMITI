from modules.N.ADD_1N_N import ADD_1N_N_f
from modules.N.MUL_ND_N import MUL_ND_N_f
from modules.N.MUL_Nk_N import MUL_Nk_N_f
from modules.N.N_NUM import NNum

# test_ADD_1N_N
def test_add_1n_n_valid_cases():
    assert ADD_1N_N_f(NNum(3, [1,2,9])).A == [1,3,0]
    assert ADD_1N_N_f(NNum(1, [9])).A == [1,0]
    assert ADD_1N_N_f(NNum(4, [4,5,6,7])).A == [4,5,6,8]

def test_add_1n_n_very_large():
    big_num = NNum(1000, [9]*1000)
    result = ADD_1N_N_f(big_num)
    assert result.A == [1] + [0]*1000

# test_MUL_ND_N_f
def test_mul_nd_n_normal():
    assert MUL_ND_N_f(NNum(3,[1,2,3]), 2).A == [2,4,6]
    assert MUL_ND_N_f(NNum(1,[9]), 9).A == [8,1]

# test_MUL_Nk_N_f
def test_mul_nk_n_normal():
    assert MUL_Nk_N_f(NNum(3,[1,2,3]), 2).A == [1,2,3,0,0]
    assert MUL_Nk_N_f(NNum(1,[9]), 1).A == [9,0]

def test_mul_nk_n_large_number():
    big_num = NNum(1000, [1]*1000)
    result = MUL_Nk_N_f(big_num, 5)
    assert len(result.A) == 1005
    assert result.A[:1000] == [1]*1000
    assert result.A[-5:] == [0]*5
