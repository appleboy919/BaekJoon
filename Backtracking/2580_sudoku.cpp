#include <iostream>
#include <list>
#include <string>
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
void fill_sudoku(int sudoku[9][9], list<string> blank) {
    bool nums[9] = {0};
    for (int i = 0; i < 9; i++)
        nums[i] = true;
    for (list<string>::iterator itr = blank.begin(); itr != blank.end();
         itr++) {
        string temp = *itr;
        int pos1 = temp[0] - '0';
        int pos2 = temp[1] - '0';
        bool temp_nums[9];
        copy(nums, nums + 9, temp_nums);
        find_number(sudoku, pos1, pos2, temp_nums);
        }
    for (int i = 0; i < 9; i++) {
        // fill_number(sudoku, )
    }
}
int main(void) {
    int sudoku[9][9];
    list<string> blank;
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
    // fill_sudoku(sudoku), blank;
    cout << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++)
            cout << sudoku[i][j] << ' ';
        cout << endl;
    }
    for (list<string>::iterator iter = blank.begin(); iter != blank.end();
         iter++) {
        cout << *iter << " ";
    }
    cout << endl;
}