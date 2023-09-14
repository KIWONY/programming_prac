class Artist():
    """
    Artist class
    Author : KIWONY
    Date : 2023.09.04
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    # 인스턴스 메소드
    def __init__(self, album, detail):
        self._album = album
        self._detail = detail

    def __str__(self):
        return 'str : {} - {}'.format(self._album, self._detail)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._album, self._detail)


    # 인스턴스 메소드
    # self : 객체의 `고유한` 속성 값을 사용 - 내꺼.
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Detail info : {} {}'.format(self._album, self._detail.get('price')))

    def get_price(self):
        return f'Before album price -> album : {self._album}, price : {self._detail.get("price")}'

    def get_price_culc(self):
        return f'After album price -> album : {self._album}, price : {self._detail.get("price") * Artist.price_per_raise}'

    # 클래스 메소드
    @classmethod
    def raise_price(cls, per):
        # cls = 클래스 그 자체
        bool(cls.price_per_raise == Artist.price_per_raise)     # True
        if per <=1:
            print("Please enter 1 or more")

            cls.price_per_raise = per
            print("Succeed! price increased")

    @staticmethod
    def is_Wings(inst):
        if inst._album == "Wings":
            return f"album name is {inst._album}"
        return "not Wings"


artist1 = Artist('Wings', {"price": 20000})
artist2 = Artist('Young Forever', {"price": 25000})

# 전체 정보
artist1.detail_info()

# 가격정보(직접 접근)
artist2._detail.get('price') # -> 이렇게 직접 인스턴스 변수에 접근하는 방식은 좋지 않다. (자바의 캡슐 등)
# -> 그래서 주로 인스턴스 메소드를 생성하여 접근 -> get_price 메소드, get_price_culc 메소드

# 가격정보(인스턴스 메소드로 접근)
print(artist1.get_price())
print(artist2.get_price())

# 가격 인상(클래스 메소드 미사용)
Artist.price_per_raise = 1.4    ###### -> 이런 식으로 클래스 변수를 직접 수정하는 것보다 메소드를 사용해서 변경하는 것이 좋다.

# 가격 정보 (인상 후)
print(artist1.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Artist.raise_price(2.3)
print(artist1.get_price_culc())


# static 메소드는 매우 유연하다
# 인스턴스로 호출
print(artist1.is_Wings(artist1))
print(artist2.is_Wings(artist2))
# 클래스로 호출
print(Artist.is_Wings(artist1))
print(Artist.is_Wings(artist2))












