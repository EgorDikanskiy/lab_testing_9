class Calculator:
    """Простой калькулятор с бизнес-логикой, которую покрываем модульными тестами."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def is_prime_number(self, number):
        # простое число — целое, больше 1, делится только на 1 и на себя
        if not isinstance(number, int) or number < 2:
            return False
        divider = 2
        # достаточно проверить делители до корня из числа
        while divider * divider <= number:
            if number % divider == 0:
                return False
            divider += 1
        return True
