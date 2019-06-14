import random


def print_board(board):
    print("   ", end="")
    for col in range(len(board[0])):
        print("{:3}".format(col), end="")
    print()
    for row in range(len(board)):
        print("{:2}|".format(row), end="")
        for cell in board[row]:
            print("{:3}".format(cell), end="")
        print()


BOARD_ROW, BOARD_COL, NUM_MINES = 16, 30, 99
UNKNOWN, MINE = "", -1
generated = [[UNKNOWN] * BOARD_COL for _ in range(BOARD_ROW)]

file = open("board.pl", "w")
count: int = 0
while count < NUM_MINES:
    r = random.randint(0, BOARD_ROW - 1)
    c = random.randint(0, BOARD_COL - 1)
    if generated[r][c] == UNKNOWN:
        generated[r][c] = MINE
        file.write("mine({},{}).\n".format(r, c))
        count += 1
    else:
        continue

file.close()

# for r in range(BOARD_ROW):
    # for c in range(BOARD_COL):
        # if generated[r][c] != MINE:
            # nw = UNKNOWN if r - 1 < 0 or c - 1 < 0 else generated[r - 1][c - 1]
            # n_ = UNKNOWN if r - 1 < 0 else generated[r - 1][c]
            # ne = UNKNOWN if r - 1 < 0 or c + 1 > BOARD_COL - 1 else generated[r - 1][c + 1]
            # w_ = UNKNOWN if c - 1 < 0 else generated[r][c - 1]
            # e_ = UNKNOWN if c + 1 > BOARD_COL - 1 else generated[r][c + 1]
            # sw = UNKNOWN if r + 1 > BOARD_ROW - 1 or c - 1 < 0 else generated[r + 1][c - 1]
            # s_ = UNKNOWN if r + 1 > BOARD_ROW - 1 else generated[r + 1][c]
            # se = UNKNOWN if r + 1 > BOARD_ROW - 1 or c + 1 > BOARD_COL - 1 else generated[r + 1][c + 1]
            # generated[r][c] = [nw, n_, ne, w_, e_, sw, s_, se].count(MINE)

# print_board(generated)
