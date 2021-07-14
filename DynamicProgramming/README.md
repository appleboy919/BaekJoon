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
    2. **Bottom-up Tabulation**:
       solve each problem, filling up n-dimensional table
