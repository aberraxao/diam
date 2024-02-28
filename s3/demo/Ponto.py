class Ponto:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self): return self.__x

    def getY(self): return self.__y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Ponto3D(Ponto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def getZ(self): return self.__z

    def __str__(self):
        return f'({self.getX()}, {self.getY()}, {self.getZ()}'


if __name__ == '__main__':
    p1 = Ponto(0, 0)
    p2 = Ponto(10, 20)
    p3 = Ponto()

    print(p1, type(p1))
    print(p2, type(p2))
    print(p3, type(p3))

    print(p2._Ponto__x, type(p2))

    p4 = Ponto3D(1, 2, 3)
    print(p4, type(p4))
