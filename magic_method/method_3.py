# special method (=magic method)
# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id(identity), type -> value
# 튜플의 각 요소에 이름을 부여하는 것.
# 데이터 모델링

# 일반적인 튜플
# 두 점 사이 거리 구하기
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt  # 루트
l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1]-pt2[1]) ** 2)
print(l_leng1, "Not namedtuple")


# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)
print(pt3.x)
print(pt3[0])

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y-pt4.y) ** 2)

print(l_leng2)

# 네임드 유플 선언 방법
Point1 = namedtuple('Point1', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # default 는 False,
# class는 예약어이므로 rename을 사용하여 클래스 객체 상태로 랩핑가능하도록 설정

print(Point1, Point2, Point3, Point4)   # 출력 : 클래스

# Dictionary to unpacking
temp_dict = {'x' : 30, 'y' : 10}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 30)
p3 = Point3(24, y=10)

p4 = Point4(24, 10, 20, 23)       # rename
p5 = Point3(**temp_dict)          # unpacking

print(p1, p2, p3)
print(p4)      # 출력 : Point(x=24, y=10, _2=20, _3=23)  _2와 _3이라는 난수로 변수를 만듦
print(p5)      # 딕셔너리 unpacking

# 사용
print(p1.x + p2.y)

# Unpacking 
x, y = p2
print(x,y)


# 네임드 튜플 메소드
temp = [12, 20]

# _make() : 새로운 객체 생성 , 개수가 맞아야 작동하므로 엄격한 코딩 가능
p4 = Point1._make(temp)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : dictionary로 반환
print(p1._asdict())             # {'x': 10, 'y': 35}
print(p4._asdict())
print(p5._asdict())

# 실 사용 실습
# 반 20명, 4개의 반(a, b, c, d)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'a b c d'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(students)

# 추천하는 방식
students2 = [Classes(rank, number)
             for rank in 'a b c d'.split()
                for number in [str(n)
                    for n in range(1,21)]]

print(students == students2)        # True