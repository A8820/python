
class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_expenses_c(self):
        return self.width / 6.5 + 0.5

    def get_expenses_j(self):
        return self.height * 2 + 0.3

    @property
    def get_expenses_total(self):
        return str(f'Total textil expenses: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.expenses_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Total coat expenses: {self.expenses_c}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.expenses_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Total jacket expenses: {self.expenses_j}'

coat = Coat(3, 5)
jacket = Jacket(2, 3)
print(coat)
print(jacket)
print(coat.get_expenses_total)
print(jacket.get_expenses_total)
print(jacket.get_expenses_c())
print(jacket.get_expenses_j())