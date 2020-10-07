
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start drawing {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Choosed {self.title}. Start drawing with pen.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Choosed {self.title}. Start drawing with pencil.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Choosed {self.title}. Start drawing with handle.'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())