# Хведынич Варвара Андреевна, гр. 4381

from modules.P.P_NUM import PNum
from modules.Q.Q_NUM import QNum
from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum

from modules.P.ADD_PP_P import ADD_PP_P_f
from modules.P.SUB_PP_P import SUB_PP_P_f
from modules.P.MUL_PQ_P import MUL_PQ_P_f

# вспомогательная функция 
def create_rational(num: int) -> QNum:
    #Создает рациональное число вида num/1
    num_natural = NNum(1, [abs(num)])
    num_z = ZNum(1 if num < 0 else 0, num_natural)
    den_natural = NNum(1, [1])
    return QNum(num_z, den_natural)

# Тест сложения полиномов
def test_for_ADD_PP_P():
    # (x + 1) + (2x + 3) = 3x + 4
    poly1 = PNum(1, [create_rational(1), create_rational(1)])  
    poly2 = PNum(1, [create_rational(3), create_rational(2)]) 
    result = ADD_PP_P_f(poly1, poly2)
    assert result.m == 1  
    # проверка коэффициентов 0 -- свободный, 1 -- при большей степени 
    assert result.C[0].num_tor.A == [4] 
    assert result.C[1].num_tor.A == [3] 

    # (2x**2 + 3x + 1) + (x + 2) = 2x**2 + 4x + 3
    poly3 = PNum(2, [create_rational(1), create_rational(3), create_rational(2)]) 
    poly4 = PNum(1, [create_rational(2), create_rational(1)]) 
    result2 = ADD_PP_P_f(poly3, poly4)
    assert result2.m == 2  
    # проверка коэффициентов 0 -- свободный, 2 -- при большей степени 
    assert result2.C[0].num_tor.A == [3] 
    assert result2.C[1].num_tor.A == [4]  
    assert result2.C[2].num_tor.A == [2] 

    # 0 + (x + 1) = (x + 1)
    zero_poly = PNum(-1, [create_rational(0)])
    result3 = ADD_PP_P_f(zero_poly, poly1)
    assert result3.m == 1
    assert result3.C[0].num_tor.A == [1]
    assert result3.C[1].num_tor.A == [1]


# Тест вычитания полиномов
def test_for_SUB_PP_P():
    # (3x + 4) - (x + 1) = 2x + 3
    poly1 = PNum(1, [create_rational(4), create_rational(3)])  
    poly2 = PNum(1, [create_rational(1), create_rational(1)])  
    result = SUB_PP_P_f(poly1, poly2)
    assert result.m == 1
    assert result.C[0].num_tor.A == [3]  
    assert result.C[1].num_tor.A == [2]  

    # (2x**2 + 4x + 3) - (x + 2) = 2x**2 + 3x + 1
    poly3 = PNum(2, [create_rational(3), create_rational(4), create_rational(2)])  
    poly4 = PNum(1, [create_rational(2), create_rational(1)])  
    result2 = SUB_PP_P_f(poly3, poly4)
    assert result2.m == 2
    assert result2.C[0].num_tor.A == [1] 
    assert result2.C[1].num_tor.A == [3]
    assert result2.C[2].num_tor.A == [2]  

    # (3x + 4) - 0 = (3x + 4)
    zero_poly = PNum(-1, [create_rational(0)])
    result3 = SUB_PP_P_f(poly1, zero_poly)
    assert result3.m == 1
    assert result3.C[0].num_tor.A == [4]
    assert result3.C[1].num_tor.A == [3]

# Тест умножения полинома на число
def test_for_MUL_PQ_P():
    # (2x + 3) * 2 = 4x + 6
    poly1 = PNum(1, [create_rational(3), create_rational(2)])  
    number = create_rational(2)
    result = MUL_PQ_P_f(poly1, number)
    assert result.m == 1
    assert result.C[0].num_tor.A == [6]  
    assert result.C[1].num_tor.A == [4]  

    # (x**2 + 2x + 1) * 3 = 3x**2 + 6x + 3
    poly2 = PNum(2, [create_rational(1), create_rational(2), create_rational(1)])  
    number2 = create_rational(3)
    result2 = MUL_PQ_P_f(poly2, number2)
    assert result2.m == 2
    assert result2.C[0].num_tor.A == [3]  
    assert result2.C[1].num_tor.A == [6]  
    assert result2.C[2].num_tor.A == [3]  

    # Умножение на 0 = нулевой полином
    zero_number = create_rational(0)
    result3 = MUL_PQ_P_f(poly1, zero_number)
    assert result3.m == -1  # нулевой полином

    # Умножение нулевого полинома на число = нулевой полином
    zero_poly = PNum(-1, [create_rational(0)])
    result4 = MUL_PQ_P_f(zero_poly, number)
    assert result4.m == -1  # нулевой полином

test_for_ADD_PP_P()
test_for_SUB_PP_P()
test_for_MUL_PQ_P()
