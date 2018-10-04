class planet:
    fun='happy'
    def __init__(self,name,age,game,system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system

    def orbit(self):
        return f'{self.name} is {self.system}'

lohit=planet('lohit','23','cousdn','windows')

print(f'name is : {lohit.name}')
print(f'age is : {lohit.age}')
print(f'game is : {lohit.game}')
print(lohit.orbit())
