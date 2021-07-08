#include <iostream>
using namespace std;

void fib(int *x, int n) {
    if (n == 1 || n == 0) {
        x[n]++;
        return;
    }
    fib(x, n - 1);
    fib(x, n - 2);
}

int main() {

    int t;
    cin >> t;
    int n[t];
    for (int i = 0; i < t; i++)
        cin >> n[i];
    for (int i = 0; i < t; i++) {
        int oneTwo[2] = {0};
        fib(oneTwo, n[i]);
        cout << oneTwo[0] << " " << oneTwo[1] << endl;
    }
    return 0;
}
