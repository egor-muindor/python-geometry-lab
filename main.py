from rectangle_class import Rectangle


def debug_for_current(i):
    print(
        '''
Дебаг меню:
Редактируемый прямоугольник: {0} 
1) Перемещение прямоугольника
2) Изменение размера прямоугольника
3) Назад
        '''.format(i))
    return input('Введите № пункта меню: ')


def move_rectangle_menu(data):
    print('Перемещение прямоугольника:')
    print('Старые координаты: x: {}; y: {}'.format(data['x'], data['y']))
    print('Введите новые координаты левого нижнего угла:')
    try:
        x = round(float(input('\tВведите координату x: ')), 2)
        y = round(float(input('\tВведите координату y: ')), 2)
        return x, y
    except Exception as e:
        raise Exception('Ошибка перемещения прямоугольника')


def resize_rectangle_menu(data):
    print('Изменение размеров прямоугольника:')
    print('Старые размеры: высота: {}; ширина: {}'.format(data['h'], data['w']))
    print('Введите новые координаты левого нижнего угла:')
    try:
        w = round(float(input('\tВведите ширину прямоугольника:')), 2)
        h = round(float(input('\tВведите высота прямоугольника:')), 2)
        return h, w
    except Exception as e:
        raise Exception('Ошибка перемещения прямоугольника')


def find_combination_menu(rectangles_list):
    print(rectangles_list)
    print('Введите номера прямоугольников для сравнения:')
    try:
        first = int(input('Номер первого прямоугольника: '))
        second = int(input('Номер второго прямоугольника: '))
        return first, second
    except Exception as e:
        raise Exception('Ошибка выбора прямоугольников')

def find_intersection_menu(rectangles_list):
    print(rectangles_list)
    print('Введите номера прямоугольников для поиска пересечения:')
    try:
        first = int(input('Номер первого прямоугольника: '))
        second = int(input('Номер второго прямоугольника: '))
        return first, second
    except Exception as e:
        raise Exception('Ошибка выбора прямоугольников')


def main_menu():
    print(
        '''
Главное меню: 
1) Добавить новый прямоугольник
2) Посмотреть список прямоугольников
3) Редактировать прямоугольник
4) Поиск наименьшего общего прямоугольника
5) Поиск пересечения (относительно прямоугольников)
6) Поиск пересечения (относительно координатной плоскости)
7) Выход
        '''
    )
    return input('Введите № пункта меню: ')


def new_rectangle_menu():
    print('Добавление нового прямоугольника:')
    print('Введите координаты левого нижнего угла:')
    try:
        x = round(float(input('\tВведите координату x: ')), 2)
        y = round(float(input('\tВведите координату y: ')), 2)
        w = round(float(input('\tВведите ширину прямоугольника:')), 2)
        h = round(float(input('\tВведите высота прямоугольника:')), 2)
        return x, y, w, h
    except Exception as e:
        raise Exception('Ошибка добавления нового прямоугольника')


class Main:
    def __init__(self):
        self.rectangles = [Rectangle(4, 4, 0, 0), Rectangle(4, 4, 1, -1)]  # Предустановленные прямоугольники

    def add_new_rectangle(self, x, y, w, h):
        obj = Rectangle(h, w, x, y)
        self.rectangles.append(obj)

    def move_rectangle(self, x, y, index):
        obj = self.rectangles[index]
        obj.set_coords(x, y)

    def resize_rectangle(self, h, w, index):
        obj = self.rectangles[index]
        obj.resize(w, h)

    def list_of_rectangles(self, ):
        arr = []
        index = 0
        for rect in self.rectangles:
            str = 'Прямоугольник №{} с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                  '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(index,
                                                                                rect.get_rectangle()['w'],
                                                                                rect.get_rectangle()['h'],
                                                                                rect.get_rectangle()['x'],
                                                                                rect.get_rectangle()['y'])
            arr.append(str)
            index += 1
        return '\n_______________\n'.join(arr)


