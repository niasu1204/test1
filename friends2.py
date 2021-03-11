import os,re

os.chdir(r'C:\su\python\test')
f = open('friends101.txt', 'r', encoding = 'utf-8')

sentences = f.readlines()
print(len(sentences))

# for i in sentences[:1000]:
#     if re.match(r'[A-Z][a-z]+:', i) and re.search('would',i):
#         print(i)

f.close()

take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take',i)]

f = open('take.txt', 'w', encoding = 'utf-8')
f.writelines(take)
f.close
