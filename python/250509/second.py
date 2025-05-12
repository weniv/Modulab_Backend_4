# 딕셔너리 dict()

# key:value
my_dict = {"me": "길동"}
print(my_dict)
my_dict2 = dict()
my_dict2_1 = dict([("one", "하나"), ("two", "둘")])
print(my_dict2_1)  # {'one': '하나', 'two': '둘'}
my_dict3 = {"me": [1, 2, 3], "me2": "good"}

# 데이터 추가
dict4 = dict()
dict4["max"] = [1, 2, 3, 4]  # 데이터 삽입 {'max': [1, 2, 3, 4]}
print(dict4)
"""
dict() 를 통해 빈 딕셔너리를 만든 후

데이터 삽입을 하여 키가 4개 , 각각의 밸류에는 다른 타입의 데이터를 넣어서

그 딕셔너리를 출력 

"""

# 데이터 읽기
person = {"name": "licat", "age": 25, "height": 165.5}
print(f"이름은 : {person["name"]} 입니다.")
print(f"나이는 : {person["age"]} 입니다.")

# print(f"생년월일은 : {person["good"]}") KeyError: 'good'

# 데이터 수정
person["age"] = 30  # age 키를 통해 value의 값을 30으로 변경
print(person)

# 데이터 삭제
del person["height"]
print(person)

person["age"] = None  # 키를 남기고 값을 없애고 싶을 때

a = {"good": ["a", "b", "c"]}

a["good"].remove(
    "c"
)  # 해당 value에 접근한 후, 리스트의 remove기능을 통해 데이터를 지운다.

print(a)  # {'good': ['a', 'b']}

b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
# "good1": {"good2": [1, 2, 3, [1, 2, 3, 4]]}}
b["good1"]["good2"][3].append(4)
print(b)

person = {"name": "licat", "age": 25, "city": "seoul"}

# get(키,키가 없을 경우의 value)
city = person.get('city',"없는뎅")
print(city)
city2 = person.get('city2',"없는뎅")
print(city2)


person = {"name": "licat", "age": 25, "city": "seoul"}
# 키만 가져온다.

person_keys = person.keys() #키 값들만 추출
print(person_keys) # dict_keys(['name', 'age', 'city'])
a = list(person_keys) # 형변환
print(a)

# value 만추출
person_values = person.values() # 밸류 값들만 추출
print(person_values) # dict_values(['licat', 25, 'seoul'])
b = list(person_values)
print(b)

# 전체를 추출
person_items = person.items()
print(person_items) #dict_items([('name', 'licat'), ('age', 25), ('city', 'seoul')])
c = list(person_items) #[('name', 'licat'), ('age', 25), ('city', 'seoul')]
print(c)
print(type(person_items))
#del person['age'] 권장 x
a = person.pop("age") # age라는 키에 있는 값을 a에 저장장
print(a)