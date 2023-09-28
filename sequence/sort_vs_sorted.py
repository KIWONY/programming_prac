# sort VS sorted
# reverse, key=len, key=str.lower, key=func

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'lemon']

print(f_list)
print('sorted:' , sorted(f_list))
print('sorted reverse:' , sorted(f_list, reverse=True))
print('sorted key len:' , sorted(f_list, key=len))
print('sorted lambda:' , sorted(f_list, key=lambda x : x[-1]))      # 마지막 글자를 기준으로

print('sorted:' , f_list)

# sort : 정렬 후 객체 직접 변경 (원본 직접 변경)
# 반환값 확인 (None)

print('sort: ',  f_list.sort(), f_list)     # 바뀐 것을 확인 가능
print('sort: ',  f_list.sort(reverse=True), f_list)


# list 와 array 적합한 사용법
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# array: 숫자 기반 (리스트와 거의 호환)



