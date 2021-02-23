'''
A. Исполнитель Робот
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Напишите класс Robot, который инициализируется с начальными координатами – положением Робота на плоскости, обе координаты заключены в пределах от 0 до 100.

Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W). Выйти за границы плоскости Робот не может.

Метод move() принимает строку – последовательность команд перемещения робота, каждая буква строки соответствует перемещению на единичный интервал в направлении, указанном буквой. Метод возвращает кортеж координат – конечное положение Робота после перемещения.

Метод path() вызывается без аргументов и возвращает список кортежей координат точек, по которым перемещался Робот при последнем вызове метода move. Если метод не вызывался, возвращает список с одним кортежем – начальным положением Робота.

Пример
Ввод	Вывод
from solution import Robot

r = Robot((0, 0))
print(r.move('NENW'))
print(*r.path())
(0, 2)
(0, 0) (0, 1) (1, 1) (1, 2) (0, 2)
'''

class Robot:
    def __init__(self, startCoordinates):
        self.x = startCoordinates[0]
        self.y = startCoordinates[1]
        self.tracklist = []
        self.trackreset()

    def trackreset(self):
        self.tracklist = [(self.x, self.y)]

    def move(self, instructions):
        coordinates = (self.x, self.y)
        self.trackreset()
        for i in range(0, (len(instructions))):
            if instructions[i] == 'N' and self.y < 100:
                self.y += 1
            if instructions[i] == 'S' and self.y > 0:
                self.y -= 1
            if instructions[i] == 'E' and self.x < 100:
                self.x += 1
            if instructions[i] == 'W' and self.x > 0:
                self.x -= 1
            self.track()
            coordinates = (self.x, self.y)
        return (coordinates)

    def track(self):
        currentcoordinates = (self.x, self.y)
        self.tracklist.append(currentcoordinates)

    def path(self):
        pathlist = self.tracklist
        return pathlist


if __name__ == '__main__':
    r = Robot((0, 0))
    #print(r.move('NENW'))
    print(*r.path())

