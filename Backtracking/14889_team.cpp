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
        int t1, t2;
        t1 = teamStat(temp, s, idx);
        t2 = teamStat(temp2, s, idx2);
        int diff = abs(t1 - t2);
        if (minVal > diff)
            minVal = diff;
        return;
    }
    for (int i = temp[idx - 1] + 1; i <= n / 2 + idx; i++) {
        int new_idx2 = idx2;
        temp[idx] = i;
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