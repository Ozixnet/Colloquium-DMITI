from modules.С.C_NUM import Permutation
from modules.С.APPLY_P_I_I import APPLY_P_I_I_f
from modules.С.COMPOSE_PP_P import COMPOSE_PP_P_f
from modules.С.INVERSE_P_P import INVERSE_P_P_f
from modules.С.TO_CYCLES_P_L import TO_CYCLES_P_L_f
from modules.С.SIGN_P_I import SIGN_P_I_f
from modules.С.ORDER_P_N import ORDER_P_N_f
from modules.С.IDENTITY_P_P import IDENTITY_P_P_f


# ============================================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================================

class TestStats:
    """Класс для отслеживания статистики тестов"""
    def __init__(self):
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.categories = {}
    
    def add_result(self, category, passed):
        self.total += 1
        if passed:
            self.passed += 1
        else:
            self.failed += 1
        
        if category not in self.categories:
            self.categories[category] = {"passed": 0, "failed": 0}
        
        if passed:
            self.categories[category]["passed"] += 1
        else:
            self.categories[category]["failed"] += 1


stats = TestStats()


def print_header(text, char="="):
    """Красивый заголовок для раздела"""
    width = 80
    print(f"\n{char * width}")
    print(f"{text:^{width}}")
    print(f"{char * width}")


def print_subheader(text):
    """Подзаголовок для группы тестов"""
    print(f"\n{'-' * 80}")
    print(f"> {text}")
    print(f"{'-' * 80}")


def debug_assert_eq(test_name: str, expected, actual, category="General"):
    """Проверка с красивым выводом"""
    print(f"\n[TEST] {test_name}")
    print(f"  Expected: {expected}")
    print(f"  Actual  : {actual}")
    
    if expected != actual:
        print(f"  Result: [X] FAILED")
        stats.add_result(category, False)
        raise AssertionError(f"{test_name} FAILED: expected {expected}, got {actual}")
    else:
        print(f"  Result: [OK] PASSED")
        stats.add_result(category, True)


def perm_to_str(p):
    """Преобразует перестановку в строку для вывода"""
    return f"[{', '.join(map(str, p.as_list()))}]"


def cycles_to_str(cycles):
    """Преобразует циклы в читаемую строку"""
    if not cycles:
        return "id"
    return ''.join(f"({' '.join(map(str, c))})" for c in cycles)


# ============================================================================
# БАЗОВЫЕ ТЕСТЫ
# ============================================================================

def test_basic_application():
    """Тестирование базового применения перестановки"""
    print_subheader("Базовое применение перестановки")
    
    p = Permutation([2, 3, 1])  # (1→2, 2→3, 3→1)
    debug_assert_eq("Размер перестановки", 3, p.n, "Basic")
    debug_assert_eq("Применение p(1)", 2, APPLY_P_I_I_f(p, 1), "Basic")
    debug_assert_eq("Применение p(2)", 3, APPLY_P_I_I_f(p, 2), "Basic")
    debug_assert_eq("Применение p(3)", 1, APPLY_P_I_I_f(p, 3), "Basic")
    
    # Проверка больших перестановок
    p_large = Permutation([5, 1, 3, 2, 4])
    debug_assert_eq("Большая перестановка p(1)", 5, APPLY_P_I_I_f(p_large, 1), "Basic")
    debug_assert_eq("Большая перестановка p(5)", 4, APPLY_P_I_I_f(p_large, 5), "Basic")


def test_identity():
    """Тестирование тождественной перестановки"""
    print_subheader("Тождественная перестановка")
    
    for n in [1, 3, 5, 10]:
        e = IDENTITY_P_P_f(n)
        expected = list(range(1, n + 1))
        debug_assert_eq(f"Identity S{n}", expected, e.as_list(), "Identity")
        debug_assert_eq(f"Знак id S{n}", 1, SIGN_P_I_f(e), "Identity")
        debug_assert_eq(f"Порядок id S{n}", 1, ORDER_P_N_f(e), "Identity")


