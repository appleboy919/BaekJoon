#include <iostream>
using namespace std;
long int dp[101] = {0};
long int padovan(int n) {
    if (n <= 0)
        return 0;
    if (n == 1 || n == 2)
        return 1;
    if (dp[n] == 0)
        dp[n] = padovan(n - 3) + padovan(n - 2);
    return dp[n];
}

int main() {
    int t;
    cin >> t;
    int cases[t];
    for (int i = 0; i < t; i++)
        cin >> cases[i];
    for (int i = 0; i < t; i++)
        cout << padovan(cases[i]) << endl;

    return 0;
}