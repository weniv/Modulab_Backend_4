# insert
a = [1, 2, 3, 4, 5]

# insert(인덱스, 값)
a.insert(0, 0)
print(a)
# pop() 제일 끝에 있는 값 추출
# pop(4) 4번째 인덱스에 있는 값을 추출
# 리스트값이 비어있으면 IndexError: pop from empty list
b = a.pop()
print(a)
# 미연에 방지하려면?
if len(a) >= 1:  # 리스트 내부의 데이터 갯수가 1개 이상이라면?
    a.pop()  # 추출
else:
    print("리스트가 비어있습니다.")

# remove(값)
c = [1, 2, 3, 1, 1]
c.remove(1)
print(c)  # [2, 3, 1, 1]
c.remove(1)
print(c)  # [2, 3, 1]
# c.remove(50) # ValueError: list.remove(x): x not in list
# reverse vs reversed
a = [1, 2, 3, 4, 5]
b = a.reverse()  # [5,4,3,2,1]
print(b)  # None;'


a = [1, 2, 3, 4, 5]
b = list(reversed(a))
print(a)
print(b)
c = a[::-1]
print("============================")
# sort sorted

a = [5, 4, 3, 2, 1]

# a.sort() 원본데이터 자체를 변경
b = list(sorted(a))  # 원본데이터 복사후 정렬 -> 리스트 타입으로 변경
print(a)
print(b)
c = [1, 2, 3, 4, 5]
# sorted(리스트,reverse=bool)
d = sorted(c, reverse=False)  # sorted(a)
# d = list(sorted(c, reverse=True))  # 내림차순 정렬
print(d)