# ============================================================================
# ТЕСТЫ НА КОМПОЗИЦИЮ
# ============================================================================

def test_composition_basic():
    """Базовые тесты на композицию"""
    print_subheader("Композиция перестановок - базовые случаи")
    
    p = Permutation([2, 3, 1])
    e = IDENTITY_P_P_f(3)
    
    # Композиция с тождественной
    comp1 = COMPOSE_PP_P_f(e, p).as_list()
    comp2 = COMPOSE_PP_P_f(p, e).as_list()
    debug_assert_eq("e ∘ p = p", p.as_list(), comp1, "Composition")
    debug_assert_eq("p ∘ e = p", p.as_list(), comp2, "Composition")


def test_composition_advanced():
    """Продвинутые тесты на композицию"""
    print_subheader("Композиция перестановок - сложные случаи")
    
    # Тест 1: Композиция транспозиций
    t1 = Permutation([2, 1, 3, 4])  # (1 2)
    t2 = Permutation([1, 3, 2, 4])  # (2 3)
    result = COMPOSE_PP_P_f(t1, t2)
    # (1 2) ∘ (2 3) = (1 2 3)
    expected = [2, 3, 1, 4]
    debug_assert_eq("(1 2) ∘ (2 3)", expected, result.as_list(), "Composition")
    
    # Тест 2: Некоммутативность
    result_rev = COMPOSE_PP_P_f(t2, t1)
    # (2 3) ∘ (1 2) = (1 3 2)
    expected_rev = [3, 1, 2, 4]
    debug_assert_eq("(2 3) ∘ (1 2)", expected_rev, result_rev.as_list(), "Composition")
    
    # Тест 3: Ассоциативность (p ∘ q) ∘ r = p ∘ (q ∘ r)
    p = Permutation([3, 1, 2, 4])
    q = Permutation([2, 3, 1, 4])
    r = Permutation([1, 3, 4, 2])
    
    left = COMPOSE_PP_P_f(COMPOSE_PP_P_f(p, q), r)
    right = COMPOSE_PP_P_f(p, COMPOSE_PP_P_f(q, r))
    debug_assert_eq("Ассоциативность (p∘q)∘r = p∘(q∘r)", 
                    left.as_list(), right.as_list(), "Composition")
    
    # Тест 4: Большие перестановки
    p1 = Permutation([3, 1, 5, 2, 4, 7, 6, 8])
    p2 = Permutation([2, 4, 1, 3, 6, 5, 8, 7])
    result = COMPOSE_PP_P_f(p1, p2)
    # Проверяем, что результат валидный
    debug_assert_eq("Размер композиции больших перестановок", 8, result.n, "Composition")


# ============================================================================
# ТЕСТЫ НА ОБРАТНУЮ ПЕРЕСТАНОВКУ
# ============================================================================

def test_inverse_basic():
    """Базовые тесты на обратную перестановку"""
    print_subheader("Обратная перестановка - базовые случаи")
    
    p = Permutation([3, 2, 1])
    inv = INVERSE_P_P_f(p)
    e = IDENTITY_P_P_f(3)
    
    comp_pi_inv = COMPOSE_PP_P_f(p, inv).as_list()
    comp_inv_pi = COMPOSE_PP_P_f(inv, p).as_list()
    
    debug_assert_eq("p ∘ p⁻¹ = e", e.as_list(), comp_pi_inv, "Inverse")
    debug_assert_eq("p⁻¹ ∘ p = e", e.as_list(), comp_inv_pi, "Inverse")


