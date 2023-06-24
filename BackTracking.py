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

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve_sudoku(board, show_steps=False):
    find = find_empty(board)
    if not find:
        # Jika tidak ada kotak kosong lagi, maka papan Sudoku terisi dengan benar
        return True
    else:
        row, col = find

    for i in range(1, 10):
        pos = row, col
        if valid(board, i, pos):
            board[row][col] = i

            if show_steps:
                # Menampilkan papan Sudoku pada setiap iterasi
                print("Langkah : Memasukkan angka {} ke Kolom {} dan Baris {}".format(
                    i, i, row+1, col+1))
                print_board(board)
                print("")

            if solve_sudoku(board, show_steps):
                return True

            # Jika tidak ada solusi yang ditemukan, kembali ke nilai 0
            board[row][col] = 0

    return False

def valid(board, num, pos):
    # Check row
    i = 1
    for i in range(len(board[0])): #len(board[0]) = kolom; Jadi loop ini utk mengecek baris dr kolom pertama (indeks ke 0) hingga trakhir
        if board[pos[0]][i] == num and pos[1] != i: #pos[0] = baris; pos[1] = kolom
            return False

    # Check column
    i = 1
    for i in range(len(board)): #len(board) = baris; Jadi loop ini utk mengecek kolom dr baris pertama (indeks ke 0) hingga trakhir
        if board[i][pos[1]] == num and pos[0] != i: #pos[0] = baris; pos[1] = kolom
            return False

    # Check box
    box_x = pos[1] // 3 #pos[1] = kolom
    box_y = pos[0] // 3 #pos[0] = baris

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# ...

# Input user
input_board = []
for i in range(9):
    row = input(
        "Masukkan baris ke-{} tanpa spasi: ".format(i + 1))
    input_board.append([int(num) if num.isdigit() else 0 for num in row])

# Cetak board inputan user
print("Board inputan user:")
print_board(input_board)
print("")

# Tanyakan apakah langkah-langkah harus ditampilkan atau tidak
show_steps = input(
    "Apakah Anda ingin menampilkan langkah-langkah? (ya/tidak): ").lower() == "ya"

# Cari solusi untuk board inputan user dengan mengontrol tampilan langkah-langkah
if solve_sudoku(input_board, show_steps):
    print("Berikut adalah solusi untuk papan Sudoku yang diberikan:")
    print_board(input_board)
else:
    print("Tidak ada solusi yang ditemukan untuk papan Sudoku yang diberikan.")

elapsed_time = time.time() - start_time
print("Waktu eksekusi: {:.6f} detik".format(elapsed_time))

'''
Contoh Inputannya :

050002790
700460003
400100000
009000500
001025037
000000419
082094000
534000962
910230005
'''