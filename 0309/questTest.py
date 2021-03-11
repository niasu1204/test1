import usecsv
import numpy as np

quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
#print(quest)

#print(quest>5)
quest[quest>5] = 5
print(quest)

quest = quest.astype('int32')
usecsv.writecsv('resultcsv.csv', list(quest))