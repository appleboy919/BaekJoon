#include <iostream>
using namespace std;
int dp[10001] = {0};

int solve(int n, int *c, int idx, int cont) {
    if (idx > n)
        return 0;
    if (dp[idx] == 0) {
        int t1 = 0;
        if (cont < 2)
            t1 = solve(n, c, idx + 1, cont + 1);
        int t2 = solve(n, c, idx + 2, 1);
        dp[idx] = c[idx] + t1 > t2 ? t1 : t2;
    }
    cout << dp[idx] << " ";
    return dp[idx];
}
int main() {
    int n;
    cin >> n;
    int c[n];
    for (int i = 0; i < n; i++)
        cin >> c[i];
    solve(n, c, 1, 1);
    solve(n, c, 2, 1);
    cout << solve(n, c, 0, 0) << endl;
    return 0;
}