
# and 연산

## 다른 언어에서는

# a && b
a = True
b = True

c = a and b

d = 10 > 5 and 10 < 5 # d = True and False
print(d)

f = 10 >= 10 or False # 앞에 이미 True 나왔기에 때문에 뒤에 값이 무엇이 오든 True가 성립된다.
print(f)

f = False and True and True # 0 1 1
print(f)

f2 = (False or True) and True
print(f2)

f3 = not ((False or True) and True)

print(f3)

a = 10
b = 20

c = a!=b # 다르니? 라고 물어보는것 # True
d = not a!=b # 다르니? 라고 물어보는것(반전) # False

##
# a = int(input())
# b = int(input())
# c = int(input()) 
###  항은 3개 이상 and , or는 마음대로 연결하여 결과 출력

a = 10

a = a + 10 # == a+= 10

# 멤버연산

st = "modulabs is good"

sta = "good" not in st # "good"이라는 문자가 st에 없니?
sta2 = "good" in st # "good"이라는 문자가 st에 있니?

# split 

a = "123456-1122335"

c,d = a.split()
print(c)