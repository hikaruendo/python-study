class planet:
    def __init__(self):
        self.name='lohit'
        self.game='hdfu'
        self.number=498
        self.rate=5

    def orbit(self):
        return f'{self.name} is {self.number}'

lohit=planet()
print(f'name is : {lohit.name}')
print(f'game is : {lohit.game}')
print(f'num is : {lohit.number}')

print(lohit.orbit())
