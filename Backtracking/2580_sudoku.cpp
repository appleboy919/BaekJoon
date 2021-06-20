#include <cstring>
#include <iostream>
#define MAX_BLANK 81

using namespace std;

bool check(int sudoku[9][9], int row, int col, int num) {
    int rowNum, colNum;
    for (int i = 0; i < 9; i++)
        if (sudoku[row][i] == num || sudoku[i][col] == num)
            return false;

    int row_i = row / 3 * 3;
    int col_i = col / 3 * 3;
    for (int i = row_i; i < row_i + 3; i++) {
        for (int j = col_i; j < col_i + 3; j++)
            if (sudoku[i][j] == num)
                return false;
    }
    return true;
}

bool fill_sudoku(int sudoku[9][9], int blank[MAX_BLANK][2], int num,
                 int index) {
    if (index == num)
        return true;
    for (int i = 1; i < 10; i++) {
        if (check(sudoku, blank[index][0], blank[index][1], i)) {
            sudoku[blank[index][0]][blank[index][1]] = i;
            if (fill_sudoku(sudoku, blank, num, index + 1))
                // reached the end successfully
                return true;
        }
    }
    // step-back the current cell to 0
    sudoku[blank[index][0]][blank[index][1]] = 0;
    return false;
}
int main(void) {
    int sudoku[9][9];
    int num = 0;
    int blank[MAX_BLANK][2];
    char input[20];
    char *token;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> sudoku[i][j];
            if (sudoku[i][j] == 0) {
                blank[num][0] = i;
                blank[num][1] = j;
                num++;
            }
        }
    }

    fill_sudoku(sudoku, blank, num, 0);
    cout << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++)
            cout << sudoku[i][j] << " ";
        cout << endl;
    }
}
