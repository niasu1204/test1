import csv, os

# f = open('a.csv','r')

# new = csv.reader(f)
# print(new)

# a_list =[]

# for i in new:
#     print(i)
#     a_list.append(i)

# print('a_list : ',a_list)

#f.close()

def opencsv(filename):
    f=open(filename, 'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

print(opencsv('example2.csv'))
