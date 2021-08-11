#include <iostream>
using namespace std;
int dp[1001] = {0};
int c[1001];
int n, ans;
void solve() {
    dp[1] = 1;
    int t;
    for (int i = 2; i <= n; i++) {
        t = 0;
        for (int j = 1; j < i; j++) {
            // 2 for loop?
        }
    }
}
int main() {
    ans = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> c[i];
    return 0;
}