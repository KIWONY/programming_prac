# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형을 저장할 수 있음 [list, tuple, collections.deque]
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a , b  (할당)
print(divmod(100, 9))       # (11, 1),
print(divmod(*(100, 9)))    # (11, 1), 튜플 (100, 9)을 언패킹하여 divmod 함수에 전달
print(*(divmod(100, 9)))    # 11 1, divmod(100, 9)결과 값을 언패킹하여 전달

x, y, *rest = range(10)     # 언패킹하여 전달
print(x, y, rest)
# 0 1 [2, 3, 4, 5, 6, 7, 8, 9], 나머지는 패킹된 것을 알 수 있음
x, y, *rest = range(2)
print(x, y, rest)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

# 재할당
l = l * 2
m = m * 2

# 새로운 변수에 재할당 했으므로 id 다름
print(l, id(l))     # 4365383520
print(m, id(m))     # 4364925632

l *= 2
m *= 2

print(l, id(l))     # 4365220400        # 튜플은 불변형이라서 새로운 아이디값 부여
print(m, id(m))     # 4364925632        # 리스트는 가변형이라서 같은 아이디에 재할당




