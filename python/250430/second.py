a = "good"

b = "a" in a

print(len(a))

# 리스트
li = [10, 20, 30, 40]
a = "a씨"
b = "b씨"

x = [1, 2, 3]
y = ["apple", "banana", "cherry", 1]
t = ["a", ["c", "d"], "c"]
z = [1, [2], 3] in [2]  # false
# [1, [2], 3] in [2,3,2132,13,[1,[2],3]]
print(z)
test = [1, 2, 3] in [1, 2, [1, 2, 3]]
print(test)
test2 = [1, 2, 3] in [[1, 2, 3]]
print(test2)
test3 = [1, [2, [3, [3, 4, [4, [1, []]]]]]]

print(len(test3))

t = [1, 2, 3, [4, 5, 6]]

a = t[3]

t2 = [1, 2, 3, [4, 5, [2, 31]], 1]

print(t2[3][2])

# print(t2[10000])

# 수정
t2[0] = 5

t3 = [5, 4, 3, [2, 1]]

t4 = []

t4.append(1)

print(t4)

t4.append(2)  # append는 리스트 뒤에 붙인다.

t4.clear()  # 리스트안 데이터 삭제

# t4.remove(3)  # 리스트 안에서 3이란 값을 찾아 지운다.

t4 = [5, 4, 3, 2, 1] # 오름차순 정렬
t4.sort()
print(t4)

# 리스트 만들 때 방법
a = []
b = list()

data = t4.pop() # 리스트의 맨 오른쪽에 있는 값을 추출후 변수에 저장
