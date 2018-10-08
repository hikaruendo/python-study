def sequence_filter(line):
    return '>' not in line

with open ('text2.txt') as text:
    lines=text.readlines()
    print(list(filter(sequence_filter,lines)))
    