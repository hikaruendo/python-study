def area(radius):
    return 3.142*radius*radius

def volume(area,length):
    print(area*length)

radius=int(input('enter the value for the rad'))
length=int(input('enter the len'))

volume(area(radius),length)