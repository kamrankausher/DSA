# Chapter 09: Searching & Binary Search 🚀

Imagine you want to look up a word in a physical 1,000-page English dictionary. You would never open page 1 and read every word one-by-one until you find it. That would take all day!

Instead, you open to the middle, check the letter, throw away half the book, and repeat the process on the remaining half. In computer science, this is **Binary Search**—one of the most elegant, powerful algorithms ever designed.

Today, we will learn how binary search works, compare it with Linear Search, write iterative and recursive versions, and see how it speeds up search queries on massive datasets.

***

## 💡 Real-World Analogy: The Guessing Game (Higher / Lower)

Imagine a friend asks you to guess a secret number they chose between **1 and 100**.
* **Linear Search (Naive):** You guess: *"Is it 1?"*, *"Is it 2?"*, *"Is it 3?"*... 
  * If the number is 99, it takes you **99 guesses**!
* **Binary Search (Smart):** You guess: *"Is it 50?"*
  * Friend says: *"No, my number is higher."*
  * **What you do:** You discard all numbers from 1 to 50! Now your search window is **51 to 100**.
  * You split it again: *"Is it 75?"*
  * Friend says: *"No, my number is lower."*
  * **What you do:** You discard numbers 75 to 100! Your new window is **51 to 74**.
  * You find the number in at most **7 guesses**!

***

## 📌 In Simple Terms: The Sorted Condition

* **Sorted Constraint:** Binary Search **ONLY** works on lists that are already sorted! If the data is scrambled, you cannot discard halves safely, and you must use Linear Search.
* **Divide & Conquer:** Split the search space in half at each step.
* **Logarithmic Time $O(\log N)$:** An efficiency level where doubling the data size only adds **1 single step** to the execution time!

***

## 🧠 Memory Model: Moving Boundaries

In Binary Search, we do not edit the array in memory. Instead, we use two pointers (`left` and `right`) to represent our active search window.

Let's search for target `11` in array `[2, 5, 8, 11, 15, 20]`:

```
  Step 1: Check mid = (0 + 5) // 2 = 2
  [ 2 | 5 | 8 | 11 | 15 | 20 ]
    ▲       ▲             ▲
    │       │             │
  left     mid          right
  
  arr[mid] (8) < Target (11). Shift left to mid + 1 (3):
  
  Step 2: Check mid = (3 + 5) // 2 = 4
  [ 2 | 5 | 8 | 11 | 15 | 20 ]
                ▲    ▲    ▲
                │    │    │
              left  mid right
              
  arr[mid] (15) > Target (11). Shift right to mid - 1 (3):
  
  Step 3: Check mid = (3 + 3) // 2 = 3
  [ 2 | 5 | 8 | 11 | 15 | 20 ]
                ▲
             left, mid, right
             
  arr[mid] (11) == Target (11). Match Found! Return index 3.
```

***

## 🧠 Python Implementation: Iterative & Recursive

Let's implement both iterative and recursive Binary Search in Python, printing detailed window logs.

### 1. Iterative Binary Search (Constant Space O(1))

```python
def binary_search_iterative(arr, target):
    """
    Finds index of target in sorted arr iteratively. Time: O(log N), Space: O(1).
    """
    print(f"=== Starting Iterative Binary Search for target: {target} ===")
    left = 0
    right = len(arr) - 1
    steps = 0
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        mid_val = arr[mid]
        
        print(f"Step {steps}: Search Window indices [{left} to {right}]")
        print(f"  Middle index checked: {mid} (Value: {mid_val})")
        
        if mid_val == target:
            print(f"  🎉 Found target '{target}' at index {mid} in {steps} steps!\n")
            return mid
        elif mid_val < target:
            print(f"    Target ({target}) > Middle ({mid_val}). Discarding Left Half.")
            left = mid + 1  # Shift left boundary
        else:
            print(f"    Target ({target}) < Middle ({mid_val}). Discarding Right Half.")
            right = mid - 1 # Shift right boundary
            
    print(f"❌ Target '{target}' not found in {steps} steps.\n")
    return -1

# Test Iterative Binary Search
names = ["Arham", "Bat", "Chetan", "Dog", "Kamran", "Zebra"]
binary_search_iterative(names, "Kamran")
```

---

### 2. Recursive Binary Search (O(log N) stack memory)

