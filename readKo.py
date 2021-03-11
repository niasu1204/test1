import codecs

f = codecs.open('a.txt', 'r', 'utf-8')
print(f.read())
f.close()