def test_inverse_advanced():
    """Продвинутые тесты на обратную перестановку"""
    print_subheader("Обратная перестановка - сложные случаи")
    
    # Тест 1: (p⁻¹)⁻¹ = p
    p = Permutation([4, 1, 5, 2, 3])
    inv_inv = INVERSE_P_P_f(INVERSE_P_P_f(p))
    debug_assert_eq("(p⁻¹)⁻¹ = p", p.as_list(), inv_inv.as_list(), "Inverse")
    
    # Тест 2: (p ∘ q)⁻¹ = q⁻¹ ∘ p⁻¹
    p = Permutation([3, 1, 2, 4, 5])
    q = Permutation([2, 3, 4, 5, 1])
    
    pq = COMPOSE_PP_P_f(p, q)
    inv_pq = INVERSE_P_P_f(pq)
    
    inv_p = INVERSE_P_P_f(p)
    inv_q = INVERSE_P_P_f(q)
    inv_q_inv_p = COMPOSE_PP_P_f(inv_q, inv_p)
    
    debug_assert_eq("(p∘q)⁻¹ = q⁻¹∘p⁻¹", 
                    inv_pq.as_list(), inv_q_inv_p.as_list(), "Inverse")
    
    # Тест 3: Инволюция (p = p⁻¹)
    involution = Permutation([2, 1, 4, 3, 5])
    inv = INVERSE_P_P_f(involution)
    debug_assert_eq("Инволюция p = p⁻¹", involution.as_list(), inv.as_list(), "Inverse")
    
    # Тест 4: Большая перестановка
    p_large = Permutation([7, 3, 9, 1, 5, 2, 8, 4, 6, 10])
    inv_large = INVERSE_P_P_f(p_large)
    e_large = IDENTITY_P_P_f(10)
    result = COMPOSE_PP_P_f(p_large, inv_large)
    debug_assert_eq("Большая перестановка p ∘ p⁻¹ = e", 
                    e_large.as_list(), result.as_list(), "Inverse")


# ============================================================================
# ТЕСТЫ НА ЦИКЛЫ
# ============================================================================

def test_cycles_basic():
    """Базовые тесты на разложение на циклы"""
    print_subheader("Разложение на циклы - базовые случаи")
    
    # Тождественная перестановка
    e = IDENTITY_P_P_f(4)
    cycles_no_fp = TO_CYCLES_P_L_f(e, include_fixed_points=False)
    cycles_with_fp = TO_CYCLES_P_L_f(e, include_fixed_points=True)
    
    debug_assert_eq("id S4 без фикс. точек", [], cycles_no_fp, "Cycles")
    debug_assert_eq("id S4 с фикс. точками", [[1], [2], [3], [4]], cycles_with_fp, "Cycles")
    
    # Одиночный цикл
    p = Permutation([2, 3, 4, 1])
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    debug_assert_eq("(1 2 3 4)", [[1, 2, 3, 4]], cycles, "Cycles")


