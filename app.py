sudoku = [
    [5, 0, 0, 0, 0, 1, 2, 0, 6],
    [6, 9, 0, 4, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [7, 0, 0, 0, 9, 8, 5, 0, 1],
    [8, 6, 0, 0, 0, 0, 0, 2, 7],
    [1, 0, 4, 2, 7, 0, 0, 0, 9],
    [4, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 5, 0, 2, 0, 0, 6, 8],
    [2, 0, 3, 1, 0, 0, 0, 0, 5],
]

for i in range(0, 9, 1):
    for j in range(0, 9, 1):
        if sudoku[i][j] == 0:
            elemento = sudoku[i][j] + 1
            while True:
                for k in range(0,9,1):
                    if elemento == sudoku[k][j] or elemento in sudoku[i]:
                        elemento += 1
                        continue

                    else:
                        sudoku[i][j] = elemento
                        break
                    



                break

print(sudoku)


