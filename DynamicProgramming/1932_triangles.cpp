#include <iostream>
using namespace std;
int **c;
int **dp;
int maxCost(int n, int k, int idx) {
    if (k == n - 1)
        return c[k][idx];
    if (dp[k][idx] == 0) {
        int t1 = maxCost(n, k + 1, idx) + c[k][idx];
        int t2 = maxCost(n, k + 1, idx + 1) + c[k][idx];
        dp[k][idx] = t1 > t2 ? t1 : t2;
    }
    return dp[k][idx];
}
int main() {
    int n;
    cin >> n;
    c = new int *[n];
    dp = new int *[n];
    for (int i = 0; i < n; i++) {
        c[i] = new int[i + 1];
        dp[i] = new int[i + 1];
        for (int j = 0; j < i + 1; j++)
            cin >> c[i][j];
    }
    cout << maxCost(n, 0, 0) << endl;
    for (int i = 0; i < n; i++) {
        delete c[i];
        delete dp[i];
    }
    delete c;
    delete dp;
    return 0;
}