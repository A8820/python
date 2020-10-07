
class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} started'

    def stop(self):
        return f'{self.name} stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allowed for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allowed for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


bmw = SportCar(180, 'Blue', 'BMW', False)
renault = TownCar(30, 'Black', 'Renault', False)
vw = WorkCar(70, 'Yellow', 'VolksWagen', False)
mercedes = PoliceCar(110, 'White',  'Ford', True)
print(renault.turn_left())
print(f'When {renault.turn_right()}, {bmw.stop()}')
print(f'{vw.name} is {vw.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {vw.name}  a police car? {vw.is_police}')
print(bmw.show_speed())
print(renault.show_speed())
print(mercedes.police())
print(mercedes.show_speed())