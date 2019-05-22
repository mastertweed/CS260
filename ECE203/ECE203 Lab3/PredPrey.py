A = float(input(('Rate at which prey birth exceeds natural death')))
B = float(input('Rate of predation\n'))
C = float(input('Rate at which predator deaths exceed birth without food\n'))
D = float(input('Predator increase in the presence of food\n'))
Prey_size = float(input('Prey population size\n'))
Predator_size = float(input('Predator population size\n'))
years = int(input('Number of years\n'))


for i in range(years):
    Prey_size = Prey_size*(1 + A - B * Predator_size)
    Predator_size = Predator_size*(1 - C + D * Prey_size)

print(Prey_size)
print(Predator_size)