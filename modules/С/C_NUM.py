class Permutation:
    """
    Структура хранения параметров для C-модулей (комбинаторика)
    
    _mapping — список длины n, содержащий перестановку чисел 1..n, без повторов.
    """
    def __init__(self, mapping):
        """
        mapping: список или кортеж длины n,
        содержащий перестановку чисел 1..n, без повторов.
        """
        self._mapping = list(mapping)
        n = len(self._mapping)
        if sorted(self._mapping) != list(range(1, n + 1)):  # TODO сделать свою сортировку
            raise ValueError(f"Некорректная перестановка: {self._mapping}")

    @property
    def n(self):
        """Размер n, то есть мы работаем в S_n."""
        return len(self._mapping)

    def as_list(self):
        """Удобный способ получить внутреннее представление."""
        return list(self._mapping)

    def __repr__(self):
        return f"Permutation({self._mapping})"
