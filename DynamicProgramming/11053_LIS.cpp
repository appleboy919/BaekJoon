#include <iostream>
using namespace std;
int dp[1001] = {0};
int c[1001];
int n, ans;
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

int tempLIS(int idx) {
    int t = c[idx];
    int size = 1;
    for (int i = idx + 1; i <= n; i++) {
        if (t < c[i]) {
            t = c[i];
            size++;
        }
    }
    return size;
}
int nextLIS(int idx) {
    for (int i = idx + 1; i <= n; i++) {
        if (c[idx] < c[i])
            return dp[c[i]];
    }
    return 0;
}
void lis(int idx) {
    if (idx == n) {
        cout << idx << ": 1!" << endl;
        dp[c[idx]] = 1;
        ans = 1;
        return;
    }
    lis(idx + 1);
    int t = nextLIS(idx);
    dp[c[idx]] = t == 0 ? (dp[c[idx]] == 0 ? 1 : dp[c[idx]]) : t + 1;
    if (dp[c[idx]] > ans)
        ans = dp[c[idx]];
    // int t = lis(idx + 1);
    // if (dp[c[idx]] == 0)
    //     dp[c[idx]] = tempLIS(idx);
    cout << idx << ": ";
    // if (c[idx] < c[idx + 1])
    //     dp[c[idx]] =
    //         dp[c[idx]] > dp[c[idx + 1]] ? dp[c[idx]] : dp[c[idx + 1]] + 1;
    cout << dp[c[idx]] << " / " << t << endl;
    // return dp[c[idx]] > t ? dp[c[idx]] : t;
}
int main() {
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> c[i];
    // cout << sol(n, 1) << endl;
    lis(1);
    cout << ans << endl;
    return 0;
}
/*
1 2 1 3 2 5
3 5 1 2 3 4
1 3 5 2 3 4
*/

// void lis(int n, int idx) {
//     dp[1] = 1;
//     if (n == 1)
//         return;
//     if (c[1] < c[2]) {
//         dp[2] = 2;
//         minNum = c[1];
//         maxNum = c[2];
//     } else {
//         dp[2] = 1;
//         minNum = maxNum = c[2];
//     }
//     for (int i = 3; i <= n; i++) {
//         if (c[i - 1] < c[i]) {
//             if(maxNum < c[i]) {
//                 maxNum = c[i];
//                 dp[i] = dp[i-1] + 1;
//             }
//         } else {
//             if (c[i] < minNum) {
//                 minNum =
//             }
//         }
//     }
// }