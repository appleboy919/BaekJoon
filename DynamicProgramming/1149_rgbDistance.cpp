#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int val[n][3];
    for (int i = 0; i < n; i++)
        cin >> val[i][0] >> val[i][1] >> val[i][2];
    for (int i = 0; i < n; i++)
        cout << val[i][0] << " " << val[i][1] << " " << val[i][2] << endl;

    return 0;
}
