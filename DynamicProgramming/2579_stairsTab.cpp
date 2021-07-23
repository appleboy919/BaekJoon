#include <iostream>
using namespace std;

void goUp(int n, int *c, int *dp) {
    dp[0] = c[0];
    dp[1] = c[0] + c[1];
    dp[2] = max(c[0] + c[2], c[1] + c[2]);
    for (int i = 3; i < n; i++)
        dp[i] = max(dp[i - 2] + c[i], dp[i - 3] + c[i - 1] + c[i]);
}
int main() {
    int n;
    cin >> n;
    int c[n];
    int dp[n];
    for (int i = 0; i < n; i++)
        cin >> c[i];
    goUp(n, c, dp);
    cout << dp[n - 1] << endl;
    return 0;
}