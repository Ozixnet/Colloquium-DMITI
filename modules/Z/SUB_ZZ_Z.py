from modules.Z.Z_NUM import ZNum
from modules.N.N_NUM import NNum
from modules.Z.POZ_Z_D import POZ_Z_D_f
from modules.Z.ABS_Z_N import ABS_Z_N_f
from modules.N.ADD_NN_N import ADD_NN_N_f
from modules.N.SUB_NN_N import SUB_NN_N_f
from modules.N.COM_NN_D import COM_NN_D_f
from modules.Z.MUL_ZM_Z import MUL_ZM_Z_f
from modules.Z.ADD_ZZ_Z import ADD_ZZ_Z_f

def SUB_ZZ_Z_f(a: ZNum, b: ZNum) -> ZNum:
    """
    Вычитание целых чисел
    a - уменьшаемое (целое число)
    b - вычитаемое (целое число)
    Возврат - ZNum (разность a - b)
    """

    # Умножаем b на -1 и складываем с a
    neg_b = MUL_ZM_Z_f(b)
    return ADD_ZZ_Z_f(a, neg_b)