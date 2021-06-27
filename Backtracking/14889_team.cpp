#include <iostream>
using namespace std;
int minVal = 10000;

void minDiff(int n, int *s, int idx) {}
int main() {
    int n;
    cin >> n;
    int s[n][n];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> s[i][j];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout << s[i][j] << " ";
        cout << endl;
    }
    cout << endl;

    return 0;
}