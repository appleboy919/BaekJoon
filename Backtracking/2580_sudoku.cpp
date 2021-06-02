#include <iostream>
#include <string>
using namespace std;

void fill_sudoku(int sudoku[9][9]) {}
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