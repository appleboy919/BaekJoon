#include <iostream>

static int ans;

bool check_pos(int *cols, int row, int col) {
    int init_row = row;
    while (row > 0) {
        row -= 1;
        if (abs(init_row - row) == abs(cols[row] - col)) {
            return false;
        }
    }
    return true;
}
void n_queen(int n, int *cols, int row, int *emp_cols, int emp_num) {
    for (int i = 0; i < emp_num; i++) {
        if (check_pos(cols, row, emp_cols[i])) {
            if (row == n - 1) {
                ans += 1;
            } else {
                cols[row] = emp_cols[i];
                int temp_cols[n];
                std::copy(cols, cols + n, temp_cols);
                int temp_emp[emp_num - 1];
                int idx = 0;
                for (int j = 0; j < emp_num; j++) {
                    if (j == i)
                        continue;
                    temp_emp[idx] = emp_cols[j];
                    idx += 1;
                }
                n_queen(n, temp_cols, row + 1, temp_emp, idx);
            }
        }
    }
    return;
}

int main(void) {
    int n;
    std::cin >> n;
    int init_cols[n], init_emp[n];
    for (int i = 0; i < n; i++) {
        init_cols[i] = -1;
        init_emp[i] = i;
    }
    n_queen(n, init_cols, 0, init_emp, n);
    std::cout << ans << std::endl;
}
