class Artist():
    """
    Artist class
    Author : KIWONY
    Date : 2023.09.04
    """

    # 클래스 변수(모든 인스턴스가 공유)
    count = 0

    # 인스턴스 메소드
    def __init__(self, artist, details):
        self._artist = artist
        self._details = details
        Artist.count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._artist, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._artist, self._details)

    def __del__(self):
        Artist.count -=1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Artist Detail info : {} {}'.format(self._artist, self._details.get('song')))


# self의 의미
artist1 = Artist('BTS', {'debut': 2013, 'song': 'DNA'})
artist2 = Artist('IU', {'debut': 2008, 'song': 'Blueming'})

print(artist1._artist ==artist2._artist)        # False
print(artist1 is artist2)                       # False


# dir & __dict__ 확인
# 해당 인스턴스가 가지고 있는 모든 attribute들을 리스트형태로
# 상위로부터 오버라이딩 된 것까지 모두 표시
print(dir(artist1))     # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '........', '_artist', '_details']

# 인스턴스 안의 값들을 key와 value인 딕셔너리 형태로 확인
print(artist1.__dict__)     # {'_artist': 'BTS', '_details': {'debut': 2013, 'song': 'DNA'}}

# class doctring 주석 확인
print(Artist.__doc__)

# 인스턴스 메소드 실행
artist1.detail_info()        # self
Artist.detail_info(artist1)  # class로 인스턴스 메소드에 접근할 때는 인자를 넣어줘야함
artist2.detail_info()
Artist.detail_info(artist2)


# 비교
print(artist1.__class__, artist2.__class__)
print(id(artist1.__class__) == id(artist2.__class__))     #True 클래스 값이므로 클래스 id 동일

# 공유 확인
print(artist1.count)
print(artist2.count)
print(artist1.__dict__)
print(artist1.__dict__)
print(dir(artist1))

# 삭제 확인
del artist1
print(artist2.count)        # 1
print(Artist.count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생서 가능 : 인스턴스 검색 후 -> 상위 클래스 변후 or 부모 클래스 변수를 가져온다








