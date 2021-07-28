#include <iostream>
using namespace std;
int dp[10001] = {0};
int max(int n1, int n2) { return n1 > n2 ? n1 : n2; }
// int solve(int n, int *c, int idx, int cont) {
//     if (idx > n)
//         return 0;
//     if (dp[idx] == 0) {
//         int t1 = 0;
//         if (cont <= 2)
//             t1 = solve(n, c, idx + 1, cont + 1);
//         int t2 = solve(n, c, idx + 2, 1);
//         dp[idx] = c[idx] + t1 > t2 ? t1 : t2;
//     }
//     cout << dp[idx] << " ";
//     return dp[idx];
// }
void sol(int n, int *c) {
    dp[0] = c[0];
    if (n == 1)
        return;
    dp[1] = c[0] + c[1];
    if (n == 2)
        return;
    dp[2] = max(c[0] + c[2], c[1] + c[2]);
    for (int i = 3; i < n; i++) {
        dp[i] = max(dp[i - 3] + c[i - 1] + c[i], dp[i - 2] + c[i]);
        cout << dp[i] << " ";
    }
    cout << endl;
}
int main() {
    int n;
    cin >> n;
    int c[n];
    for (int i = 0; i < n; i++)
        cin >> c[i];
    // solve(n, c, 0, 0);
    sol(n, c);
    cout << dp[n - 1] << endl;
    return 0;
}