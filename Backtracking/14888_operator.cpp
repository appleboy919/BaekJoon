#include <iostream>
using namespace std;

int calculate(int *nums, int *temp_opr, int num) {
    int ans = nums[0];
    for (int i = 1; i < num; i++) {
        switch (temp_opr[i - 1]) {
        case 0:
            ans += nums[i];
        case 1:
            ans -= nums[i];
        case 2:
            ans *= nums[i];
        case 3:
            ans /= nums[i];
        }
    }
    return ans;
}
void maxMinNum(int *nums, int num, int opr[4], int *temp_opr, int ans[2]) {
    // 1. calculate the numbers from the passed sequence
    int res = calculate(nums, temp_opr, num);

    // 2. get the next sequence of operators

    int idx = num - 2;
    int temp[4] = {0};
    while (idx >= 0) {
        temp[temp_opr[idx]]++;
        idx--;
        temp_opr[idx];
    }
    if (ans[0] < res)
        ans[0] = res;
    if (ans[1] > res)
        ans[1] = res;
    return;
}
int main() {
    int n;
    cin >> n;
    int nums[n], operators[4], temp[n - 1], ans[2];
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    for (int i = 0; i < 4; i++)
        cin >> operators[i];
    int idx = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < operators[i]; j++) {
            temp[idx] = i;
            idx++;
        }
    }
    int remainder[4] = {0};
    idx = n - 2;
    while (idx >= 0) {
        remainder[temp[idx]]++;
        }
    remainder[operators[n - 2]]++;
    maxMinNum(nums, n, remainder, temp, ans);

    /*
        for (int i = 0; i < n - 1; i++)
            cout << temp[i] << " ";
        cout << endl;
        */
    /*
    for (int i = 0; i < n; i++)
        cout << nums[i] << " ";
    cout << endl;
    for (int i = 0; i < 4; i++)
        cout << operators[i] << " ";
    cout << endl;
    */
    return 0;
}