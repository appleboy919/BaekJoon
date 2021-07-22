#include <iostream>
using namespace std;
int *c;
long int **dp;
long int goUp(int n, int f, int prvStep) {
    if (f > n)
        return -1000 * n;
    if (f == n)
        return c[n - 1];
    if (dp[f - 1][prvStep - 1] == 0) {
        long int t1 = -1;
        long int t2;
        if (prvStep != 1 || f == 1)
            t1 = goUp(n, f + 1, 1) + c[f - 1];
        t2 = goUp(n, f + 2, 2) + c[f - 1];
        dp[f - 1][prvStep - 1] = t1 > t2 ? t1 : t2;
    }
    return dp[f - 1][prvStep - 1];
}
int main() {
    int n;
    cin >> n;
    c = new int[n];
    dp = new long int *[n];
    for (int i = 0; i < n; i++) {
        dp[i] = new long int[2];
        cin >> c[i];
    }
    long int t1 = goUp(n, 1, 1);
    long int t2 = 0;
    if (n >= 2)
        t2 = goUp(n, 2, 2);
    long int ans = t1 > t2 ? t1 : t2;
    cout << ans << endl;

    for (int i = 0; i < n; i++)
        delete[] dp[i];
    delete[] dp;
    delete[] c;
    return 0;
}