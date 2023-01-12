from Operaciones.obtenerTabla import get_board


def main():
    board_ = get_board()
    for item in board_:
        print(item.get_text())
        print('--o--'*10)


if __name__ == '__main__':
    main()
