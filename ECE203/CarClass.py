import random


class Car:

    kind = 'car'         # class variables shared by all instances
    manufacturer = ''
    type = ''
    model = ''
    year = ''
    color = ''
    miles = ''
    MSRP = ''
    value = ''

    def __init__(self, kind):
        self.kind = kind

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'black', 'white', 'grey']    #Car class colors
    car_types = ['truck', 'sedan', 'coupe', 'SUV', 'sports', 'super']

#

# Car type class within company class

    class Ford:

        name = 'Ford'

        class Truck:
            type = 'Truck'
            models = ['f150', 'f250', 'f350']
            price = ['35,000', '45,000', '55,000']

        class Sedan:
            type = 'Sedan'
            models = ['focus']
            price = ['28,000']

        class Coupe:
            type = 'Coupe'
            models = []
            price = []

        class SUV:
            type = 'SUV'
            models = ['explorer', 'expedition']
            price = ['38,500', '50,800']

        class Sports:
            type = 'Sports'
            models = []
            price = []

        class Super:
            type = 'Super'
            models = []
            price = []


# Car class without type

    class Honda:

        name = 'Honda'
        models = ['accord', 'civic', 'cr-v', 'fit', 'nsx', 'pilot', 'odyssey', 'ridgeline']
        price = ['30,000', '26,000', '35,000', '24,500', '120,000', '40,000', '45,000', '43,400']

    class GeneralMotors:

        name = 'General Motors'
        models = ['accord', 'civic', 'cr-v', 'fit', 'nsx', 'pilot', 'odyssey', 'ridgeline']
        price = ['30,000', '26,000', '35,000', '24,500', '120,000', '40,000', '45,000', '43,400']

    class Toyota:

        name = 'Toyota'
        models = ['accord', 'civic', 'cr-v', 'fit', 'nsx', 'pilot', 'odyssey', 'ridgeline']
        price = ['30,000', '26,000', '35,000', '24,500', '120,000', '40,000', '45,000', '43,400']

    class BMW:

        name = 'BMW'
        models = []
        price = []

    class VW:

        name = 'VW'
        models = []
        price = []

    class Audi:

        name = 'Audi'
        models = []
        price = []

    class Nissan:

        name = 'Nissan'
        models = []
        price = []

#

    brands = [Ford, Honda, GeneralMotors, Toyota, BMW, VW]

# Random mileage generator

def miles_selector():
    mile = random.randrange(100000)
    return mile

# Index of all possible cars

all_cars_index = ['Auto 1', 'Auto 2', 'Auto 3', 'Auto 4', 'Auto 5', 'Auto 6', 'Auto 7']
all_cars = []

# Generate Car class object for each all_cars_index

p = 0
for i in all_cars_index:
    a = 'a' + str(p)
    a = Car(i)
    p += 1
    all_cars.append(a)

# Define all Car class variables for each object

def car_chooser(car_num, brands_index, vehicle_type, model_in, mileage, col_index):

    company = Car.brands[brands_index]

    id = all_cars[car_num]
    id.manufacturer = company.name
    id.type = company.vehicle_type
    id.model = company.Truck.models[model_in]
    id.MSRP = company.Truck.price[company.Truck.models.index(id.model)]
    id.year = mileage
    id.color = Car.colors[col_index]
    id.miles = miles_selector()


car_chooser(0, 0, 0, 0, '2009', 5)
car_chooser(1, 0, 0, 1, '2004', 4)
car_chooser(2, 0, 0, 1, '1996', 0)
car_chooser(3, 0, 0, 2, '2015', 6)
car_chooser(4, 0, 0, 0, '2016', 2)

print('')
print(all_cars_index)

for i in all_cars:
    print(i.kind, '|', i.manufacturer, '|',  i.model, '|',  i.year, '|',  i.color, '|',  i.miles, '|',  '$' + i.MSRP)
