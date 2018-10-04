class planet:
    def __init__(self,name,age,game,system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system

    def orbit(self):
        return f'{self.name} is {self.system}'

lohit=planet('lohit',23,'counter strike','windows')

print(f'name is : {lohit.name}')
print(f'age is : {lohit.age}')
print(f'game is : {lohit.game}')
print(lohit.orbit())

naboo=planet('ggtgr',43,'cogfr','mac')

print(f'name is : {naboo.name}')
print(f'age is : {naboo.age}')
print(f'game is : {naboo.game}')
print(naboo.orbit())
