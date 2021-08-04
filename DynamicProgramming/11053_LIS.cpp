#include <iostream>
using namespace std;
int max_len = -1;
int minNum = 1001;
int maxNum = 0;
int dp[1001] = {0};
int c[1001];
int n;
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

int sol(int n, int idx) {
    if (idx == n) {
        maxNum = c[idx];
        cout << idx << ": 1!\n";
        return 1;
    }
    int t = sol(n, idx + 1);
    if (c[idx] < minNum) {
        cout << "minNum changed! " << minNum;
        minNum = c[idx];
        cout << " -> " << minNum << endl;
        cout << idx << ": " << t + 1 << endl;
        dp[c[idx]] = t + 1;
        return t + 1;
    }
    cout << idx << ": " << t << endl;
    dp[c[idx]] = t;
    return t;

    // if (prvNum < c[idx])
    //     return sol(n, c, idx + 1, minIdx, c[idx]) + 1;
    // int t1 = 0;
    // if (prvNum > c[idx])
    //     int t1 = sol(n, c, idx + 1, idx, c[idx]);
    // int t2 = sol(n, c, idx + 2, minIdx, c[idx]);
    // return t1 > t2 ? t1 : t2;
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
int lis(int idx) {
    if (idx == n) {
        cout << c[idx] << ": 1!" << endl;
        dp[c[idx]] = 1;
        return 1;
    }
    if (dp[c[idx]] == 0)
        dp[c[idx]] = tempLIS(idx);

    int t = lis(idx + 1);
    cout << idx << ": ";
    if (c[idx] < c[idx + 1])
        dp[c[idx]] =
            dp[c[idx]] > dp[c[idx + 1]] ? dp[c[idx]] : dp[c[idx + 1]] + 1;
    cout << dp[c[idx]] << " / " << t << endl;
    return dp[c[idx]] > t ? dp[c[idx]] : t;
}
int main() {
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> c[i];
    // cout << sol(n, 1) << endl;
    cout << lis(1) << endl;
    return 0;
}
/*
2 3 1 4 3 6
1 2 3 4 3 5

1 2 1 3 2 5

3 5 2 3 4 5

2 3 2 4 5

2 3 4 5 1 6

2 1 2 3 4 5
2 1 3 2 5 6
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