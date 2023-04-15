from time import sleep
from itertools import cycle


class TrafficLight:
    __traffic_color = [["red", 31, 7], ["yellow", 33, 3], ["green", 32, 7]]

    def running(self):
        for color in cycle(self.__traffic_color):
            print(f"\r\033[{color[1]}mгорит {color[0]} ", end="")
            sleep(color[2])


t = TrafficLight()
t.running()
