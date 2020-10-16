
class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Devision by null!")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(1, 0))
print(DivisionByNull.divide_by_null(15, 0.1))
print(div.divide_by_null(0, 0))