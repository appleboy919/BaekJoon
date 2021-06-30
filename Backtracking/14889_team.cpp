#include <iostream>
using namespace std;
int minVal = 10000;

int teamStat(int *team, int **s, int len) {
    int sum = 0;
    for (int i = 0; i < len; i++)
        for (int j = 0; j < len; j++)
            sum += s[team[i]][team[j]];

    return sum;
}

void minDiff(int n, int **s, int idx, int *temp, int idx2, int *temp2) {
    if (idx == n / 2) {
        if (idx2 != n / 2) {
            for (int i = temp[idx - 1] + 1; i < n; i++) {
                temp2[idx2] = i;
                idx2++;
            }
        }
        cout << "t1(" << idx << ")\n";
        for (int i = 0; i < idx; i++) {
            cout << temp[i] << " ";
        }
        cout << endl;
        cout << "t2(" << idx2 << ")\n";
        for (int i = 0; i < idx2; i++) {
            cout << temp2[i] << " ";
        }
        cout << endl;

        // int t2, idx2;
        // int temp2[idx];
        int t1, t2;
        t1 = teamStat(temp, s, idx);
        t2 = teamStat(temp2, s, idx2);
        cout << "t1: " << t1 << "!\n"
             << "t2: " << t2 << "!\n";
        cout << endl;
        int diff = abs(t1 - t2);
        if (minVal > diff)
            minVal = diff;
        return;
    }
    // int bt_idx2 = idx2;
    for (int i = idx; i <= n - idx; i++) {
        int new_idx2 = idx2;
        temp[idx] = i;
        // for (int j = idx; j < i; j++) {
        //     temp2[new_idx2] = j;
        //     new_idx2++;
        // }
        // for (int j = 0; j < idx; j++) {
        //     new_t1 += s[temp[j]][i];
        //     new_t1 += s[i][temp[j]];
        // }
        minDiff(n, s, idx + 1, temp, idx2, temp2);
        if (idx2 != n / 2) {
            temp2[idx2] = i;
            idx2++;
        }
    }
}
int main() {
    int n;
    cin >> n;
    int **s;
    s = new int *[n];
    for (int i = 0; i < n; i++) {
        s[i] = new int[n];
        for (int j = 0; j < n; j++) {
            cin >> s[i][j];
        }
    }
    int team1[n / 2], team2[n / 2];
    team1[0] = 0;

    minDiff(n, s, 1, team1, 0, team2);
    cout << minVal << endl;
    return 0;
}