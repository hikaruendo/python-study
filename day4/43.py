from random import shuffle
def jumble(word):
    aaa=list(word)
    shuffle(aaa)
    return '-'.join(aaa)

words=['lohit','Takuma','endo']
changer=[]

for word in words:
    changer.append(jumble(word))

print(changer)

changer=[jumble(word) for word in words]
print(changer)