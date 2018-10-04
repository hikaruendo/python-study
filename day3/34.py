class planet:
    shape='round'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def orbit(self):
        return f'{self.name} age is {self.age}'

    @classmethod
    def commons(cls):
        return f'All the planets are {cls.shape}'

napoo=planet('napoo',400)
print(planet.shape)
print(planet.commons())
print(napoo.orbit())
print(napoo.commons())