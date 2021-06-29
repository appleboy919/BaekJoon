#include <iostream>
using namespace std;
int minVal = 10000;

void minDiff(int n, int **s, int idx, int *temp, int t1) {
    if (idx == n / 2) {
        int t2;
        int temp2[idx];

        // cout << "t1: " << t1 << "!\n";
        // int diff = abs(total - t1 * 2);
        if (minVal > diff)
            minVal = diff;
        return;
    }
    for (int i = idx; i < n - idx; i++) {
        int new_t1 = t1;
        temp[idx] = i;
        for (int j = 0; j < idx; j++) {
            new_t1 += s[temp[j]][i];
            new_t1 += s[i][temp[j]];
        }
        minDiff(n, s, idx + 1, temp, new_t1);
    }
}
int main() {
    int n;
    // int sum = 0;
    cin >> n;
    int **s;
    s = new int *[n];
    for (int i = 0; i < n; i++) {
        s[i] = new int[n];
        for (int j = 0; j < n; j++) {
            cin >> s[i][j];
            // sum += s[i][j];
        }
    }
    // cout << "sum: " << sum << endl;
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++)
    //         cout << s[i][j] << " ";
    //     cout << endl;
    // }
    int temp[n / 2];
    temp[0] = 0;

    minDiff(n, s, 1, temp, 0);
    cout << minVal << endl;
    return 0;
}