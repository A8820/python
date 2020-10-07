
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def road_square(self):
        s = self._length * self._width
        return s

class Mass(Road):
    def __init__(self, _length, _width, _mass_per_cm, _thickth):
        self._length = _length
        self._width = _width
        self._mass_per_cm = _mass_per_cm
        self._thickth = _thickth


    def mass_per_square(self):
        road_mass = self._length * self._width * self._mass_per_cm * self._thickth
        return road_mass

r = Mass(5000, 20, 25, 5)
print(r.mass_per_square())