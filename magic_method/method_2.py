# 클래스 예제2
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object):
    def __init__(self, *args):  # 패킹되어 넘어온다고 생각하고 언패킹하기
        """
        Create a vector, example : v = Vector(5,10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        Return the vector information
        """
        print(f"Vector({self._x},{self._y}) yam yam")
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """
        Return the vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y , self._y * y)

    def __bool__(self):
        """
        checking if it's (0,0)
        Return True if it's not 0 when implemented(boolean method is already implemented)
        Return False if 0
        """
        check = bool(max(self._x, self._y))
        if check == False:
            print("WARNING: (0,0)")
        return check


print(Vector.__init__.__doc__)

v1 = Vector(5,7)
v2 = Vector(10,3)
v3 = Vector()
print(v1 + v2)
print(v1*3)
print(f"({bool(v1)}, {bool(v2)})")
print(bool(v3))