if '__main__' == __name__:
    menu = Main()
    while True:
        choice = main_menu()
        if '7' in choice:
            print('Пока!')
            exit(1)
        elif '1' in choice:  # добавление нового
            try:
                x, y, w, h = new_rectangle_menu()
                menu.add_new_rectangle(x, y, w, h)
                print(menu.list_of_rectangles())
                input('enter to continue')
            except Exception as e:
                print(e)
        elif '2' in choice:  # список
            print(menu.list_of_rectangles())
            input('enter to continue')
        elif '3' in choice:  # меню изменения
            i = int(input('Введите номер прямоугольника:'))
            while True:
                try:
                    data = menu.rectangles[i].get_rectangle()
                except:
                    print('Ошибка выбора')
                    break
                try:
                    debug_choice = debug_for_current(i)
                    if '3' in debug_choice:  # возврат в главное меню
                        break
                    elif '1' in debug_choice:  # изменение начала координат
                        x, y = move_rectangle_menu(data)
                        menu.move_rectangle(x, y, i)
                    elif '2' in debug_choice:  # изменение размера
                        h, w = resize_rectangle_menu(data)
                        menu.resize_rectangle(h, w, i)

                except Exception as e:
                    print(e)
        elif '4' in choice:
            try:
                r1, r2 = find_combination_menu(menu.list_of_rectangles())
                try:
                    r1 = menu.rectangles[r1]
                    r2 = menu.rectangles[r2]
                    r3 = r1.combination(r2)
                    cords = r3.get_coords()
                    print('Получился прямоугольник с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                          '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(r3.get_rectangle()['w'],
                                                                                        r3.get_rectangle()['h'],
                                                                                        r3.get_rectangle()['x'],
                                                                                        r3.get_rectangle()['y']))
                    print(
                        '''
Координаты вершин
{}\t\t{}
\t-------
\t|  \t  |
\t-------
{}\t\t{}
                        '''.format(cords[1], cords[2], cords[0], cords[3]))
                except Exception as e:
                    print('Неверный выбор прямоугольников')
            except Exception as e:
                print(e)
        elif '5' in choice:
            try:
                r1, r2 = find_intersection_menu(menu.list_of_rectangles())
                try:
                    r1 = menu.rectangles[r1]
                    r2 = menu.rectangles[r2]
                    r3 = r1.intersection(r2)
                    cords = r3.get_coords()
                    print('Получился прямоугольник с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                          '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(r3.get_rectangle()['w'],
                                                                                        r3.get_rectangle()['h'],
                                                                                        r3.get_rectangle()['x'],
                                                                                        r3.get_rectangle()['y']))
                    print(
                        '''
Координаты вершин
{}\t\t{}
\t-------
\t|  \t  |
\t-------
{}\t\t{}
                        '''.format(cords[1], cords[2], cords[0], cords[3]))
                except Exception as e:
                    print('Неверный выбор прямоугольников')
            except Exception as e:
                print(e)
        elif '6' in choice:
            try:
                r1, r2 = find_intersection_menu(menu.list_of_rectangles())
                try:
                    r1 = menu.rectangles[r1]
                    r2 = menu.rectangles[r2]
                    r3 = r1.intersection_on_flat(r2)
                    if not r3:
                        print('Прямоугольники не пересекаются на плоскости')
                        continue
                    cords = r3.get_coords()
                    print('Получился прямоугольник с параметрами: \n\tШирина: {}, \tВысота: {}, ' \
                          '\n\tКоординаты левого нижнего угла: \n\tx: {}; y: {}'.format(r3.get_rectangle()['w'],
                                                                                        r3.get_rectangle()['h'],
                                                                                        r3.get_rectangle()['x'],
                                                                                        r3.get_rectangle()['y']))
                    print(
                        '''
Координаты вершин
{}\t\t{}
\t-------
\t|  \t  |
\t-------
{}\t\t{}
                        '''.format(cords[1], cords[2], cords[0], cords[3]))
                except Exception as e:
                    print('Неверный выбор прямоугольников')
            except Exception as e:
                print(e)