#include <iostream>
using namespace std;
int max_len = -1;
int dp[1001] = {0};
int solve(int n, int *c, int idx) {
    if (idx == n)
        return 1;
    if (dp[idx] == 0) {
        int temp = solve(n, c, idx + 1);
        if (c[idx] < c[idx + 1] && c[idx] < c[0]) {
            temp += 1;
            c[0] = c[idx];
        }
        dp[idx] = temp;
    }
    return dp[idx];
}

int main() {
    int n;
    cin >> n;
    int c[n + 1];
    c[0] = 1001;
    for (int i = 1; i < n + 1; i++)
        cin >> c[i];
    for (int i = 0; i < n + 1; i++)
        cout << c[i] << " ";
    cout << endl;
    cout << solve(n, c, 1) << endl;
    return 0;
}