#include <iostream>
#include <list>
using namespace std;
int n[21][21][21] = {0};

int w(int x1, int x2, int x3) {
    if (x1 <= 0 || x2 <= 0 || x3 <= 0)
        return 1;
    if (x1 > 20 || x2 > 20 || x3 > 20)
        return n[20][20][20];
    if (x1 < x2 && x2 < x3)
        return w(x1, x2, x3 - 1) + w(x1, x2 - 1, x3 - 1) - w(x1, x2 - 1, x3);
    return w(x1 - 1, x2, x3) + w(x1 - 1, x2 - 1, x3) + w(x1 - 1, x2, x3 - 1) -
           w(x1 - 1, x2 - 1, x3 - 1);
}

int main() {
    list<int *> nums;
    int *temp;
    int num = 0;
    while (true) {
        temp = new int[3];
        cin >> temp[0] >> temp[1] >> temp[2];
        nums.push_back(temp);
        num++;
        if (temp[0] == -1 && temp[1] == -1 && temp[2] == -1)
            break;
    }
    int ans;
    for (int i = 0; i < num; i++) {
        temp = nums.front();
        ans = w(temp[0], temp[1], temp[2]);
        cout << "w(" << temp[0] << ", " << temp[1] << ", " << temp[2]
             << ") = " << ans << endl;
        nums.pop_front();
    }
    return 0;
}