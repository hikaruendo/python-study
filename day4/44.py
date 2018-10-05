grades=['A','B','A','C','F','C',"D"]

def remove_F(grade):
    return grade!='F'

print(list(filter(remove_F, grades)))

filtered_grade=[]
for grade in grades:
    if grade!='A':
        filtered_grade.append(grade)
print(filtered_grade)

filtered_grade=[grade for grade in grades if grade != 'B']
print(filtered_grade)