class Rectangle:
    def __init__(self, h, w, x=0, y=0):
        """
        Объявление прямоугольника в координатах
        (x, y) и с высотой, шириной (h, w)
        :param h: Высота,
        :param w: Ширина,
        :param x: Координата по оси X,
        :param y: Координата по оси Y
        """
        if type(x) != int != type(x) != float:
            raise TypeError('Неверный тип для x', type(x))
        if type(y) != int != type(y) != float:
            raise TypeError('Неверный тип для y', type(y))
        if type(h) != int != type(h) != float:
            raise TypeError('Неверный тип для h', type(h))
        if type(w) != int != type(w) != float:
            raise TypeError('Неверный тип для w', type(w))
        if h < 0:
            raise TypeError('Высота не может быть < 0')
        if w < 0:
            raise TypeError('Ширина не может быть < 0')
        self.__rectangle = {
            'x': x,
            'y': y,
            'h': h,
            'w': w
        }

    def get_rectangle(self):
        """
        :return: Возвращает текущие параметры прямоугольника
        """
        return self.__rectangle

    def get_coords(self):
        """
        Возвращает текущие координаты вершин прямоугольника
        [(Левый нижний), (Левый верхний), (Правый верхний), (Правый нижний)] углы
        :return: Array
        """
        x = self.__rectangle['x']
        y = self.__rectangle['y']
        width = self.__rectangle['w']
        height = self.__rectangle['h']
        return [(round(x, 2), round(y, 2)), (round(x, 2), round(y + height, 2)),
                (round(x + width, 2), round(y + height, 2)), (round(x + width, 2), round(y, 2))]

    def set_coords(self, x, y):
        """
        Устанавливает прямоугольнику координаты левого нижнего угла
        :type x: int
        :type y: int
        :param x: Int
        :param y: Int
        :return: Массив с новыми координатами вершин
        """
        if type(x) != int != type(x) != float:
            raise TypeError('Неверный тип для x', type(x))
        if type(y) != int != type(y) != float:
            raise TypeError('Неверный тип для y', type(y))

        self.__rectangle['x'] = round(x, 2)
        self.__rectangle['y'] = round(y, 2)

        return self.get_coords()

    def move_to(self, x, y):
        """
        Смещает прямоугольник относительно текущих координат
        :param x: смещение по оси X
        :param y: смещение по оси Y
        :return: Массив с новыми координатами вершин
        """
        if type(x) != int != type(x) != float:
            raise TypeError('Неверный тип для x', type(x))
        if type(y) != int != type(y) != float:
            raise TypeError('Неверный тип для y', type(y))

        self.__rectangle['x'] += round(x, 2)
        self.__rectangle['y'] += round(y, 2)

        return self.get_coords()

    def resize(self, w, h):
        """
        Меняет размер прямоугольника
        :param w: Желаемая ширина прямоугольника
        :param h: Желаемая высота прямоугольника
        :return: Массив с новыми координатами вершин
        """
        if type(h) != int != type(h) != float:
            raise TypeError('Неверный тип для h', type(h))
        if type(w) != int != type(w) != float:
            raise TypeError('Неверный тип для w', type(w))
        if h < 0:
            raise TypeError('Высота не может быть < 0')
        if w < 0:
            raise TypeError('Ширина не может быть < 0')
        self.__rectangle['w'] = round(w, 2)
        self.__rectangle['h'] = round(h, 2)

    def resize_to(self, w, h):
        """
        Изменение размера прямоугольника относительно текущего размера
        :param w: изменение ширины
        :param h: изменение высоты
        :return: Массив с новыми координатами вершин
        """
        if type(h) != int != type(h) != float:
            raise TypeError('Неверный тип для h', type(h))
        if type(w) != int != type(w) != float:
            raise TypeError('Неверный тип для w', type(w))
        if self.__rectangle['h'] + round(h, 2) < 0:
            raise TypeError('Высота не может быть < 0')
        if self.__rectangle['w'] + round(w, 2) < 0:
            raise TypeError('Ширина не может быть < 0')
        self.__rectangle['w'] += round(w, 2)
        self.__rectangle['h'] += round(h, 2)

        return self.get_coords()

    def combination(self, second_rectangle):
        """
        Строит наименьший прямоугольник, содержащий оба заданных (относительно координат)
        :type second_rectangle: Rectangle
        :param second_rectangle: второй прямоугольник
        :return: Возвращает третий прямоугольник, содержащий оба входных
        """
        if type(second_rectangle) != type(self):
            raise TypeError('Неверный тип для second_rectangle', type(second_rectangle))


        fc = self.get_coords()
        sc = second_rectangle.get_coords()
        min_x = min([i[0] for i in fc] + [i[0] for i in sc])
        max_x = max([i[0] for i in fc] + [i[0] for i in sc])
        min_y = min([i[1] for i in fc] + [i[1] for i in sc])
        max_y = max([i[1] for i in fc] + [i[1] for i in sc])

        return Rectangle(x=min_x, y=min_y, w=max_x-min_x, h=max_y-min_y)

    def intersection(self, second_rectangle):
        """
        Строит зону пересечения исходных прямоугольников
        :type second_rectangle: Rectangle
        :param second_rectangle: второй прямоугольник
        :return: Возвращает новый прямоугольник, являющийся пересечением 2х исходных
        """
        if type(second_rectangle) != type(self):
            raise TypeError('Неверный тип для second_rectangle', type(second_rectangle))

        second_rectangle = second_rectangle.get_rectangle()
        min_h = min(self.__rectangle['h'], second_rectangle['h'])
        min_w = min(self.__rectangle['w'], second_rectangle['w'])

        return Rectangle(h=min_h, w=min_w)

    def intersection_on_flat(self, second_rectangle):
        """
        Строит зону пересечения исходных прямоугольников (на координатной плоскости)
        :type second_rectangle: Rectangle
        :param second_rectangle: второй прямоугольник
        :return: Возвращает новый прямоугольник, являющийся пересечением 2х исходных
        """
        if type(second_rectangle) != type(self):
            raise TypeError('Неверный тип для second_rectangle', type(second_rectangle))

        fr = self.get_coords()
        sr = second_rectangle.get_coords()

        # R1.y < R2.y1 (левый верхний первого ниже правого нижнего второго)
        # R1.y1 > R2.y (правый нижний выше первого правого верхнего второго)
        # R1.x1 < R2.x (правый нижний первого правее левого верхнего второго)
        # R1.x > R2.x1 (левый верхний первого левее правого нижнего второго)
        # Проверка на пересечение прямоугольников на плоскости (от противного)
        cross = not (fr[1][1] < sr[3][1] or fr[3][1] > sr[1][1] or
                     fr[3][0] < sr[1][0] or fr[1][0] > sr[3][0])

        if cross:
            right_x = sr[3][0] if fr[3][0] > sr[3][0] else fr[3][0]
            left_x = fr[1][0] if fr[1][0] > sr[1][0] else sr[1][0]
            upper_y = sr[1][1] if fr[1][1] > sr[1][1] else fr[1][1]
            bottom_y = sr[3][1] if fr[3][1] < sr[3][1] else fr[3][1]
            return Rectangle(x=left_x, y=bottom_y,
                             h=upper_y-bottom_y,
                             w=right_x-left_x)
        else:
            return False
