class employee:
    increase=2
    def __init__(self,pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

    def fullname(self):
        return '{} {}'.format(self.name,self.age)

    def salery_hike(self):
        self.pay=int(self.pay * employee.increase)

lohit=employee(2,'lohit',21)
rekha=employee(3,'rekha',23)

print(lohit.pay)
lohit.salery_hike()
print(lohit.pay)
print(lohit.__dict__)
print(lohit.increase)
lohit.increase=10

print(lohit.__dict__)
print(lohit.increase)
print(lohit.name)
print(lohit.pay)

