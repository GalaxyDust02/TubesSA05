import time

start_time = time.time()


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def solve_sudoku(board, show_steps=False):
    find = find_empty(board)
    if not find:
        # Jika tidak ada kotak kosong lagi, maka papan Sudoku terisi dengan benar
        return True

    row, col = find

    for num in range(1, 10):
        board[row][col] = num

        if show_steps:
            # Menampilkan papan Sudoku pada setiap langkah pengisian
            print("Langkah : Memasukkan angka {} ke Kolom {} dan Baris {}".format(
                num, col+1, row+1))
            print_board(board)
            print("")

        if valid(board, num, (row, col)) and solve_sudoku(board, show_steps):
            return True

    # Jika tidak ada solusi yang ditemukan, kembali ke nilai 0
    board[row][col] = 0
    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


# ...

# Input user
input_board = []
for i in range(9):
    row = input("Masukkan baris ke-{} tanpa spasi: ".format(i + 1))
    input_board.append([int(num) if num.isdigit() else 0 for num in row])

# Cetak board inputan user
print("Board inputan user:")
print_board(input_board)
print("")

# Tanyakan apakah langkah-langkah harus ditampilkan atau tidak
show_steps = input(
    "Apakah Anda ingin menampilkan langkah-langkah? (ya/tidak): ").lower() == "ya"

# Cari solusi untuk board inputan user dengan
if solve_sudoku(input_board, show_steps):
    print("Berikut adalah solusi untuk papan Sudoku yang diberikan:")
    print_board(input_board)
else:
    print("Tidak ada solusi yang ditemukan untuk papan Sudoku yang diberikan.")

elapsed_time = time.time() - start_time
print("Waktu eksekusi: {:.6f} detik".format(elapsed_time))
