def lohit(dictionary):
    for key, val in dictionary.items():
        print('Iknow this a {} programing and \
this is {}, a framework of {}'.format(key,val,key))

lohit_items={}

while True:
    lohit_program=input('enter name of prog')
    lohit_frame=input('enter yhe name of frame')
    lohit_items[lohit_program]=[lohit_frame]

    another=input('add another prog? y/n')
    if another=='y':
        continue
    else:
        break

lohit(lohit_items)