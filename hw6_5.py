class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"запуск отрисовки при помощи {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"запуск отрисовки ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"запуск отрисовки карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"запуск отрисовки маркером {self.title}")


st = Stationery("ручка")
st.draw()

pen = Pen("erichkrause")
pen.draw()

pencil = Pencil("белка")
pencil.draw()

handle = Handle("топмаркер")
handle.draw()






