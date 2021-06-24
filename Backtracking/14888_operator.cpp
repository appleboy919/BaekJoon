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
        }
    }
}
int *minMaxNum(int *nums, int num, int opr[4], int *temp_opr, int *opr_rmd,
               int ans[2]) {
    if (nums)
        return nums return
}
int main() {
    int n;
    cin >> n;
    int nums[n], operators[4], temp[n - 1];
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    for (int i = 0; i < 4; i++)
        cin >> operators[i];
    int idx = 0;
    for (int i = 0; i < OPR_NUM; i++) {
        for (int j = 0; j < operators[i]; j++) {
            temp[idx] = i;
            idx++;
        }
    }
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