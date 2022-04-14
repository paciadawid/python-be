def calculate_fuel(mass: int) -> str | int:
    if type(mass) != int:
        return False

    fuel = mass // 3 - 2
    if mass <= 0:
        return 0
    elif mass > 0 and fuel <= 0:
        return 1
    return fuel


class Animal:

    def __init__(self, type):
        self.type = type

    def make_a_sound(self):
        if self.type == "cat":
            print("meow")
        elif self.type == "dog":
            print("bark")
        else:
            print("not known")


class Calculator:

    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    @staticmethod
    def add(a, b):
        try:
            return a + b
        except TypeError:
            return False

    def sub(self, a, b):
        try:
            return a - b
        except TypeError:
            return False

    def div(self, a, b):
        try:
            return a / b
        except (ZeroDivisionError, TypeError):
            return False

    def mul(self, a, b):
        try:
            return a * b
        except TypeError:
            return False


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.div(1, 0))

    Calculator.add(1, 2)
