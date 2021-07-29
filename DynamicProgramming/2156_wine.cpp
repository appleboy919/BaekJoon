#include <iostream>
using namespace std;
int dp[10001] = {0};
int max(int n1, int n2, int n3) {
    return n1 > n2 ? n1 > n3 ? n1 : n3 : n2 > n3 ? n2 : n3;
}
void sol(int n, int *c) {
    dp[0] = c[0];
    if (n == 1)
        return;
    dp[1] = c[0] + c[1];
    if (n == 2)
        return;
    for (int i = 2; i < n; i++) {
        dp[i] = max(dp[i - 3] + c[i - 1] + c[i], dp[i - 2] + c[i], dp[i - 1]);
    }
}

int main() {
    int n;
    cin >> n;
    int c[n];
    for (int i = 0; i < n; i++)
        cin >> c[i];
    sol(n, c);
    cout << dp[n - 1] << endl;
    return 0;
}