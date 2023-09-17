# special method (=magic method)
# 파이썬의 핵심 -> 시퀀스(squence), 반복(iterator), 함수(function), class(클래스)
# 클래스 안에 정의할 수 있는 특별한 (built-in) 메소드

# 기본형
print(int)      # class
print(float)    # class

# 모든 속성 및 메소드 출력
print(dir(int))                     # int에 대한 모든 속성과 메소드
print(dir(float))

n = 10

print(n+100)                        # 랩핑
print(n.__add__(100))               # 내부적으로 호출이 되는 것

print(n.__bool__() == bool(n))      # True
print(n * 100 ==  n.__mul__(100))   # True


# 클래스 예제
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit class info : {self._name}, {self._price}"

    def __add__(self, x):
        print('Called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called __le__')
        return True if self._price <= x._price else False

    def __ge__(self, x):
        print('Called __ge__')
        return True if self._price >= x._price else False

s1 = Fruit("Orange", 8000)
s2 = Fruit("Banana", 5000)

print(s1 + s2)      # self에 s1가 인자로, x에 s2가 인자로 들어가게 된다.
# 일반적인 계산 = s1._price + s2._price

# 매직 메소드
print(s1 >= s2)
print(s1 <= s2)
print(s1-s2)






