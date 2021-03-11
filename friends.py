import os, re, codecs

os.chdir(r'C:\su\python\test')

f = open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()
#print(script101[:100])
f.close()
Line = re.findall(r'Monica:.+', script101)
#print(Line[:3])
'''
for i in Line[:3]:
    print(i)
'''
'''
f = open('monica.txt','w',encoding='utf-8')
monica =''
for i in Line:
    monica += i +'\n'

f.write(monica)
f.close()
'''
# p = list(set(re.findall(r'[A-Z][a-z]+:', script101)))
# for x in p :
#     print(re.sub(':','',x))
#     print(x[:-1])

text = re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101) [:6]
print(text)

  












