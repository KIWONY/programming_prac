# chapter02-01

# 객체 지향 프로그래밍(OOP) -> 장점: 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트에 적함
# 규모가 큰 프로젝트(프로그램)의 경우 함수 중심으로 짜면 데이터가 방대해져서 복잡해짐
# 이 때 클래스 중심으로 코딩하는 것은 데이터가 중심이 되는 것이기 때문에 객체로 관리됨.
# (함수 파라미터 감소, 프로그램 구성요소들이 객체로 관리됨)

# 일반적인 코딩의 경우
artist_1 = "BTS"
artist_detail_1 = [
    {'debut': 2013},
    {'song': 'DNA'}
]
artist_2 = "IU"
artist_detail_2 = [
    {'debut': 2008},
    {'song': 'Blueming'}
]

# 리스트 구조
# 관리하기가 불편하다
# 인덱스 접근 시 실수 할 가능성이 있다. 삭제가 불편하다.
artist_list = ["BTS", "IU"]
artist_detail_list = [
    {'debut': 2013, 'song': 'DNA'},
    {'debut': 2008, 'song': 'Blueming'}
]

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제가 있다. 키로 조회 했을 떄 예외 처리
artist_dicts = [
    {'artist': 'BTS', 'artist_detail': {'debut': 2013, 'song': 'DNA'}},
    {'artist': 'IU', 'artist_detail': {'debut': 2008, 'song': 'Blueming'}}
]

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Artist():
    def __init__(self, artist, details):
        self._artist = artist
        self._details = details

        # 사용자 입장에서의 프린트문으로 확인
    def __str__(self):
        return 'str : {} - {}'.format(self._artist, self._details)

        # 개발자가 객체 타입, 정보 확인
    def __repr__(self):
        return 'repr : {} - {}'.format(self._artist, self._details)

artist1 = Artist('BTS', {'debut': 2013, 'song': 'DNA'})
artist2 = Artist('IU', {'debut': 2008, 'song': 'Blueming'})

print(artist1)

# Class안 속성들 확인
print(artist1.__dict__)
# {'_artist': 'BTS', '_details': {'debut': 2013, 'song': 'DNA'}}

# 리스트 선언
artist_lst = []
artist_lst.append(artist1)
artist_lst.append(artist2)

a = [repr(i) for i in artist_lst]
print(a)
# ["repr : BTS - {'debut': 2013, 'song': 'DNA'}", "repr : IU - {'debut': 2008, 'song': 'Blueming'}"]

for x in artist_lst:
    print(x)        # str
    print(repr(x))  # repr 명시적 호출





