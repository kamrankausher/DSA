# Chapter 00: Basics of Algorithms & Time Complexity (Big O) 🚀

Have you ever wondered why some apps load instantly while others lag? Or how Google can search billions of web pages in milliseconds? 

The secret lies in **Algorithms** and **Time Complexity**. Today, we are going to learn how to write efficient code and measure its speed like a pro—even if you've never studied computer science before!

***

## 💡 Real-World Analogy: The Phone Book Search

Imagine you have a physical phone book containing 1,000 names sorted alphabetically, and you want to find your friend **"Kamran"**.

Here are three different ways you could search for him:

### 1. The Lazy Search (Linear Search)
* **What you do:** Start on page 1 and look at the first name. If it's not Kamran, move to page 2, then page 3, all the way to page 1,000.
* **Best Case:** Kamran is on page 1. You find him in **1 step**.
* **Worst Case:** Kamran is on the very last page, or not in the book at all. You take **1,000 steps**.
* **In Coding Terms:** If the book grows to 1,000,000 pages, you might have to take **1,000,000 steps**!

### 2. The Smart Search (Binary Search)
* **What you do:** Open the phone book exactly in the middle (page 500). 
  * Let's say the names there start with **"M"**. 
  * Since "K" comes before "M" in the alphabet, you tear the right half of the book (pages 501–1,000) and throw it away! 
  * Now you repeat the process with the remaining 500 pages. Open to the middle (page 250), check the letter, and throw away half again.
* **Worst Case:** Even for 1,000 pages, you will find Kamran in at most **10 steps**!
* **In Coding Terms:** If the book grows to 1,000,000 pages, this method takes at most **20 steps**! 🤯

### 3. The Magical Search (Hash Table Lookup)
* **What you do:** You call a magical fairy. You say "Kamran", and she immediately opens the book to the exact page and paragraph instantly.
* **Step Count:** Always **1 step**, no matter how big the phone book is.

***

## 📌 In Simple Terms: What is an Algorithm & Complexity?

* **Algorithm:** A step-by-step recipe to solve a problem. For example, a recipe to bake a cake or a set of rules to sort numbers.
* **Time Complexity:** This does **NOT** measure the time in seconds (because a supercomputer will run code faster than your old laptop). Instead, it measures **how the number of operations/steps grows** as the size of the input data ($N$) grows.
* **Space Complexity:** Measures how much extra memory (RAM) your code needs to run as the input size grows.

***

## 🧠 Memory Model: Stack vs. Heap in Python

When your code runs, Python stores information in two primary places:

```
┌────────────────────────────────────────────────────────┐
│                        COMPUTER RAM                    │
├────────────────────────────┬───────────────────────────┤
│          THE STACK         │          THE HEAP         │
│  (Fast, organized boxes)   │   (Large, open warehouse) │
├────────────────────────────┼───────────────────────────┤
│ age = 25                   │                           │
│ name = [ref to Heap 0x101] ├─► 0x101: "Kamran Kausher" │
│ arr  = [ref to Heap 0x102] ├─► 0x102: [10, 20, 30]     │
└────────────────────────────┴───────────────────────────┘
```

* **The Stack:** Keeps track of active function calls and simple variables. It's fast and automatically managed.
* **The Heap:** Stores large objects (like lists, strings, and custom classes). Your variables on the stack are just "pointers" (addresses) that point to objects residing in the Heap.

***

## 🧠 Big O Notation: The Growth Rates

We use **Big O Notation** (written as $O(...)$) to describe the worst-case scenario of how our algorithm scales. Let's look at the common ones from fastest to slowest:

| Big O Notation | Name | Analogy | Code Example |
| :---: | :--- | :--- | :--- |
| $O(1)$ | **Constant Time** | The Magical Search (Instant) | Accessing a list element by index |
| $O(\log N)$ | **Logarithmic Time** | The Smart Search (Halving every step) | Binary Search |
| $O(N)$ | **Linear Time** | The Lazy Search (One-by-one) | Looking through a list with a single loop |
| $O(N \log N)$ | **Linearithmic Time** | Divide-and-Conquer Sorting | Merge Sort / Quick Sort |
| $O(N^2)$ | **Quadratic Time** | Comparing everything with everything else | Nested loops (bubble sort) |

