a = [1, 2, 3, 1, 1, 2, 3, 4, 5, "good"]

a[0] = 3

print(a)

a[3] = "aaaa"

print(a)

# a[3][1] = "g" # agaa 문자열의 특정 문자는 바꿀 수 없다.

li = []
# 데이터 추가
li.append(1)
li.append(2)
li.append([1, 2, 3])
print(li)
# [1, 2, [1, 2, 3]]
li[2].append("good")
print(li)

# 데이터 삭제 (리스트 안에 있는 데이터만 삭제한다.)
li.clear()
print(li)

b = [1, 2, 3]
c = b

# c.append(123)/

print(b)

c = b.copy()

c.append(2)
print(b)
print(c)

"""
1. 빈리스트를 만든다.
2. append를 사용하여 이중 리스트를 만든다.
3. 출력한다.
4. 리스트의 데이터를 다 지운다.
5. 출력한다.
6. copy를 활용한다.
7. 카피를 활용한 리스트에 append를 사용하여 출력한다.
"""
a = []

a.append([1, 2, 3])
print(a)
a.clear()
print(a)
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(b)

# count
a = [1, 2, 3, "okay", 1, 1, 1]

print(a.count(1))  # 4

b = [1, 2, 3, [1, 2, 3, 1]]
print(b.count(1)) # 1
# 3이 나오게 하려면?
print(b.count(1) + b[3].count(1))

# extend
a = [1,2,3,4]
b = [5,6,7,8]
# [1,2,3,4,5,6,7,8]