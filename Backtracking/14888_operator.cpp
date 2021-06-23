#include <iostream>
#define OPR_NUM 4
using namespace std;

int *minMaxNum(int *nums, int num, int opr[OPR_NUM], int *temp) { return }
int main() {
    int n;
    cin >> n;
    int nums[n], operators[OPR_NUM], temp[n - 1];
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    for (int i = 0; i < OPR_NUM; i++)
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