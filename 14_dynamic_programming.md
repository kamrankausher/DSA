# Chapter 14: Dynamic Programming & Greedy Algorithms 🚀

Have you ever done a long math calculation on a chalkboard, erased it, and then realized you needed that exact same result five minutes later? You probably groaned and did the whole calculation all over again.

If you had just written the result in a notebook, you could have looked it up in a second.

In programming, this "write it down in a notebook" trick is called **Dynamic Programming (DP)**. It is one of the most powerful optimization techniques in computer science, turning slow, exponential-time algorithms into lightning-fast, linear-time ones.

Today, we will demystify Dynamic Programming, compare it with **Greedy Algorithms**, and build solutions for classic optimization problems.

***

## 💡 Real-World Analogy: Remembering Calculations & Building Walls

To understand DP, think of two simple concepts:

### 1. The "Write it Down" Trick (Memoization / Top-Down)
Imagine I write this on a piece of paper:
* `1 + 1 + 1 + 1 + 1`
* I ask you: *"What does that equal?"*
* You count and say: *"5!"*
* Now, I write another `+ 1` at the end: `1 + 1 + 1 + 1 + 1 + 1`
* I ask you: *"What does it equal now?"*
* You instantly say: *"6!"*
* I ask: *"How did you know it was 6 so fast? Did you count from the beginning?"*
* You say: *"No, I remembered the previous part equalled 5, and I just added 1!"*
* **This is Memoization:** Storing the results of expensive calculations so you never have to recompute them!

### 2. Building a Brick Wall (Tabulation / Bottom-Up)
Imagine building a wall.
* You cannot place the top row of bricks in the air. You must place the foundation row (base cases) first.
* Once the foundation is laid, you lay the next row of bricks, supported by the row below it.
* **This is Tabulation:** Starting from the bottom (simplest subproblems) and building up a table of answers until you reach the top target!

***

## 📌 In Simple Terms: DP vs. Greedy

* **Dynamic Programming (DP):** An optimization method that solves a problem by breaking it down into **overlapping subproblems**, solving each subproblem exactly once, and storing their answers. DP is careful and guarantees the absolute best (optimal) result.
* **Greedy Algorithm:** An algorithm that makes the **locally optimal choice** at each step (e.g. "take the biggest coin available right now") in the hope of finding the global optimum. 
  * *The Catch:* Greedy is super fast, but it doesn't always find the best overall solution!
* **Overlapping Subproblems:** When an algorithm ends up calculating the exact same thing over and over.

***

## 🧠 Memory Model: The Fibonacci Call Tree

Let's look at the recursive tree for calculating `fibonacci(5)` naively. Notice how many times `F(2)` and `F(3)` are calculated independently:

```
                          F(5)
                       /        \
                    F(4)        F(3) ◄── [DUPLICATE]
                   /    \      /    \
                 F(3)   F(2)  F(2)  F(1)
                /   \   / \   / \
              F(2)  F(1) ... ... ...
               ▲
          [DUPLICATE]
```

By caching the result of `F(3)` the very first time we see it, we can prune the entire right side of the tree, turning an $O(2^N)$ tree into a straight $O(N)$ line!

***

## 🧠 Python Implementation: Optimizing Fibonacci

Let's write three versions of Fibonacci in Python to compare their speeds and memory usage: Naive (Recursive), Memoized (Top-Down DP), and Tabulated (Bottom-Up DP).

```python
class FibonacciOptimizer:
    def __init__(self):
        self.calls = 0

    def fib_naive(self, n):
        """Naive recursion: O(2^N) time. Recalculates everything."""
        self.calls += 1
        if n <= 1:
            return n
        return self.fib_naive(n - 1) + self.fib_naive(n - 2)

    def fib_memoized(self, n, memo=None):
        """Top-Down DP (Memoization): O(N) time, O(N) space."""
        self.calls += 1
        if memo is None:
            memo = {}
            
        # 1. Check if answer is already in our notebook
        if n in memo:
            return memo[n]
            
        # Base Cases
        if n <= 1:
            return n
            
        # 2. Compute and save in notebook
        memo[n] = self.fib_memoized(n - 1, memo) + self.fib_memoized(n - 2, memo)
        return memo[n]

    def fib_tabulated(self, n):
        """Bottom-Up DP (Tabulation): O(N) time, O(1) space optimized!"""
        if n <= 1:
            return n
            
        # Instead of storing a whole array, we only need to track the last two numbers!
        prev2 = 0 # F(0)
        prev1 = 1 # F(1)
        print(f"\n[TABULATION] Initial foundation: F(0)={prev2}, F(1)={prev1}")
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            print(f"  Calculating F({i}) = F({i-1}) + F({i-2}) -> {prev1} + {prev2} = {current}")
            
            # Shift variables forward
            prev2 = prev1
            prev1 = current
            
        return prev1


# --- Speed Test Comparison ---
opt = FibonacciOptimizer()

# 1. Naive Test
opt.calls = 0
res_naive = opt.fib_naive(10)
print(f"Naive result: {res_naive} | Total function calls made: {opt.calls}")

# 2. Memoized Test
opt.calls = 0
res_memo = opt.fib_memoized(10)
print(f"Memoized result: {res_memo} | Total function calls made: {opt.calls} (Massive reduction!)")

# 3. Tabulated Test
res_tab = opt.fib_tabulated(5)
```

