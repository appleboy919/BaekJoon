#include <iostream>
using namespace std;
int minVal;
void paint(int n, int **c, int idx) {

}

int main() {
    int n;
    cin >> n;
    minVal = 1000*n;
    int c[n][3];
    for (int i = 0; i < n; i++)
        cin >> c[i][0] >> c[i][1] >> c[i][2];
    for (int i = 0; i < n; i++)
        cout << c[i][0] << " " << c[i][1] << " " << c[i][2] << endl;

    return 0;
}
