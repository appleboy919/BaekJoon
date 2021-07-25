#include <iostream>
using namespace std;
#define MAX 2147483647
int getMin(int a[3]) {
    int min = a[0];
    for (int i = 1; i < 3; i++)
        min = min > a[i] ? a[i] : min;
    return min;
}
int solution(int x, int *dp) {
    if (x == 1)
        return 0;
    if (dp[x] == 0) {
        int t[3];
        fill_n(t, 3, MAX);
        if (x % 3 == 0)
            t[0] = solution(x / 3, dp) + 1;
        if (x % 2 == 0)
            t[1] = solution(x / 2, dp) + 1;
        t[2] = solution(x - 1, dp) + 1;
        dp[x] = getMin(t);
    }
    return dp[x];
}
int main() {
    int n;
    cin >> n;
    int dp[n + 1];
    fill_n(dp, n + 1, 0);
    cout << solution(n, dp) << endl;
    return 0;
}