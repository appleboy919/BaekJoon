#include <iostream>
using namespace std;

int tile(int n, int dp[]) {
    if (n / 2 == 0)
        return 1;
    // use '1'
    if (dp[n - 1] == 0)
        dp[n - 1] = tile(n - 1, dp);
    // use '00'
    if (dp[n - 2] == 0)
        dp[n - 2] = tile(n - 2, dp);
    dp[n] = (dp[n - 1] + dp[n - 2])%15746;
    return dp[n];
}

int main() {
    int n;
    cin >> n;
    int *dp = new int[n + 1];
    int ans = tile(n, dp);
    cout << ans << endl;
    delete[] dp;
    return 0;
}