# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형을 저장할 수 있음 [list, tuple, collections.deque]
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Interator(이터레이터): 값을 차례대로 반환할 수 있는 객체
# Generator(제너레이터): 이터레이터를 생성하는 함수 /  호출되면 즉시 실행되지 않고 제너레이터 객체를 반환

# 지능형 리스트(Comprehending list)
chars = '+_)(*&^%$#@!~'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))   # unicode

print(code_list1)

# Comprehending lists
code_list2 = [ord(s) for s in chars]

print(code_list1 == code_list2)     # True

# Comprehending lists + Map , Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3)
print([chr(o) for o in code_list3])     # unicode to character

# Generator 생성

# 제너레이터는 한 번에 한 개의 항목을 생성 (메모리 유지 x)
tuple_c = [i for i in code_list3]
print(tuple_c)      # 값을 만들어 버림, 메모리 모두 사용

tuple_g= (i for i in code_list3)
print(tuple_g)          # <generator object <genexpr> at 0x100f60270>
print(type(tuple_g))    # 값을 생성 하지 않고, 첫번쨰 값을 반환할 준비를 하고 있는 상태
print(next(tuple_g))    # 값을 하나씩 반환
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
# 모두 반환 후에는 StopIteration 발생

import array
# array: 수치 연산이나 어떤 하나의 데이터 타입을 이용한 어떤 최적화된 그런 자료

array_g = array.array('I', (ord(s) for s in chars))

print(type(array_g))        # <class 'array.array'>
print(array_g.tolist())     # list로 convert


students3 = ('%s' % c + str(n)
             for c in 'a b c d'.split()
                for n in range(1,21))

print(students3)        # <generator object <genexpr> at 0x100a7cba0>

for s in ('%s' % c + str(n)
             for c in 'a b c d'.split()
                for n in range(1,21)):
    print(s)

# 리스트 주의
marks1 =[['~'] * 2 for _ in range(3)]
marks2 =[['~'] * 2] * 3
print(marks1, marks2 , marks1==marks2)
# [['~', '~'], ['~', '~'], ['~', '~']] [['~', '~'], ['~', '~'], ['~', '~']] True

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)   # [['~', 'X'], ['~', '~'], ['~', '~']]
print(marks2)   # [['~', 'X'], ['~', 'X'], ['~', 'X']]

# 출력
print([id(i) for i in marks1])      # id 값이 모두 다르다 [4350772416, 4350772224, 4350772160]
                                    # 내부의 각 리스트는 서로 다른 객체이다
print([id(i) for i in marks2])      # id 값이 모두 같다 [4350772032, 4350772032, 4350772032]
                                    # 모두 같은 리스트 객체를 참조하고 있다