***

## 🔍 The Tabulation Table (Trace Table)

Let's track how a Bottom-Up DP table of size `7` is filled step-by-step to compute `fibonacci(6)`:

* Formula: `DP[i] = DP[i-1] + DP[i-2]`

| Table Index ($i$) | DP[i-2] | DP[i-1] | Computed DP[i] | State of DP Table Array |
| :---: | :---: | :---: | :---: | :--- |
| **0** (Base) | - | - | 0 | `[0, _, _, _, _, _, _]` |
| **1** (Base) | - | - | 1 | `[0, 1, _, _, _, _, _]` |
| **2** | 0 | 1 | $0 + 1 = $ **1** | `[0, 1, 1, _, _, _, _]` |
| **3** | 1 | 1 | $1 + 1 = $ **2** | `[0, 1, 1, 2, _, _, _]` |
| **4** | 1 | 2 | $1 + 2 = $ **3** | `[0, 1, 1, 2, 3, _, _]` |
| **5** | 2 | 3 | $2 + 3 = $ **5** | `[0, 1, 1, 2, 3, 5, _]` |
| **6** | 3 | 5 | $3 + 5 = $ **8** | `[0, 1, 1, 2, 3, 5, 8]` |

***

## 📈 Complexity & Big O Analysis

| Method | Time Complexity | Space Complexity | Why? |
| :--- | :---: | :---: | :--- |
| **Naive Recursion** | $O(2^N)$ | $O(N)$ | Redundant calls multiply exponentially. Stack depth is $N$. |
| **Memoization (Top-down)** | $O(N)$ | $O(N)$ | Each subproblem is solved once. Dictionary uses $O(N)$ space. |
| **Tabulation (Bottom-up)** | $O(N)$ | $O(1)$ (optimized) | Iterative loop. Storing last two values uses constant space. |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 322: Coin Change (Medium)
> **Problem:** You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

#### Bottom-Up Tabulation Approach (O(Amount * Coins))
We create a DP table of size `amount + 1` where `dp[i]` represents the minimum coins needed to make amount `i`.
* Base Case: `dp[0] = 0` (0 coins to make 0 amount).
* For each amount `i` from 1 to `amount`, we try every coin: `dp[i] = min(dp[i], dp[i - coin] + 1)`.

```python
def coin_change(coins, amount):
    """
    Computes minimum coins to make amount using Bottom-Up DP.
    """
    print(f"=== Calculating Coin Change for amount: {amount} with coins {coins} ===")
    
    # Initialize DP table with infinity (representing unreachable amount)
    # We use amount + 1 as placeholder for infinity since we can't need more than that many coins
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0 # Base Case
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                # Minimum of current state or using this coin (+1 coin count)
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        print(f"  dp[{i}] = {dp[i] if dp[i] != amount + 1 else -1}")
        
    result = dp[amount] if dp[amount] != amount + 1 else -1
    print(f"🎉 Minimum coins needed for {amount}: {result}\n")
    return result

# Test
coin_change([1, 2, 5], 11)
```

***

## 🤖 Connection to Machine Learning & AI: Q-Learning & Bellman Equation

How does Dynamic Programming train AI agents to play chess or drive self-driving cars?
* **Reinforcement Learning (RL):** In RL, an AI agent interacts with an environment, performing actions to maximize its rewards (like a robot navigating a grid maze).
* **The Bellman Equation:** The core math of Q-Learning calculates the "Quality value" ($Q$) of being in a state $S$ and taking an action $A$.
  $$Q(s, a) = R(s, a) + \gamma \max_{a'} Q(s', a')$$
  * In plain English: *"The value of my current choice equals the immediate reward plus the value of the best possible choices I can make next."*
* **Why it's Dynamic Programming:** Notice that $Q(s, a)$ relies on the values of the next state $Q(s', a')$. 
  * The agent updates its Q-Table iteratively over thousands of episodes.
  * Instead of calculating all future paths from scratch (which is impossible), the algorithm reads the stored $Q$-values of future states directly from a lookup table (Tabulation).
  * This bottom-up tabular update process is what allows the agent to learn the optimal path through a maze, steering wheels on a road, or winning chess moves!
