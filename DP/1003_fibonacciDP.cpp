#include <iostream>
using namespace std;
int nums[41][2] = {0};

void fib(int n) {
    int idx;
    for (int i = n; i >= 0; i--) {
        if (nums[i][0] != 0 || nums[i][1] != 0) {
            idx = i;
            break;
        }
    }
    for (int i = idx + 1; i <= n; i++) {
        nums[i][0] = nums[i - 1][0] + nums[i - 2][0];
        nums[i][1] = nums[i - 1][1] + nums[i - 2][1];
    }
}

int main() {
    nums[0][0] = 1;
    nums[1][1] = 1;
    int t;
    cin >> t;
    int n[t];
    for (int i = 0; i < t; i++)
        cin >> n[i];
    for (int i = 0; i < t; i++) {
        if (n[i] != 0 && n[i] != 1 && nums[n[i]][0] == 0)
            fib(n[i]);
        cout << nums[n[i]][0] << " " << nums[n[i]][1] << endl;
    }

    return 0;
}
