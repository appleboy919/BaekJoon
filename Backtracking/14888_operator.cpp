#include <iostream>
#define OPR_NUM 4
using namespace std;

int *minMaxNum(int nums) {}
int main() {
    int n;
    cin >> n;
    int nums[n], operators[OPR_NUM];
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    for (int i = 0; i < OPR_NUM; i++)
        cin >> operators[i];
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