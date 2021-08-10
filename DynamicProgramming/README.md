# Dynamic Programming

- solve an optimization problem by breaking down into simpler subproblems
- subproblems **overlaps**
- ex) fibonacci numbers: _fib(n) = fib(n-1) + fib(n-2)_

  ```
  fib(4)  -   fib(3)  -   fib(2)  -   fib(1)
                                  -   fib(0)
                      -   fib(1)

          -   fib(2)  -   fib(1)
                      -   fib(0)
  ```

  - Memoization vs Tabulation

    1. **Top-down Memoization**

       - chache each subproblem result --> no need to solve each problem repeatedly
       - "Top-down": recurses down to solve subproblems

         ```c++
         // going up stairs with 1 or 2 steps

         #include <iostream>
         using namespace std;
         int *c;
         long int **dp;

         // recursively solve down to subproblems
         long int goUp(int n, int f, int prvStep) {
            if (f > n)
               return -1000 * n;
            if (f == n)
               return c[n - 1];
            if (dp[f - 1][prvStep - 1] == 0) {
               long int t1 = -1;
               long int t2;
               if (prvStep != 1 || f == 1)
                     t1 = goUp(n, f + 1, 1) + c[f - 1];
               t2 = goUp(n, f + 2, 2) + c[f - 1];
               dp[f - 1][prvStep - 1] = t1 > t2 ? t1 : t2;
            }
            return dp[f - 1][prvStep - 1];
         }
         int main() {
            int n;
            cin >> n;
            c = new int[n];
            dp = new long int *[n];
            for (int i = 0; i < n; i++) {
               dp[i] = new long int[2];
               cin >> c[i];
            }
            long int t1 = goUp(n, 1, 1);
            long int t2 = 0;
            if (n >= 2)
               t2 = goUp(n, 2, 2);
            long int ans = t1 > t2 ? t1 : t2;
            cout << ans << endl;

            for (int i = 0; i < n; i++)
               delete[] dp[i];
            delete[] dp;
            delete[] c;
            return 0;
         }
         ```

    2. **Bottom-up Tabulation**

       - solve each problem, filling up n-dimensional table

       ```c++
         #include <iostream>
         using namespace std;

         void goUp(int n, int *c, int *dp) {
            dp[0] = c[0];
            dp[1] = c[0] + c[1];
            dp[2] = max(c[0] + c[2], c[1] + c[2]);
            for (int i = 3; i < n; i++)
               dp[i] = max(dp[i - 2] + c[i], dp[i - 3] + c[i - 1] + c[i]);
         }
         int main() {
            int n;
            cin >> n;
            int c[n];
            int dp[n];
            for (int i = 0; i < n; i++)
               cin >> c[i];
            goUp(n, c, dp);
            cout << dp[n - 1] << endl;
            return 0;
         }
       ```

  ### Problem Note

  - Re: 11053 LIS (in Python)
