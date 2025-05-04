class calculator_functions:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def mod(self):
        return self.a % self.b
    def pow(self):
        return self.a ** self.b
    def sqrta(self):
        return self.a ** 0.5
    def sqrtb(self):
        return self.b ** 0.5


class numbers(calculator_functions):
    pass