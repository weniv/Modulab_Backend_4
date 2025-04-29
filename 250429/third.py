
# if 문
age = 10
height = 200
if age > 18 or height >=150:
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")
    print("성인입니다.")


print("안녕하세요.")

"""
if 입력한 비밀번호 != 입력한 비밀번호 확인:
    회원가입 거부

"""

# if ~ else 구문 if가 참이 아니면 else 구문을 실행

age = 20

if age >= 30:
    print("30대 이상입니다.")
else:
    print("30대가 아닙니다.")

# if ~ elif ~ else 구문

age = 20

if age <= 19:
    print("청소년입니다.")

elif age < 30:
    print("성인입니다.")

else:
    print("30대 이상입니다.")

'''
한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)
'''

yyyy,mm,dd = input().split()

yyyy,mm,dd = int(yyyy),int(mm),int(dd)

if yyyy % 2 == 0:
    print("짝수 년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")