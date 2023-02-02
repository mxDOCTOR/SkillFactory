def start():
    print('--------------------')
    print('   КРЕСТИКИ-НОЛИКИ  ')
    print('--------------------')
    print('  формат ввода: x y ')
    print('  x - номер строки  ')
    print('  y - номер столбца ')


def show():
    print()
    print('    | 0 | 1 | 2 | ')
    print('  --------------- ')
    for i, row in enumerate(excel):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print('  --------------- ')
    print()


def ask():
    while True:
        x_y = input('         Ваш ход: ').split()

        if len(x_y) != 2:
            print(' Введите 2 числа через пробел! ')
            continue

        x, y = x_y

        if not (x.isdigit()) or not (y.isdigit()):
            print(' Только числа! ')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(' Мимо! ')
            continue

        if excel[x][y] != ' ':
            print(' Клетка занята! ')
            continue

        return x, y


def check_win():
    win_x_y = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for x_y in win_x_y:
        symbols = []
        for c in x_y:
            symbols.append(excel[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл X!!!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выиграл 0!!!')
            return True
    return False


start()
excel = [[' '] * 3 for i in range(3)]
cnt = 0
while True:
    cnt += 1
    show()
    if cnt % 2 == 1:
        print(' Ходит крестик!')
    else:
        print(' Ходит нолик!')

    x, y = ask()

    if cnt % 2 == 1:
        excel[x][y] = 'X'
    else:
        excel[x][y] = '0'

    if check_win():
        break

    if cnt == 9:
        print(' Ничья!')
        break
