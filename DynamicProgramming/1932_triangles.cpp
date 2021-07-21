#include <iostream>
using namespace std;
int **c;
int main() {
    int n;
    cin >> n;
    c = new int *[n];
    for (int i = 0; i < n; i++) {
        c[i] = new int[i + 1];
        for (int j = 0; j < i + 1; j++)
            cin >> c[i][j];
    }
    return 0;
}