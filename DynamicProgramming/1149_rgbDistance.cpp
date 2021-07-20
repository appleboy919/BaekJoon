#include <iostream>
using namespace std;
int **c;
int **t;
int paint(int n, int color, int idx) {
    if (idx == n)
        return 0;
    if (t[idx][color] == 0) {
        int temp;
        int ret = -1;
        for (int i = 0; i < 3; i++) {
            if (idx != 0 && i == color)
                continue;
            temp = paint(n, i, idx + 1) + c[idx][i];
            if (ret == -1)
                ret = temp;
            else
                ret = ret > temp ? temp : ret;
        }
        t[idx][color] = ret;
    }
    return t[idx][color];
}

int main() {
    int n;
    cin >> n;
    int ans;
    c = new int *[n];
    t = new int *[n];
    for (int i = 0; i < n; i++) {
        c[i] = new int[3];
        t[i] = new int[3];
    }
    for (int i = 0; i < n; i++)
        cin >> c[i][0] >> c[i][1] >> c[i][2];
    for (int i = 0; i < 3; i++)
        ans = paint(n, 0, 0);
    cout << ans << endl;
    for (int i = 0; i < n; i++) {
        delete[] c[i];
        delete[] t[i];
    }
    delete[] c;
    delete[] t;
    return 0;
}
