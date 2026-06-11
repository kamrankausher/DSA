# Chapter 02: Recursion & the Call Stack 🚀

Have you ever stood between two parallel mirrors and seen an infinite corridor of yourself shrinking into the distance? Or opened a Russian nesting doll, only to find a smaller doll, and a smaller one inside it?

That is the essence of **Recursion**. In this chapter, we will demystify this powerful concept, understand how the computer tracks active functions in its brain (the Call Stack), and learn how to write recursive code without crashing the computer!

***

## 💡 Real-World Analogy: The Russian Nesting Dolls

Imagine you are handed a giant wooden Russian nesting doll. You are told there is a **piece of candy** hidden inside the smallest doll. How do you find it?

1. **The Step:** You open the outer doll.
2. **The Question:** Is there candy inside?
   * *Case A:* Yes, there's candy! You eat it and stop. (This is the **Base Case**).
   * *Case B:* No candy, just a smaller doll. You repeat the process and open that doll. (This is the **Recursive Case**).
3. **The Cleanup:** Once you eat the candy, you have to pack all the dolls back together, closing them one-by-one from smallest to largest.

If you forget to include a "smallest doll" with the candy, you would keep opening dolls forever. In computer science, this is called **Infinite Recursion**, which causes a **Stack Overflow** crash!

***

## 📌 In Simple Terms: What is Recursion?

* **Recursion:** A programming technique where a function calls **itself** to solve a smaller version of the same problem.
* **Base Case:** The condition under which the function *stops* calling itself and starts returning values. **Every recursive function must have at least one base case!**
* **Recursive Case:** The condition where the function calls itself with a modified, simpler input.
* **The Call Stack:** A special section of the computer's memory (arranged like a stack of plates) that remembers where each active function was paused so it can return there when sub-functions finish.

***

## 🧠 Memory Model: The Call Stack in Action

When your program calls a function, the computer creates a **Stack Frame** (a memory box) containing the function's variables and parameters, and places it on top of the Call Stack.

Let's look at what the Call Stack looks like when calculating the Factorial of 3 ($3! = 3 \times 2 \times 1 = 6$):

```
       CALL STACK DURING EXECUTION (LIFO: Last In, First Out)

   Step 1: factorial(3)      Step 2: factorial(2)      Step 3: factorial(1)
   ┌───────────────────┐     ┌───────────────────┐     ┌───────────────────┐
   │                   │     │                   │     │  factorial(1)     │
   ├───────────────────┤     ├───────────────────┤     ├───────────────────┤
   │                   │     │  factorial(2)     │     │  factorial(2)     │
   ├───────────────────┤     ├───────────────────┤     ├───────────────────┤
   │  factorial(3)     │     │  factorial(3)     │     │  factorial(3)     │
   └───────────────────┴─────┴───────────────────┴─────┴───────────────────┘
     Active: fact(3)           Active: fact(2)           Active: fact(1) (Base!)
     Wait: for fact(2)         Wait: for fact(1)         Returns: 1
```

Once `factorial(1)` returns `1`, the frames pop off one-by-one, passing their results down:
* `factorial(1)` returns `1` -> popped.
* `factorial(2)` computes $2 \times 1 = 2$ and returns `2` -> popped.
* `factorial(3)` computes $3 \times 2 = 6$ and returns `6` -> popped.
* Stack is empty!

***

## 🧠 Python Implementation with Indented Tracing Logs

Let's write a recursive implementation of **Factorial** and **Fibonacci** in Python. We will add an `indent` parameter to our debug prints so you can visually watch the call stack grow and shrink in your terminal!

### 1. Factorial ($N!$) with Visual Stack Tracing

