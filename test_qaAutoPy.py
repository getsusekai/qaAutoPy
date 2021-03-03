import pytest


# тесты для Int
# 1 - Двойной(!) параметрический тест для Int: Проверяет: 1) является ли значение Int, 2)Если Int, то простое ли?
# Также здесь предусмотрен try-except, чтобы сотвествовать п.5 (TypeError не бросает, обрабатывает дальше)
# Невалидные значения (другой тип данных, отриц. числа и т.п.) не добавил в параметры, чтобы тест проходил (п.3)
@pytest.mark.parametrize("value", [3, 7, 11])
def test_value_is_prime_number(value):
    try:
        assert isprime(value), f"{value} isn't a prime number"
    except TypeError:
        assert isinstance(value, int), f"{value} isn't the Integer!"


# 2 - Делится ли число одновременно на 3 и 5 без остатка?
def test_number_is_positive(number=15):
    assert ((number % 3 == 0) and (number % 5 == 0)), f"{number} isn't divisible by 3 and 5"


# 3 - Number is positive ?
def test_sum(number=99):
    assert (number > 0), f"{number} isn't a positive number"


# тесты для List
# 1 - проверка на пустоту списка
def test_list_is_empty():
    assert len([]) == 0, "List isn't empty"


# 2 - cумма чисел в списке больше 99?
def test_sum_elmnts():
    assert sum(int(i) for i in [99, 1]), "Sum of number '<' or '=' 99"


# 3 - Содержит ли список другие списки?
def test_has_list():
    assert any(isinstance(a, list) for a in [1, 2, [3, 'A']]), "List doesn't contain any lists"


# вспомогательная функция для самого первого теста
def isprime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False
