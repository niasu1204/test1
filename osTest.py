import os

#os.chdir(r'C:\su')   
#print(os.getcwd())
#print(os.listdir())


os.chdir(r'C:\su\python\test')

f = open('a.txt', 'w', encoding="utf-8")
text = 'abcde한글'
print(f.write(text))
f.close()

f = open('a.txt', 'r', encoding="utf-8")
print('첫번째 읽음 :',f.read())
f.close()

f = open('a.txt', 'a', encoding="utf-8")
print(f.write("\n추가 잘 되는지 확인하자"))
f.close()

f = open('a.txt', 'r', encoding="utf-8")
print('두번째 읽음',f.read())
f.close()

with open('test.txt','w') as f:
    f.write("I like python")