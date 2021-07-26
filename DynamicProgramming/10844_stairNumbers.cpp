#include <iostream>
using namespace std;
long int dp[101];
void solve(int n) {
    dp[0] = 0;
    dp[1] = 9;
    for (int i = 2; i <= n; i++)
        dp[i] = dp[i - 1] * 2 - 1;
}
int main() {
    int n;
    cin >> n;
    solve(n);
    cout << dp[n] % 1000000000 << endl;
    return 0;
}