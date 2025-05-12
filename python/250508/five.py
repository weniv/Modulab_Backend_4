# 튜플플
a = (1, 2, 3, "good")

print(type(a))  # <class 'tuple'>

print(a[3]) # 인덱싱 기능 사용 가능

b = a[0:2] # 슬라이스 기능 사용 가능
print(b)

# a[3] = "good" #TypeError: 'tuple' object does not support item assignment

numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

print(numbers.count(5)) # 2
print(numbers.index(5)) # 4 제일 처음에 있는 인덱스를 찾음.