#include <iostream>
using namespace std;
int dp[1001] = {0};
int c[1001];
int n, ans;
void solve() {
    int t = 0;
    bool up;
    for (int i = 2; i <= n; i++) {
        // how to handle bool??
        if (c[i] == c[i - 1])
            continue;
        if (up) {
            if (c[i - 1] > c[i])
                up = false;
            dp[i] = dp[i - 1] + 1;
        } else {
            if (c[i - 1] < c[i]) {
                up = true;
                dp[i] = 2;
            } else
                dp[i] = dp[i - 1] + 1;
        }
        t = dp[i] > t ? dp[i] : t;
    }
    ans = t;
}
int main() {
    fill_n(dp, 1001, 1);
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> c[i];
    for (int i = 1; i <= n; i++)
        cout << dp[i] << endl;
    cout << endl;
    cout << ans << endl;
    return 0;
}
