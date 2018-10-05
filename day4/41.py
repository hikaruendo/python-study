numbers=[1,2,3,4,5,6,7,8,9]
square=[]

for number in numbers:
    if (number**2)%2==0:
        square.append(number**2)

print(square)

square=[num**2 for num in numbers if (num**2)%2==0]
print('_',square)