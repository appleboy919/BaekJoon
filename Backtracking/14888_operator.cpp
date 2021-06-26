#include <iostream>

using namespace std;

int maxRes = -1000000000;
int minRes = 1000000000;
int calculate(int *nums, int *temp_opr, int num) {
    int ans = nums[0];
    for (int i = 1; i < num; i++) {
        switch (temp_opr[i - 1]) {
        case 0:
            ans += nums[i];
            break;
        case 1:
            ans -= nums[i];
            break;
        case 2:
            ans *= nums[i];
            break;
        case 3:
            ans /= nums[i];
        }
    }
    return ans;
}
void maxMinNum(int *nums, int num, int opr[4], int *temp_opr, int index) {
    if (index == num - 1) {
        int ans = calculate(nums, temp_opr, num);
        if (maxRes < ans)
            maxRes = ans;
        if (minRes > ans)
            minRes = ans;
        return;
    }
    for (int i = 0; i < 4; i++) {
        if (opr[i] != 0) {
            opr[i]--;
            temp_opr[index] = i;
            maxMinNum(nums, num, opr, temp_opr, index + 1);
            opr[i]++;
        }
    }
}
int main() {
    int n;
    cin >> n;
    int nums[n], operators[4], temp[n - 1];
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    for (int i = 0; i < 4; i++)
        cin >> operators[i];
    maxMinNum(nums, n, operators, temp, 0);
    cout << maxRes << endl << minRes << endl;
    return 0;
}