```python
def factorial_trace(n, depth=0):
    """
    Computes n! recursively and prints a visual model of the call stack.
    """
    indent = "  " * depth  # Indentation matches the call stack depth
    print(f"{indent}▶️ [CALL] factorial_trace(n={n})")
    
    # 1. Base Case: n is 1 or 0
    if n <= 1:
        print(f"{indent}🎉 [BASE CASE REACHED] Returning 1")
        return 1
        
    # 2. Recursive Case: n * factorial(n - 1)
    print(f"{indent}⏳ [PAUSED] fact({n}) needs fact({n-1}). Calling fact({n-1})...")
    sub_result = factorial_trace(n - 1, depth + 1)
    
    result = n * sub_result
    print(f"{indent}🔄 [RESUMED] fact({n}) got result {sub_result}. Computing {n} * {sub_result} = {result}")
    print(f"{indent}◀️ [RETURN] factorial_trace(n={n}) returning {result}")
    return result

# Run the tracing factorial!
print("--- STARTING FACTORIAL TRACE ---")
factorial_trace(4)
```

---

### 2. Fibonacci Sequence with Branching Visual Tracing

The Fibonacci sequence starts `0, 1, 1, 2, 3, 5, 8...` where each number is the sum of the two preceding ones: $F(n) = F(n-1) + F(n-2)$.

```python
def fibonacci_trace(n, depth=0, branch=""):
    """
    Computes the nth Fibonacci number recursively and visualizes the tree branching.
    """
    indent = "  " * depth
    print(f"{indent}▶️ [CALL] {branch} fibonacci_trace(n={n})")
    
    # Base Cases
    if n == 0:
        print(f"{indent}🎉 [BASE CASE] F(0) = 0")
        return 0
    if n == 1:
        print(f"{indent}🎉 [BASE CASE] F(1) = 1")
        return 1
        
    # Recursive Case: F(n) = F(n-1) + F(n-2)
    print(f"{indent}⏳ [PAUSED] F({n}) needs F({n-1}) and F({n-2})")
    
    left_val = fibonacci_trace(n - 1, depth + 1, "Left:")
    right_val = fibonacci_trace(n - 2, depth + 1, "Right:")
    
    result = left_val + right_val
    print(f"{indent}🔄 [RESUMED] F({n}) = {left_val} + {right_val} = {result}")
    print(f"{indent}◀️ [RETURN] Returning F({n}) = {result}")
    return result

print("\n--- STARTING FIBONACCI TRACE ---")
fibonacci_trace(3)
```

***

## 🔍 Step-by-Step Call Tree for `fibonacci(3)`

Unlike Factorial which has a straight chain of calls, Fibonacci splits into a **Tree** because each step spawns two new calls:

```
                  F(3) [Needs F(2) + F(1)]
                 /    \
      F(2) [Needs F(1)+F(0)]  F(1) [Returns 1]
           /      \
    F(1)[Ret 1]  F(0)[Ret 0]
```

### Trace Table of Stack Frames
Below is the timeline of how frames are pushed and popped from memory to calculate `fibonacci(3)`:

| Time Step | Action | Call Stack (Bottom to Top) | Active Frame | Return Value |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Call `F(3)` | `[F(3)]` | `F(3)` | - |
| 2 | Call `F(2)` | `[F(3), F(2)]` | `F(2)` | - |
| 3 | Call `F(1)` (Left) | `[F(3), F(2), F(1)]` | `F(1)` | **1** (Base Case) |
| 4 | Pop `F(1)` | `[F(3), F(2)]` | `F(2)` (Resumed) | - |
| 5 | Call `F(0)` (Right)| `[F(3), F(2), F(0)]` | `F(0)` | **0** (Base Case) |
| 6 | Pop `F(0)` | `[F(3), F(2)]` | `F(2)` (Resumed) | $1 + 0 =$ **1** |
| 7 | Pop `F(2)` | `[F(3)]` | `F(3)` (Resumed) | - |
| 8 | Call `F(1)` (Right)| `[F(3), F(1)]` | `F(1)` | **1** (Base Case) |
| 9 | Pop `F(1)` | `[F(3)]` | `F(3)` (Resumed) | $1 + 1 =$ **2** |
| 10 | Pop `F(3)` | `[]` (Empty) | None | **2** (Final Result)|

