if __name__:
    print("*" * 5, "Игра Крестики - нолики", '*' * 5)
    board = list(range(1, 10))

    def draw_board(board):
        print(("+---" * 3 + "+").strip())
        for i in range(3):
            print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
            print(("+---" * 3 + "+").strip())

    def play(xo):
        correct = False
        while not correct:
            answer = input("Куда поставим " + xo + "? ")
            try:
                answer = int(answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число? ")
                continue
            if 0 < answer < 10:
                if (str(board[answer-1]) not in "XO"):
                    board[answer-1] = xo
                    correct = True
                else:
                    print("Эта клетка уже занята")
            else:
                print("Некорректный ввод. Ввведите число от 1 до 9")

    def check_win(board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for item in win_coord:
            if board[item[0]] == board[item[1]] == board[item[2]]:
                return board[item[0]]
            return False

    def main(board):
        counter = 1
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                play("X")
            else:
                play("O")
            counter += 1
            if 4 < counter < 9:
                if check_win(board):
                    print(check_win(board), "ура! вы выиграли")
                    win = True
                    break
            if counter == 9:
                print("ничья")
                break
        draw_board(board)

    main(board)

    input("нажмите Enter для выхода")