***

## 🔍 Step-by-Step Dry Run & Python Code

Let's look at real Python implementations of **Linear Search** ($O(N)$) and **Binary Search** ($O(\log N)$). 

To make it easy to understand, we have added trace logs so you can see exactly how the computer searches!

### 1. Linear Search Implementation ($O(N)$)

```python
def linear_search(name_list, target_name):
    """
    Searches for target_name in name_list one by one.
    This takes O(N) time in the worst case.
    """
    print(f"=== Starting Linear Search for '{target_name}' ===")
    steps = 0
    
    # Loop through the list index by index
    for index, name in enumerate(name_list):
        steps += 1
        print(f"Step {steps}: Checking index {index} -> Found '{name}'")
        
        if name == target_name:
            print(f"🎉 Found '{target_name}' at index {index} in {steps} steps!\n")
            return index
            
    print(f"❌ '{target_name}' not found after checking all {steps} elements.\n")
    return -1

# Let's test it!
names = ["Arham", "Bat", "Chetan", "Dog", "Kamran", "Zebra"]
linear_search(names, "Kamran")
linear_search(names, "Unicorn")
```

### 2. Binary Search Implementation ($O(\log N)$)

```python
def binary_search(sorted_list, target_name):
    """
    Searches for target in a SORTED list by halving the search space each time.
    This takes O(log N) time.
    """
    print(f"=== Starting Binary Search for '{target_name}' ===")
    steps = 0
    left = 0
    right = len(sorted_list) - 1
    
    # Keep searching while our search window is valid
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        mid_val = sorted_list[mid]
        
        print(f"Step {steps}: Search Window indices [{left} to {right}]. Checking Middle index {mid} ('{mid_val}')")
        
        if mid_val == target_name:
            print(f"🎉 Found '{target_name}' at index {mid} in {steps} steps!\n")
            return mid
        elif mid_val < target_name:
            print(f"   -> '{target_name}' comes after '{mid_val}'. Discarding Left Half.")
            left = mid + 1
        else:
            print(f"   -> '{target_name}' comes before '{mid_val}'. Discarding Right Half.")
            right = mid - 1
            
    print(f"❌ '{target_name}' not found after {steps} steps.\n")
    return -1

# Test binary search (the list MUST be sorted!)
names_sorted = ["Arham", "Bat", "Chetan", "Dog", "Kamran", "Zebra"]
binary_search(names_sorted, "Kamran")
```

***

## 🧠 Trace Table (Dry Run) for Binary Search

Let's track how variables `left`, `right`, and `mid` change in `binary_search(names_sorted, "Kamran")`:

* List: `["Arham", "Bat", "Chetan", "Dog", "Kamran", "Zebra"]` (Size $N = 6$)
* Target: `"Kamran"`

| Step | Left Index | Right Index | Mid Index | Mid Value | Comparison | Action |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Start** | 0 | 5 | - | - | - | Initialize boundaries |
| **1** | 0 | 5 | 2 | `"Chetan"` | `"Kamran" > "Chetan"` | Keep right side: set `left = 3` |
| **2** | 3 | 5 | 4 | `"Kamran"` | `"Kamran" == "Kamran"` | Match Found! Return index 4 |

***

## 🤖 Connection to Machine Learning & AI: The Transformer Bottleneck

Why do AI developers care about time complexity? Let's talk about **LLMs** (like ChatGPT, Claude, or Gemini).

Inside Large Language Models, there is an architecture called a **Transformer**, which uses a mechanism called **Self-Attention**.
* When you prompt an LLM, the model compares every token (word) in your prompt to every other token to understand context.
* If your prompt has $N$ tokens, the complexity of this comparison is **$O(N^2)$ (Quadratic Complexity)**.
* **Why this matters:** If your input text doubles in size, the computing power required increases by **4 times**! If it triples, it increases by **9 times**!
* This is why long context windows (handling large PDFs or books) are extremely expensive to compute, and why researchers are constantly trying to invent new models with $O(N)$ or $O(N \log N)$ complexity!
