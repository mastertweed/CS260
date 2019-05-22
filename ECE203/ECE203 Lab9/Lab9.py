class SodaCan:

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def get_surface_area(self):
        area = 2 * 3.1415 * self.radius * self.height
        return area

    def get_volume(self):
        volume = 3.1415 * self.radius**2
        return volume


can1 = SodaCan(4, 0.5)
print(can1.get_volume())
print(can1.get_surface_area())
print('\n')

# --------------------


class Car:

    gas = 0

    def __init__(self, efficiency):
        self.efficiency = efficiency

    def add_gas(self, amount):
        self.gas = self.gas + amount

    def get_gas_level(self):
        print('There are %d Gallons in fuel tank' % (self.gas))

    def drive(self, miles):
        if miles < (self.efficiency * self.gas):
            self.gas = self.gas - (miles / self.efficiency)
            print('There are %d Gallons in fuel tank' % (self.gas))
        else:
            print('Not enough fuel in the tank!')


car1 = Car(20)
car1.get_gas_level()
car1.drive(10)
car1.add_gas(10)
car1.drive(20)
print('\n')

# --------------------

class Bug:

    facing = 'right'

    def __init__(self, inital_position):
        self.initial_position = inital_position

    def turn(self):
        if self.facing == 'right':
            self.facing = 'left'
        else:
            self.facing = 'right'

    def move(self):
        if self.facing == 'right':
            self.initial_position += 1
        else:
            self.initial_position -= 1

    def position(self):
        print(self.initial_position)

    def direction(self):
        print(self.facing)

ant = Bug(10)
ant.move()
ant.turn()
ant.move()
ant.move()
ant.position()
ant.direction()

# --------------------