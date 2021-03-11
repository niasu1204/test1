import os,re, usecsv

apt = usecsv.switch(usecsv.opencsv('apt_202102.csv'))

#print(apt[:2])
#print(len(apt))

price =[]
newlist= []
for i in apt:
    try:
        #if i[5] > 120 and i[-5] >= 30000 and re.match('강원', i[0]):
        #if i[5]> 100 and i [-4] > 10 and i [-4] < 15 and i[-5] > 50000:
        #if i[5] > 130 and i[-5] <= 40000:
        #if re.search(r'아이파크',i[4]):
        if i[-5] > 300000:
            newlist.append([i[0], i[4],i[-4], i[-5]])       
            price.append(i[-5])
    except:
        pass    

usecsv.writecsv('apt_over30억.csv', newlist)

import numpy as np 
price2 = np.array([price])
print(price2.min(), price2.max())
