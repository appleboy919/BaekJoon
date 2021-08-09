#include <iostream>
using namespace std;
int dp[1001] = {0};
int c[1001];
int n, ans;

void sol() {
    dp[1] = 1;
    ans = dp[1];
    if (n == 1)
        return;
    int t;
    for (int i = 2; i <= n; i++) {
        t = 0;
        for (int j = 1; j < i; j++) {
            if (c[j] < c[i]) {
                t = dp[j] + 1;
                dp[i] = t > dp[i] ? t : dp[i];
            }
        }
        if (dp[i] == 0)
            dp[i] = 1;
        ans = dp[i] > ans ? dp[i] : ans;
    }
}

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> c[i];
    sol();
    cout << ans << endl;
    return 0;
}