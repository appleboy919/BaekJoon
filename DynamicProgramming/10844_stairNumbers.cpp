#include <iostream>
using namespace std;
long int dp[101][11];
long int solve(int l, int num) {
    if (dp[l][num] == 0) {
        long int t = 0;
        if (num > 0)
            t += solve(l - 1, num - 1);
        if (num < 9)
            t += solve(l - 1, num + 1);
        dp[l][num] = t % 1000000000;
    }
    return dp[l][num];
}
int main() {
    int n;
    fill_n(&dp[0][0], 101 * 11, 0);
    for (int i = 0; i < 11; i++)
        dp[1][i] = 1;
    cin >> n;
    long int ans = 0;
    for (int i = 1; i < 10; i++)
        ans += solve(n, i);
    cout << ans % 1000000000 << endl;
    return 0;
}