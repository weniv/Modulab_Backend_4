
# 정수
a = 10
b = 20
c = 0
d = -40
print(type(a),type(b),type(c),type(d))
print(int(9.33333))
# 실수
number1 = 3.12
number2 = -0.12
print(type(number1),type(number2))
print(float(3))
## 무한대
x = float("inf")
y = float("-inf")

# 문자열
str1 = "adcd"
str2 = 'adcd'

str3 = '''
오늘은 4월 28일입니다.

5월이 멀지 않았네요.

'''
str4 = '오늘은 4월 28일입니다.\n\n5월이 멀지 않았네요.'
print(type(str3))
print(str3)
print(str4)

# 문자열 이어붙이기

str6 = "modu"
str7 = "labs"

print(str6+str7)
str8 = str7+str6

print(str8)

# 개인정보 출력해보기
## 1. 성, 이름 변수를 따로 만들어서 + 로 합친 후 출력
## 2. 주민등록번호도 1번과 같이
## 3. 이메일 {아이디} {@} {네이버, 구글}

# 문자열 반복하기

str10 = str1 * 10

test2 = "30"

print(str10)

# print(str1 * test2) (x)
print(str10+"입니다"+"어쩌고 쩌고")
# 오늘은 4월 28일입니다.
a = "4"
b = "28"
# 기본방식
print("오늘은 "+a+"월 "+b+"일입니다.")
# f-string
# f""
print(f"오늘은 {a}월 {b*10}일입니다.")

# 문자열 인덱싱

s = "life is good"
print(s[0])
print(s[3])

# print(s[300]) #IndexError: string index out of range
## 주민등록번호가 13자리
## print(s[13])

# 문자열 슬라이싱 #  [start:stop:step]

print(s[0:3]) # s[0:3:1]
print(s[0:4:2]) # s[0:3:1]

# 다양한 슬라이싱 방법

s = 'weniv CEO licat'
print(1, s[0:5]) # 출력 : weniv
print(2, s[6:]) 
print(3, s[:]) 
print(4, s[::-1]) 
print(5, s[::2]) 

# 테스트
## ip address = 172.100.200.100

s = "ip address = 172.100.200.100"
'''
1. ip address문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다.
3. f-string을 사용해서 172100200100 문자 나오게 하기
'''
address = s[0:11]
print(address)
a,b,c,d = s[13:16],s[17:20],s[21:24],s[25:28]
print(a,b,c,d)

print(f"{a}{b}{c}{d}")
max