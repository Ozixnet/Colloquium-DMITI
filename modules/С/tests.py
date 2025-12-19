from modules.С.C_NUM import Permutation
from modules.С.APPLY_P_I_I import APPLY_P_I_I_f
from modules.С.COMPOSE_PP_P import COMPOSE_PP_P_f
from modules.С.INVERSE_P_P import INVERSE_P_P_f
from modules.С.TO_CYCLES_P_L import TO_CYCLES_P_L_f
from modules.С.SIGN_P_I import SIGN_P_I_f
from modules.С.ORDER_P_N import ORDER_P_N_f
from modules.С.IDENTITY_P_P import IDENTITY_P_P_f


def _test_basic_application():
    print("\n=== _test_basic_application ===")
    p = Permutation([2, 3, 1])  # (1→2, 2→3, 3→1)
    debug_assert_eq("size n", 3, p.n)

    debug_assert_eq("p(1)", 2, APPLY_P_I_I_f(p, 1))
    debug_assert_eq("p(2)", 3, APPLY_P_I_I_f(p, 2))
    debug_assert_eq("p(3)", 1, APPLY_P_I_I_f(p, 3))


def _test_identity_and_composition():
    print("\n=== _test_identity_and_composition ===")
    p = Permutation([2, 3, 1])
    e = IDENTITY_P_P_f(3)

    comp1 = COMPOSE_PP_P_f(e, p).as_list()
    comp2 = COMPOSE_PP_P_f(p, e).as_list()

    debug_assert_eq("e ∘ p", p.as_list(), comp1)
    debug_assert_eq("p ∘ e", p.as_list(), comp2)


def _test_inverse():
    print("\n=== _test_inverse ===")
    p = Permutation([3, 2, 1])
    inv = INVERSE_P_P_f(p)
    e = IDENTITY_P_P_f(3)

    comp_pi_inv = COMPOSE_PP_P_f(p, inv).as_list()
    comp_inv_pi = COMPOSE_PP_P_f(inv, p).as_list()

    debug_assert_eq("p ∘ p^{-1}", e.as_list(), comp_pi_inv)
    debug_assert_eq("p^{-1} ∘ p", e.as_list(), comp_inv_pi)


def _test_to_cycles():
    print("\n=== _test_to_cycles ===")

    # 1) Тождественная перестановка: без fixed_points циклов нет, с ними — n одноэлементных
    e = IDENTITY_P_P_f(4)
    debug_assert_eq(
        "id S4, no fixed points",
        [],
        TO_CYCLES_P_L_f(e, include_fixed_points=False),
    )
    debug_assert_eq(
        "id S4, with fixed points",
        [[1], [2], [3], [4]],
        TO_CYCLES_P_L_f(e, include_fixed_points=True),
    )

    # 2) Одна 4-цикл: (1 2 3 4)
    p = Permutation([2, 3, 4, 1])
    debug_assert_eq(
        "(1 2 3 4), no fp",
        [[1, 2, 3, 4]],
        TO_CYCLES_P_L_f(p, include_fixed_points=False),
    )

    # 3) Пример из наших обсуждений: [1,2,3,4,5,6,7] → [7,5,1,4,2,3,6]
    #    Это должно дать циклы (1 7 6 3) и (2 5), фиксированная точка 4.
    q = Permutation([7, 5, 1, 4, 2, 3, 6])
    cycles_no_fp = TO_CYCLES_P_L_f(q, include_fixed_points=False)
    cycles_with_fp = TO_CYCLES_P_L_f(q, include_fixed_points=True)

    debug_assert_eq(
        "q, no fixed points",
        [[1, 7, 6, 3], [2, 5]],
        cycles_no_fp,
    )
    debug_assert_eq(
        "q, with fixed points",
        [[1, 7, 6, 3], [2, 5], [4]],
        cycles_with_fp,
    )


def _test_sign_and_order():
    print("\n=== _test_sign_and_order ===")

    # 1) Тождественная перестановка: знак +1, порядок 1
    e = IDENTITY_P_P_f(4)
    debug_assert_eq("sgn(id S4)", 1, SIGN_P_I_f(e))
    debug_assert_eq("ord(id S4)", 1, ORDER_P_N_f(e))

    # 2) Транспозиция (1 2): одна инверсия → знак -1, порядок 2
    t = Permutation([2, 1, 3, 4])
    debug_assert_eq("sgn((1 2))", -1, SIGN_P_I_f(t))
    debug_assert_eq("ord((1 2))", 2, ORDER_P_N_f(t))

    # 3) Цикл (1 2 3): знак +1, порядок 3
    c3 = Permutation([2, 3, 1])
    debug_assert_eq("sgn((1 2 3))", 1, SIGN_P_I_f(c3))
    debug_assert_eq("ord((1 2 3))", 3, ORDER_P_N_f(c3))

    # 4) q = (1 7 6 3)(2 5): порядок lcm(4,2)=4, знак = (+1)
    q = Permutation([7, 5, 1, 4, 2, 3, 6])
    debug_assert_eq("ord(q)", 4, ORDER_P_N_f(q))
    debug_assert_eq("sgn(q)", 1, SIGN_P_I_f(q))  # <-- тут было -1, нужно 1


def _run_all_tests():
    _test_basic_application()
    _test_identity_and_composition()
    _test_inverse()
    _test_to_cycles()
    _test_sign_and_order()
    print("\nALL TESTS PASSED")


def debug_assert_eq(test_name: str, expected, actual):
    print(f"\n[Test] {test_name}")
    print(f"  EXPECTED: {expected}")
    print(f"  ACTUAL  : {actual}")
    if expected != actual:
        # Явный assert с сообщением — стандартный способ сделать вывод понятным.
        raise AssertionError(f"{test_name} FAILED: expected {expected}, got {actual}")
    else:
        print(f"  RESULT  : OK")


if __name__ == "__main__":
    # _run_all_tests()
    # Композиция
    g = Permutation([3, 1, 4, 2])  # нижняя строка g
    x = Permutation([1, 4, 2, 3])  # нижняя строка x

    res = COMPOSE_PP_P_f(g, x)  # g ∘ x
    print(res.as_list())  # => [3, 2, 1, 4]
