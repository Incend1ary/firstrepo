class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self):
        print(f"{self.__length * self.__width * 25 * 5 }")


t = Road(20, 5)
t.mass()
