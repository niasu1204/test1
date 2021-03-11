import usecsv, os, re

total = usecsv.opencsv('popSeoul.csv')	
newPop = usecsv.switch(total)

#print(newPop[:4])
new = [['구','한국인','외국인','외국인 비율(%)']]

for i in newPop:
    foreigner = 0
    try:
        foreigner = round(i[2]/(i[1]+i[2])*100,1)
        if foreigner > 3:
            new.append([i[0],i[1],i[2],foreigner])
        #print(i[0], foreigner)
    except:
        pass

usecsv.writecsv('newPop.csv', new)