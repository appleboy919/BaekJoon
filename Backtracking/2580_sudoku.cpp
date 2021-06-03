#include <iostream>
#include <string>
using namespace std;

int find_number(int sudoku[9][9], int pos[2], bool nums[9]) {
    int rowNum, colNum;
    for (int i = 0; i < 9; i++) {
        rowNum = sudoku[pos[0]][i];
        colNum = sudoku[i][pos[1]];
        if (rowNum != 0 && !nums[rowNum - 1])
            nums[rowNum - 1] = true;
        if (colNum != 0)
            nums[row]
    }
}
void fill_sudoku(int sudoku[9][9]) {
    bool nums[9];
    for (int i = 0; i < 9; i++)
        nums[i] = false;
}
int main(void) {
    int sudoku[9][9];
    string t;
    int index;
    for (int i = 0; i < 9; i++) {
        index = 0;
        getline(cin, t);
        for (int j = 0; j < t.length(); j++) {
            if (t[j] != ' ') {
                sudoku[i][index] = t[j] - '0';
                index++;
            }
        }
    }
    fill_sudoku(sudoku);
    cout << endl;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++)
            cout << sudoku[i][j] << ' ';
        cout << endl;
    }
    return 0;
}