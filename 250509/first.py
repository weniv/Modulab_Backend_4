# 복습

a = (1, 10, 1, 2, 3)

# 슬라이싱
b = a[2:5]  # (1,2,3)
c = a[1]
# 기능
c = a.count(1)  # 2
d = a.index(1)  # 0

# set 자료구조

a = {1, 2, 3, 1}
print(a)  # {1,2,3}
print(len(a))  # 3

# 형변환 list -> set

a = [1, 1, 1, 2, 2, 3]
b = set(a)
print(b)
c = list(b)

a = {1, 2, 3}

# print(a[0])  #TypeError: 'set' object is not subscriptable

d = {"a", 1, 2, 3, 1, "a"}
print(d)

# e = list(d)
# print(e)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}")
print(f"차집합: {set2 - set1}")

# set 수정
fruits = {'apple','banana','cherry'}

fruits.add('orange')
print(fruits)

fruits.remove('apple')
print(fruits)
# fruits.remove('apple') # KeyError: 'apple'

print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")
