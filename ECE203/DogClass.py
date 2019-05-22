class Dog:

    kind = 'canine'         # class variable shared by all instances

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

a = Dog('dog_A')
b = Dog('dog_B')
c = Dog('dog_C')
d = Dog('dog_D')

a.add_trick('roll')
b.add_trick('hello')
c.add_trick('play')
d.add_trick('fetch')

print(a.name)