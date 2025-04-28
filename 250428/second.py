# 입력 구현
# a = input("아무거나 입력해주세요.")

"""
입력을 몇가지 변수에 담아서
f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요.
"""

## 형변환
# print(type(a))
# b = int(a) # 문자를 숫자로로
# print(type(b))

# a = 1

# print(type(str(a)))

# 문자열 고유 기능
s = 'weniv CEO licat'
print(s.lower())

print(s.upper())

s = 'weniv CEO licat'

print(s.find("good"))
# print(s.index("good")) #ValueError: substring not found

print(s.find("weniv"))
print(s.find("licat"))

print(s.index("weniv"))
print(s.index("licat"))

print(s.count("i"))

s2 = s.replace("CEO","CTO")

print(s2)

s3 = "weniv-corp"

s4,s5 = s3.split("-")

print(s4,s5)
'''
입력이 들어온다. 키 몸무게 성별 나이 이름
예시 180 60 남 25 김아무개
이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
이름을 f-string통해 세번 반복해서 출력한다.
'''
# s10 = input()

# a,b,c,d,e = s10.split()
# print(a,b,c,d,e)
# print(f"{e*3}")

s20 = ["modu","labs","good"]

print("".join(s20))

name = 'licat'
age = 29


print('제 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))
print(f'제 이름은 {name}이고, 나이는 {age}살입니다.')


print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
print("Backslash: \\") # 백슬래시를 출력합니다.


# bool 타입
a = 10 > 3
b = True
c = False
print(type(a))
print(a)
## 형변환
a = 1
b = 0
c = -1
d = "okay"
f = ""

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))

print(a==b)

x = None