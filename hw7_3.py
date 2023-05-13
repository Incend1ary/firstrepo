class Cell:
    def __init__(self, number_of_cell):
        self.number_of_cell = number_of_cell

    def __add__(self, other):
        return Cell(self.number_of_cell + other.number_of_cell)

    def __sub__(self, other):
        result = self.number_of_cell - other.number_of_cell
        return result if result > 0 else "ошибка, Cell2 >Cell1 "

    def __mul__(self, other):
        result = self.number_of_cell * other.number_of_cell
        return result

    def __truediv__(self, other):
        result = self.number_of_cell / other.number_of_cell
        return result

    def make_order(self, raw):
        n = self.number_of_cell // raw
        return '\n'.join(['*' * raw for _ in range(n)]) + '\n' + '*' * (self.number_of_cell % raw)




cell1 = Cell(10)
cell2 = Cell(2)
print((cell1 + cell2).number_of_cell)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(15))
print(cell1 / cell2)
