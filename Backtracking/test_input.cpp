#include <cstring>
#include <iostream>
using namespace std;
int main() {
    int sudoku[9][9];
    // char input[1000] =
    //     "0 3 5 4 6 9 2 7 8\n7 8 2 1 0 5 6 0 9\n0 6 0 2 7 8 1 3 5\n3 2 1 0 4 6
    //     " "8 9 7\n8 0 4 9 1 3 5 0 6\n5 9 6 8 2 0 4 1 3\n9 1 7 6 5 2 0 8 0\n6
    //     0 3 " "7 0 1 9 5 2\n2 5 8 3 9 4 7 6 0";
    char input[20];
    // string input;
    char *token;
    int col;
    for (int i = 0; i < 9; i++) {
        cin.getline(input, 19);
        cout << "input: " << input << "!" << endl;
        col = 0;
        token = strtok(input, " ");
        while (token) {
            // if (strcmp(token, "\n") == 0)
            //     continue;
            sudoku[i][col] = stoi(token);
            token = strtok(NULL, " ");
            col++;
        }
    }
    cout << endl;
    for (int i = 0; i < 9; i++) {
        cout << i << ": ";
        for (int j = 0; j < 9; j++)
            cout << sudoku[i][j] << " ";
        cout << endl;
    }
    return 0;
}