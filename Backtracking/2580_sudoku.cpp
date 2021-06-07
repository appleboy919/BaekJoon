#include <iostream>
#include <list>
#include <string>
#include <time.h>

using namespace std;

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
bool fill_sudoku(int sudoku[9][9], list<string> blank,
                 list<string>::iterator itr) {
    bool nums[9] = {0};
    for (int i = 0; i < 9; i++)
        nums[i] = true;
    string temp = *itr;
    int pos1 = temp[0] - '0';
    int pos2 = temp[1] - '0';
    find_number(sudoku, pos1, pos2, nums);
    for (int i = 0; i < 9; i++) {
        if (nums[i]) {
            sudoku[pos1][pos2] = i + 1;
            if (*itr == blank.back() || fill_sudoku(sudoku, blank, ++itr))
                return true;
        }
    }
    return false;
}
int main(void) {
    clock_t start = clock();
    int sudoku[9][9];
    list<string> blank;
    int init_size = 20;
    string t;
    int index;
    for (int i = 0; i < 9; i++) {
        index = 0;
        getline(cin, t);
        for (int j = 0; j < t.length(); j++) {
            if (t[j] != ' ') {
                if (t[j] == '0')
                    blank.push_back(to_string(i) + to_string(index));
                sudoku[i][index] = t[j] - '0';
                index++;
            }
        }
    }
    fill_sudoku(sudoku, blank, blank.begin());
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++)
            cout << sudoku[i][j] << " ";
        cout << endl;
    }
    cout << "time: " << (double)(clock() - start) << endl;
}
