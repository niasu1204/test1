import re

# print(re.match(r'is', 'Life  is cool').group())

def refinder(pattern, script):
    if re.match(pattern,script):
        print("MATCH!!")
        print(re.match(pattern,script).group())
    else:
        print("NOT MATCH!!")    
'''
refinder(r'is', 'Life is cool')

script = "Life is cool"

print(re.search(r'Life', script).group())
print(re.search(r'cool', script).group())
'''
'''
number ='My number is 210304-3****** and yous is 210303-4******'

result = re.findall('\d{6}',number)
print(result)
'''
example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2021년입니다.'

result = re.findall(r'\d.+년', example1)
#숫자(\d)로 시작하고 어떤 문자든(.) 반복(+)되며, '년'으로 끝나는 문자열을 반환
#:문장 맨 앞의 숫자부터 맨 뒤의 '년'사이의 모든 문자 반환
result = re.findall(r'\d+.년', example1)
result = re.findall(r'\d.+?년', example1) # ?: 0~1회  +: 1회 이상
print(result)


example= '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영 2019). 또 다른 견해도 있었습니다(Lion, 2018).'

result = re.findall(r'\(.+?\)', example)
print(result)

sentence = 'I love a lovely dog, really. I am not telling a lie. what a pretty dog! I love this dog.'
result = re.split(r'[.!?]',sentence)
print(result)

result = re.sub(r'dog','cat', sentence)
print('dog ->cat : ',result)
'''
data = 'a:3;b:4;c:5'

for i in re.split(r';', data):
    print(re.split(r':', i))

#['a', '3']
#['b', '4']
#['c', '5']
'''
words = 'I am nome now. \n\n\nI am with my cat. \n\n'
print(words)
result = re.sub(r'\n','', words)
print(result)

sentence2 = 'I love a lovely dog, really. I am not telling a lie.'
# ~ly로 끝나는 단어들을 추출하세요
print(re.findall(r'\w+ly',sentence2))