def test_cycles_advanced():
    """Продвинутые тесты на разложение на циклы"""
    print_subheader("Разложение на циклы - сложные случаи")
    
    # Тест 1: Несколько непересекающихся циклов
    q = Permutation([7, 5, 1, 4, 2, 3, 6])
    cycles_no_fp = TO_CYCLES_P_L_f(q, include_fixed_points=False)
    cycles_with_fp = TO_CYCLES_P_L_f(q, include_fixed_points=True)
    
    debug_assert_eq("(1 7 6 3)(2 5) без фикс.", 
                    [[1, 7, 6, 3], [2, 5]], cycles_no_fp, "Cycles")
    debug_assert_eq("(1 7 6 3)(2 5) с фикс.", 
                    [[1, 7, 6, 3], [2, 5], [4]], cycles_with_fp, "Cycles")
    
    # Тест 2: Все транспозиции
    p = Permutation([2, 1, 4, 3, 6, 5])
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    debug_assert_eq("(1 2)(3 4)(5 6)", [[1, 2], [3, 4], [5, 6]], cycles, "Cycles")
    
    # Тест 3: Смешанные длины циклов
    p = Permutation([2, 3, 1, 5, 4, 7, 8, 6])
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    debug_assert_eq("(1 2 3)(4 5)(6 7 8)", 
                    [[1, 2, 3], [4, 5], [6, 7, 8]], cycles, "Cycles")
    
    # Тест 4: Длинный цикл
    p = Permutation([2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    debug_assert_eq("Цикл длины 10", expected, cycles, "Cycles")


# ============================================================================
# ТЕСТЫ НА ЗНАК
# ============================================================================

def test_sign_basic():
    """Базовые тесты на знак перестановки"""
    print_subheader("Знак перестановки - базовые случаи")
    
    # Тождественная - четная
    e = IDENTITY_P_P_f(5)
    debug_assert_eq("sgn(id) = +1", 1, SIGN_P_I_f(e), "Sign")
    
    # Транспозиция - нечетная
    t = Permutation([2, 1, 3, 4])
    debug_assert_eq("sgn((1 2)) = -1", -1, SIGN_P_I_f(t), "Sign")
    
    # 3-цикл - четный
    c3 = Permutation([2, 3, 1])
    debug_assert_eq("sgn((1 2 3)) = +1", 1, SIGN_P_I_f(c3), "Sign")


def test_sign_advanced():
    """Продвинутые тесты на знак перестановки"""
    print_subheader("Знак перестановки - сложные случаи")
    
    # Тест 1: sgn(p ∘ q) = sgn(p) × sgn(q)
    p = Permutation([2, 1, 3, 4])  # транспозиция, sgn = -1
    q = Permutation([1, 3, 2, 4])  # транспозиция, sgn = -1
    pq = COMPOSE_PP_P_f(p, q)
    
    sgn_p = SIGN_P_I_f(p)
    sgn_q = SIGN_P_I_f(q)
    sgn_pq = SIGN_P_I_f(pq)
    
    debug_assert_eq("sgn(p∘q) = sgn(p)×sgn(q)", sgn_p * sgn_q, sgn_pq, "Sign")
    
    # Тест 2: sgn(p⁻¹) = sgn(p)
    p = Permutation([3, 1, 4, 2, 5])
    inv_p = INVERSE_P_P_f(p)
    debug_assert_eq("sgn(p⁻¹) = sgn(p)", SIGN_P_I_f(p), SIGN_P_I_f(inv_p), "Sign")
    
    # Тест 3: Сложная перестановка
    q = Permutation([7, 5, 1, 4, 2, 3, 6])
    debug_assert_eq("sgn((1 7 6 3)(2 5))", 1, SIGN_P_I_f(q), "Sign")
    
    # Тест 4: Четная перестановка - композиция двух транспозиций
    t1 = Permutation([2, 1, 3, 4, 5])
    t2 = Permutation([1, 3, 2, 4, 5])
    result = COMPOSE_PP_P_f(t1, t2)
    debug_assert_eq("sgn(транспозиция ∘ транспозиция) = +1", 
                    1, SIGN_P_I_f(result), "Sign")
    
    # Тест 5: Произведение трех транспозиций
    t1 = Permutation([2, 1, 3, 4, 5, 6])
    t2 = Permutation([1, 3, 2, 4, 5, 6])
    t3 = Permutation([1, 2, 4, 3, 5, 6])
    result = COMPOSE_PP_P_f(COMPOSE_PP_P_f(t1, t2), t3)
    debug_assert_eq("sgn(3 транспозиции) = -1", -1, SIGN_P_I_f(result), "Sign")


# ============================================================================
# ТЕСТЫ НА ПОРЯДОК
# ============================================================================

def test_order_basic():
    """Базовые тесты на порядок перестановки"""
    print_subheader("Порядок перестановки - базовые случаи")
    
    # Тождественная
    e = IDENTITY_P_P_f(4)
    debug_assert_eq("ord(id) = 1", 1, ORDER_P_N_f(e), "Order")
    
    # Транспозиция
    t = Permutation([2, 1, 3, 4])
    debug_assert_eq("ord((1 2)) = 2", 2, ORDER_P_N_f(t), "Order")
    
    # 3-цикл
    c3 = Permutation([2, 3, 1])
    debug_assert_eq("ord((1 2 3)) = 3", 3, ORDER_P_N_f(c3), "Order")


def test_order_advanced():
    """Продвинутые тесты на порядок перестановки"""
    print_subheader("Порядок перестановки - сложные случаи")
    
    # Тест 1: lcm(4, 2) = 4
    q = Permutation([7, 5, 1, 4, 2, 3, 6])
    debug_assert_eq("ord((1 7 6 3)(2 5)) = lcm(4,2) = 4", 4, ORDER_P_N_f(q), "Order")
    
    # Тест 2: ord(p^k) делит ord(p)
    p = Permutation([2, 3, 1, 4])  # ord = 3
    p2 = COMPOSE_PP_P_f(p, p)  # p^2
    order_p = ORDER_P_N_f(p)
    order_p2 = ORDER_P_N_f(p2)
    # ord(p^2) должен делить ord(p)
    debug_assert_eq("ord(p²) делит ord(p)", 0, order_p % order_p2, "Order")
    
    # Тест 3: Три непересекающихся цикла - lcm(2,3,5) = 30
    p = Permutation([2, 1, 4, 5, 3, 7, 8, 9, 10, 6])  # (1 2)(3 4 5)(6 7 8 9 10)
    debug_assert_eq("ord((1 2)(3 4 5)(6 7 8 9 10)) = lcm(2,3,5) = 30", 
                    30, ORDER_P_N_f(p), "Order")
    
    # Тест 4: Большой цикл
    p = Permutation([2, 3, 4, 5, 6, 7, 8, 1])  # 8-цикл
    debug_assert_eq("ord(8-цикл) = 8", 8, ORDER_P_N_f(p), "Order")
    
    # Тест 5: lcm(3, 4) = 12
    p = Permutation([2, 3, 1, 5, 6, 7, 4])  # (1 2 3)(4 5 6 7)
    debug_assert_eq("ord((1 2 3)(4 5 6 7)) = lcm(3,4) = 12", 
                    12, ORDER_P_N_f(p), "Order")
    
    # Тест 6: Проверка p^ord(p) = id
    p = Permutation([3, 1, 5, 2, 4])
    order = ORDER_P_N_f(p)
    result = p
    for _ in range(order - 1):
        result = COMPOSE_PP_P_f(result, p)
    
    e = IDENTITY_P_P_f(5)
    debug_assert_eq(f"p^ord(p) = id (ord={order})", 
                    e.as_list(), result.as_list(), "Order")


# ============================================================================
# СТРЕСС-ТЕСТЫ
# ============================================================================

def test_stress():
    """Стресс-тесты на больших перестановках"""
    print_subheader("Стресс-тесты")
    
    # Тест 1: Большая перестановка (15 элементов)
    p = Permutation([5, 3, 7, 1, 9, 11, 2, 13, 4, 15, 6, 14, 8, 12, 10])
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    sign = SIGN_P_I_f(p)
    order = ORDER_P_N_f(p)
    inv = INVERSE_P_P_f(p)
    
    # Проверяем, что все работает
    debug_assert_eq("Большая перестановка - размер", 15, p.n, "Stress")
    debug_assert_eq("Большая перестановка - циклов > 0", True, len(cycles) > 0, "Stress")
    
    # Тест 2: Композиция больших перестановок
    p1 = Permutation([3, 1, 5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 15, 12, 14])
    p2 = Permutation([2, 4, 1, 6, 3, 8, 5, 10, 7, 12, 9, 14, 11, 15, 13])
    result = COMPOSE_PP_P_f(p1, p2)
    debug_assert_eq("Композиция больших перестановок", 15, result.n, "Stress")
    
    # Тест 3: Многократная композиция
    p = Permutation([2, 3, 4, 5, 1])
    result = p
    for i in range(4):  # p^5 = id для 5-цикла
        result = COMPOSE_PP_P_f(result, p)
    
    e = IDENTITY_P_P_f(5)
    debug_assert_eq("p^5 = id для 5-цикла", e.as_list(), result.as_list(), "Stress")


# ============================================================================
# ГРАНИЧНЫЕ СЛУЧАИ
# ============================================================================

def test_edge_cases():
    """Тесты граничных случаев"""
    print_subheader("Граничные случаи")
    
    # Тест 1: Минимальная нетривиальная перестановка
    p = Permutation([2, 1])
    debug_assert_eq("S2: размер", 2, p.n, "Edge")
    debug_assert_eq("S2: знак", -1, SIGN_P_I_f(p), "Edge")
    debug_assert_eq("S2: порядок", 2, ORDER_P_N_f(p), "Edge")
    
    # Тест 2: Одноэлементная перестановка
    p = Permutation([1])
    debug_assert_eq("S1: размер", 1, p.n, "Edge")
    debug_assert_eq("S1: знак", 1, SIGN_P_I_f(p), "Edge")
    debug_assert_eq("S1: порядок", 1, ORDER_P_N_f(p), "Edge")
    
    # Тест 3: Все элементы на своих местах кроме двух последних
    p = Permutation([1, 2, 3, 4, 6, 5])
    cycles = TO_CYCLES_P_L_f(p, include_fixed_points=False)
    debug_assert_eq("Только последняя транспозиция", [[5, 6]], cycles, "Edge")


# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ ЗАПУСКА
# ============================================================================

def print_statistics():
    """Выводит финальную статистику"""
    print_header("STATISTIKA TESTIROVANIYA", "=")
    
    print(f"\n{'Kategoriya':<20} {'Projdeno':<12} {'Provaleno':<12} {'Vsego':<12}")
    print("-" * 60)
    
    for category, results in sorted(stats.categories.items()):
        total = results["passed"] + results["failed"]
        print(f"{category:<20} {results['passed']:<12} {results['failed']:<12} {total:<12}")
    
    print("-" * 60)
    print(f"{'ITOGO':<20} {stats.passed:<12} {stats.failed:<12} {stats.total:<12}")
    print("=" * 60)
    
    success_rate = (stats.passed / stats.total * 100) if stats.total > 0 else 0
    print(f"\n[+] Uspeshnost': {success_rate:.1f}%")
    
    if stats.failed == 0:
        print("\n" + "=" * 60)
        print("VSE TESTY USPESHNO PROJDENY!")
        print("=" * 60)
    else:
        print(f"\n[!] Provaleno testov: {stats.failed}")


def run_all_tests():
    """Запускает все тесты"""
    print_header("TESTIROVANIE MODULYA KOMBINATORIKI", "=")
    print(f"{'Modul:':<15} modules.C")
    print(f"{'Avtor:':<15} Berdichevskij Maksim, gr. 4381")
    
    try:
        # Bazovye testy
        print_header("RAZDEL 1: BAZOVYE TESTY")
        test_basic_application()
        test_identity()
        
        # Kompoziciya
        print_header("RAZDEL 2: KOMPOZICIYA PERESTANOVOK")
        test_composition_basic()
        test_composition_advanced()
        
        # Obratnaya perestanovka
        print_header("RAZDEL 3: OBRATNAYA PERESTANOVKA")
        test_inverse_basic()
        test_inverse_advanced()
        
        # Cikly
        print_header("RAZDEL 4: RAZLOZHENIE NA CIKLY")
        test_cycles_basic()
        test_cycles_advanced()
        
        # Znak
        print_header("RAZDEL 5: ZNAK PERESTANOVKI")
        test_sign_basic()
        test_sign_advanced()
        
        # Poryadok
        print_header("RAZDEL 6: PORYADOK PERESTANOVKI")
        test_order_basic()
        test_order_advanced()
        
        # Stress-testy
        print_header("RAZDEL 7: STRESS-TESTY I GRANICHNYE SLUCHAI")
        test_stress()
        test_edge_cases()
        
    except AssertionError as e:
        print(f"\n\n[X] TEST PROVALEN: {e}")
        print_statistics()
        raise
    
    # Final'naya statistika
    print_statistics()


# ============================================================================
# ТОЧКА ВХОДА
# ============================================================================

if __name__ == "__main__":
    run_all_tests()