```python
def binary_search_recursive(arr, target, left, right, depth=0):
    """
    Finds index of target in sorted arr recursively. Time: O(log N), Space: O(log N).
    """
    indent = "  " * depth
    print(f"{indent}▶️ [CALL] binary_search_recursive(left={left}, right={right})")
    
    # Base Case 1: Target not found
    if left > right:
        print(f"{indent}❌ Target not found. Search boundaries crossed.")
        return -1
        
    mid = (left + right) // 2
    mid_val = arr[mid]
    print(f"{indent}  Checking middle index {mid} -> Value: {mid_val}")
    
    # Base Case 2: Target found
    if mid_val == target:
        print(f"{indent}🎉 Target '{target}' found at index {mid}!")
        return mid
        
    # Recursive Cases
    if mid_val < target:
        print(f"{indent}  Middle value {mid_val} < target. Searching Right side.")
        return binary_search_recursive(arr, target, mid + 1, right, depth + 1)
    else:
        print(f"{indent}  Middle value {mid_val} > target. Searching Left side.")
        return binary_search_recursive(arr, target, left, mid - 1, depth + 1)

# Test Recursive Binary Search
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("=== Starting Recursive Binary Search ===")
binary_search_recursive(numbers, 23, 0, len(numbers) - 1)
```

***

## 🔍 Step-by-Step State Dry Run (Trace Table)

Let's track variables `left`, `right`, `mid`, and `arr[mid]` when searching for missing target `20` in `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]` (Size $N = 10$):

| Step | Left Index | Right Index | Mid Index | Mid Value | Comparison | Action |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Start** | 0 | 9 | - | - | - | Initialize boundaries |
| **1** | 0 | 9 | 4 | 16 | `20 > 16` | Search Right: set `left = 5` |
| **2** | 5 | 9 | 7 | 56 | `20 < 56` | Search Left: set `right = 6` |
| **3** | 5 | 6 | 5 | 23 | `20 < 23` | Search Left: set `right = 4` |
| **End** | 5 | 4 | - | - | `left (5) > right (4)` | Loop terminates. Return -1 |

***

## 📈 Complexity & Big O Analysis

| Algorithm | Time Complexity | Space Complexity | Why? |
| :--- | :---: | :---: | :--- |
| **Linear Search** | $O(N)$ | $O(1)$ | Must scan all elements one-by-one in worst case. |
| **Binary Search (Iterative)** | $O(\log N)$ | $O(1)$ | Window size is halved each step. Uses only pointer variables. |
| **Binary Search (Recursive)**| $O(\log N)$ | $O(\log N)$ | Window size is halved. Uses stack frames for recursive calls. |

* **The power of $O(\log N)$:**
  * For $N = 1,000$ items, Binary Search takes at most **10 steps**.
  * For $N = 1,000,000$ items, it takes at most **20 steps**.
  * For $N = 1,000,000,000$ (1 billion) items, it takes at most **30 steps**! 🤯

***

## 🎓 Interview & LeetCode Applications

### LeetCode 34: Find First and Last Position of Element in Sorted Array (Medium)
> **Problem:** Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If target is not found, return `[-1, -1]`.

#### The Double Binary Search Solution (O(log N))
We run binary search twice: once to find the leftmost boundary of target, and once to find the rightmost boundary.

```python
def search_range(nums, target):
    """
    Finds first and last positions of target in O(log N) time.
    """
    print(f"=== Searching range for target: {target} ===")
    
    def find_boundary(is_left):
        left = 0
        right = len(nums) - 1
        boundary = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                boundary = mid
                if is_left:
                    # Keep looking left to find the first occurrence
                    right = mid - 1
                else:
                    # Keep looking right to find the last occurrence
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return boundary

    first = find_boundary(is_left=True)
    last = find_boundary(is_left=False)
    print(f"🎉 Range found: [{first}, {last}]\n")
    return [first, last]

# Test
search_range([5, 7, 7, 8, 8, 10], 8)
```

***

## 🤖 Connection to Machine Learning & AI: Decision Tree Routing

How does Binary Search run Machine Learning classification models?
* **Decision Trees (Inference):** Once a Decision Tree is trained (like predicting if a house is expensive or cheap), we write its parameters down as a set of rules (e.g. `If square_feet > 2000, go right; else go left`).
* **Binary Split Decisions:** During inference (making a prediction on a new house):
  * The query starts at the root node.
  * At each node, a single binary threshold comparison is made: `value > threshold`.
  * Based on this, the query routes to either the left child or the right child.
* **Why it's Binary Search:** This routing process is mathematically identical to Binary Search! 
  * At each branch of the tree, we discard the entire other half of the tree's leaves.
  * For a balanced decision tree containing $N = 1024$ decision rules, the model makes a prediction in just **10 binary routing steps ($O(\log N)$)**!
  * This is why decision trees are incredibly fast at making real-time classification predictions compared to heavy deep neural networks!
