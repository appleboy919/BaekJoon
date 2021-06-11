#include <iostream>
#include <list>
#include <string>
int static MAX_BLANK = 81;
// #include <time.h>

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

void find_number(int sudoku[9][9], int row, int col, bool nums[9]) {
    int rowNum, colNum;
    for (int i = 0; i < 9; i++) {
        rowNum = sudoku[row][i];
        colNum = sudoku[i][col];
        if (rowNum != 0)
            nums[rowNum - 1] = false;
        if (colNum != 0)
            nums[colNum - 1] = false;
    }
    int row_i = row / 3 * 3;
    int col_i = col / 3 * 3;

    for (int i = row_i; i < row_i + 3; i++) {
        for (int j = col_i; j < col_i + 3; j++)
            if (sudoku[i][j] != 0)
                nums[sudoku[i][j] - 1] = false;
    }
}
bool fill_sudoku(int sudoku[9][9], int blank[MAX_BLANK][2], int num, int index,
                 bool nums[9]) {
    if (index == num)
        return true;
    if (index != 0 && blank[index - 1][0] != blank[index][0]) {
        for (int i = 0; i < 9; i++)
            nums[i] = true;
        find_number(sudoku, blank[index][0], blank[index][1], nums);
    }

    // bool nums[9] = {0};
    // string temp = *itr;
    // find_number(sudoku, pos1, pos2, nums);
    // int temp_sudoku[9][9];
    // copy(&sudoku[0][0], &sudoku[0][0] + 9 * 9, &temp_sudoku[0][0]);
    // for (int i = 1; i < 10; i++) {
    //     if (check(sudoku, row, col, i)) {
    //         sudoku[row][col] = i;
    //         if (fill_sudoku(sudoku, blank, num, index + 1))
    //             return true;
    //     }
    // }
    for (int i = 0; i < 9; i++) {
        if (nums[i]) {
            sudoku[blank[index][0]][blank[index][1]] = i + 1;
            if (fill_sudoku(sudoku, blank, num, index + 1, nums)) {
                cout << "reached the end with " << index << "("
                     << blank[index][0] << ", " << blank[index][1] << ") --> "
                     << i + 1 << endl;
                return true;
            }
        }
    }
    return false;
}
int main(void) {
    // clock_t start = clock();
    int sudoku[9][9];
    // list<string> blank;
    int num = 0;
    int blank[MAX_BLANK][2];
    int index;
    bool nums[9] = {1};
    string t;

    // try to use getline and strtok funtion to read the input sudoku
    for (int i = 0; i < 9; i++) {
        index = 0;
        getline(cin, t);
        for (int j = 0; j < 18; j++) {
            cout << "\n in\t" << t[j];
            if (t[j] != ' ') {
                if (t[j] == '0') {
                    // blank.push_back(to_string(i) + to_string(index));
                    blank[num][0] = i;
                    blank[num][1] = index;
                    num++;
                }
                sudoku[i][index] = t[j] - '0';
                index++;
            }
        }
        cout << endl;
        cout << "!!" << num << endl;
    }
    cout << endl << num << endl;

    fill_sudoku(sudoku, blank, num, 0, nums);
    cout << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++)
            cout << sudoku[i][j] << " ";
        cout << endl;
    }
    // cout << "time: " << (double)(clock() - start) << endl;
}