***

## 📈 Complexity & Big O Analysis

| Algorithm | Time Complexity | Space Complexity | Why? |
| :--- | :---: | :---: | :--- |
| **Factorial** | $O(N)$ | $O(N)$ | $N$ total calls are made. Max call stack depth is $N$ frames. |
| **Fibonacci (Naive)** | $O(2^N)$ | $O(N)$ | Every call splits into 2 more calls (exponential growth). Max stack depth is $N$ frames. |
| **Fibonacci (Memoized)**| $O(N)$ | $O(N)$ | Storing results avoids recalculations, making it linear. |

* **Important Note on Space Complexity:** Even if a recursive function does not define any lists or variables, it still uses $O(D)$ memory space, where $D$ is the maximum depth of the call stack, because the computer must store those return frames!

***

## 🎓 Interview & LeetCode Applications

### LeetCode 344: Reverse String (Easy)
> **Problem:** Write a recursive function that reverses a string (passed as a list of characters) in-place.

#### Recursive Two-Pointer Walkthrough
We swap the first and last characters, then recursively solve the smaller string inside them.

```python
def reverse_string_recursive(s, left=0, right=None):
    """
    Reverses a list of characters in-place using recursion.
    """
    if right is None:
        right = len(s) - 1
        print(f"=== Reversing string: {''.join(s)} ===")

    # Base Case: Pointers met or crossed
    if left >= right:
        print(f"  Pointers met (left={left}, right={right}). Stopping.")
        return

    # Swap the outer characters
    print(f"  Swap indices {left} and {right}: '{s[left]}' <-> '{s[right]}'")
    s[left], s[right] = s[right], s[left]
    print(f"    Current state: {''.join(s)}")

    # Recursive Case: Shrink the window and swap inner elements
    reverse_string_recursive(s, left + 1, right - 1)

# Test it
char_list = list("hello")
reverse_string_recursive(char_list)
```

---

### LeetCode 70: Climbing Stairs (Easy/Medium)
> **Problem:** You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#### The Recursive Memoization Approach (Top-Down DP)
If you are on step `n`, you could have reached it from either `n-1` (by taking 1 step) or `n-2` (by taking 2 steps). This means: $\text{ways}(n) = \text{ways}(n-1) + \text{ways}(n-2)$. We use a dictionary (memo) to avoid recalculating overlapping subproblems.

```python
def climb_stairs(n, memo=None):
    """
    Computes ways to reach step n using recursion + memoization.
    """
    if memo is None:
        memo = {}
        print(f"=== Calculating Climb Stairs for n={n} ===")
        
    # Check if we already calculated ways(n)
    if n in memo:
        print(f"  [MEMO HIT] Already know ways({n}) = {memo[n]}")
        return memo[n]
        
    # Base Cases
    if n == 1: return 1  # Only 1 way (1)
    if n == 2: return 2  # 2 ways (1+1, 2)
    
    # Recursive calculation
    print(f"  [CALCULATING] ways({n}) = ways({n-1}) + ways({n-2})")
    result = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    
    # Save in memo
    memo[n] = result
    print(f"  [MEMO SAVE] Saved ways({n}) = {result}")
    return result

# Test it
climb_stairs(5)
```

***

## 🤖 Connection to Machine Learning & AI: Decision Tree Splitting

Where is recursion used in Artificial Intelligence?
* **Decision Trees (e.g., Random Forests, XGBoost):** Decision trees are used for making classifications (like predicting if a customer will buy a product based on their age and income).
* **Recursive Splitting:** To train a Decision Tree, the algorithm starts at the root node (all data) and looks for the best question to split the data (e.g., "Is age > 30?").
* It splits the dataset into a Left child and a Right child, and then **recursively calls the split function** on both children!
* **The Base Case:** Recursion stops when a leaf node is reached (e.g., all data points in that branch have the same label, or the tree hits a configured `max_depth` limit).
* Without recursion, building complex decision trees would require complicated, hard-to-maintain nested loop architectures.
