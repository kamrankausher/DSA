# Chapter 07: Basic Sorting Algorithms 🚀

How does your computer sort a list of grades? How does Amazon sort products by price? Behind these buttons are **Sorting Algorithms**—the rules for arranging elements in a specific order (like low-to-high).

Today, we will learn the three classic, beginner-friendly sorting techniques: **Bubble Sort**, **Selection Sort**, and **Insertion Sort**. We will examine how they work visually and write Python code that traces every comparison and swap!

***

## 💡 Real-World Analogies: Soda Bubbles, Player Drafts & Playing Cards

To understand basic sorting, think of three physical actions:

### 1. Bubble Sort (Soda Bubbles)
Imagine bubbles rising in a glass of soda. The largest bubbles rise to the top the fastest.
* **The Process:** You compare adjacent items. If they are in the wrong order, you swap them.
* You do this over and over. By the end of the 1st pass, the largest number has "bubbled up" to the very end of the array.
* Repeat this for the remaining unsorted numbers!

### 2. Selection Sort (Tug-of-War Player Draft)
Imagine selecting players for a game, lining them up from shortest to tallest.
* **The Process:** You scan the entire line, locate the **shortest person**, and swap them with the first person in line.
* Now, the first spot is sorted. You look at the remaining line, find the next shortest person, and swap them with the second spot.
* You keep *selecting* the minimum element and placing it in its correct position.

### 3. Insertion Sort (Sorting Playing Cards)
Imagine you are dealt a hand of playing cards one by one.
* **The Process:** You hold the sorted cards in your left hand. When a new card arrives, you scan your sorted cards from right to left and **slide (insert)** the new card into its correct position.
* You repeat this for every card until your entire hand is sorted!

***

## 📌 In Simple Terms: Unsorted vs. Sorted Boundaries

All three basic sorting algorithms divide the array into two logical zones:
1. **Sorted Zone:** Already in order.
2. **Unsorted Zone:** Still needs sorting.

With each outer loop iteration, the **Sorted Zone** grows by 1 element, and the **Unsorted Zone** shrinks by 1 element.

***

## 🧠 Memory Model: The Selection Sort Swap

During sorting, elements are rearranged in-place inside the **Heap** array. Let's trace a swap between index `0` and index `3` in Selection Sort:

```
  Unsorted Array: [ 40 | 20 | 50 | 10 ]  (Min found is 10 at index 3)
                     ▲               ▲
                     │               │
                 Swap target     Min Element
                  (Index 0)       (Index 3)
                  
  Performing Swap:
  Temp = arr[0] (40)
  arr[0] = arr[3] (10)
  arr[3] = Temp (40)
  
  After Swap:     [ 10 | 20 | 50 | 40 ]
                    └─── Sorted ───┘
```

***

## 🧠 Python Implementation with Interactive Swap Tracing

Let's write Bubble, Selection, and Insertion Sort in Python, including prints to track variable values.

### 1. Bubble Sort Implementation

```python
def bubble_sort(arr):
    """
    Sorts arr in-place using Bubble Sort. Time: O(N^2), Space: O(1).
    """
    n = len(arr)
    print(f"=== Starting Bubble Sort on {arr} ===")
    
    for i in range(n):
        swapped = False
        print(f"\n--- Pass {i+1} (Finding the {i+1}th largest element) ---")
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            print(f"  Comparing arr[{j}] ({arr[j]}) and arr[{j+1}] ({arr[j+1]})")
            if arr[j] > arr[j+1]:
                print(f"    ⚠️ Swap! {arr[j]} > {arr[j+1]}. Swapping.")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"    Current Array State: {arr}")
                
        # If no two elements were swapped in the inner loop, the array is sorted!
        if not swapped:
            print("  🎉 No swaps occurred in this pass. Array is already sorted!")
            break
            
    print(f"🎉 Bubble Sort Complete! Final: {arr}\n")
    return arr

# Test Bubble Sort
bubble_sort([64, 34, 25, 12, 22])
```

---

### 2. Selection Sort Implementation

```python
def selection_sort(arr):
    """
    Sorts arr in-place using Selection Sort. Time: O(N^2), Space: O(1).
    """
    n = len(arr)
    print(f"=== Starting Selection Sort on {arr} ===")
    
    for i in range(n):
        min_idx = i
        print(f"\n--- Pass {i+1}: Sorted Boundary Index = {i} ---")
        
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            print(f"  Comparing current minimum '{arr[min_idx]}' with '{arr[j]}'")
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"    New minimum candidate found: '{arr[min_idx]}' at index {min_idx}")
                
        # Swap the found minimum element with the first element of unsorted boundary
        if min_idx != i:
            print(f"  🔄 Swap! Swapping '{arr[i]}' at index {i} with minimum '{arr[min_idx]}' at index {min_idx}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  Current Array State: {arr}")
        else:
            print(f"  Index {i} already contains the minimum value '{arr[i]}'. No swap needed.")
            
    print(f"🎉 Selection Sort Complete! Final: {arr}\n")
    return arr

# Test Selection Sort
selection_sort([29, 10, 14, 37, 13])
```

---

### 3. Insertion Sort Implementation

```python
def insertion_sort(arr):
    """
    Sorts arr in-place using Insertion Sort. Time: O(N^2), Space: O(1).
    """
    print(f"=== Starting Insertion Sort on {arr} ===")
    
    for i in range(1, len(arr)):
        key = arr[i] # The card we are inserting
        j = i - 1
        print(f"\n--- Pass {i}: Inserting key '{key}' from index {i} ---")
        
        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead of their current position
        while j >= 0 and arr[j] > key:
            print(f"  Shift: '{arr[j]}' > '{key}'. Shifting '{arr[j]}' from index {j} to index {j+1}")
            arr[j+1] = arr[j]
            j -= 1
            print(f"    Current Array State: {arr}")
            
        arr[j+1] = key
        print(f"  🎉 Placed key '{key}' at index {j+1}.")
        print(f"  Current Array State: {arr}")
        
    print(f"🎉 Insertion Sort Complete! Final: {arr}\n")
    return arr

# Test Insertion Sort
insertion_sort([12, 11, 13, 5, 6])
```

***

## 🔍 Step-by-Step State Dry Run (Trace Table)

Let's compare how the array `[5, 2, 4, 1]` changes at the end of each pass ($i$-loop) for all three algorithms:

| Pass ($i$) | Bubble Sort State | Selection Sort State | Insertion Sort State |
| :---: | :---: | :---: | :---: |
| **Start** | `[5, 2, 4, 1]` | `[5, 2, 4, 1]` | `[5, 2, 4, 1]` |
| **Pass 1**| `[2, 4, 1, 5]` (5 bubbled to end) | `[1, 2, 4, 5]` (1 swapped with 5) | `[2, 5, 4, 1]` (2 inserted before 5) |
| **Pass 2**| `[2, 1, 4, 5]` (4 placed at index 2) | `[1, 2, 4, 5]` (2 already in place) | `[2, 4, 5, 1]` (4 inserted between 2 and 5) |
| **Pass 3**| `[1, 2, 4, 5]` (2 placed at index 1) | `[1, 2, 4, 5]` (4 already in place) | `[1, 2, 4, 5]` (1 inserted at index 0) |

***

## 📈 Complexity & Big O Analysis

| Algorithm | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stable? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Bubble Sort** | $O(N)$ (Already sorted) | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Yes** |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **No** |
| **Insertion Sort** | $O(N)$ (Already sorted) | $O(N^2)$ | $O(N^2)$ | $O(1)$ | **Yes** |

* **Stability:** A sorting algorithm is **stable** if it preserves the relative order of duplicate elements. (e.g. if we have two `5`s in our list, a stable sort guarantees the `5` that started first stays first).
* **Selection Sort Stability:** Why is Selection Sort unstable? Because its long swaps can jump over other duplicate items and ruin their ordering.

***

## 🎓 Interview & LeetCode Applications

### LeetCode 75: Sort Colors (Medium)
> **Problem:** Given an array `nums` with $N$ objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue (represented as `0`, `1`, and `2`).

#### The Dutch National Flag Algorithm (O(N) time, O(1) space)
We use three pointers: `low` (boundary of 0s), `mid` (current element), and `high` (boundary of 2s). We examine `nums[mid]` and swap it into its correct group.

```python
def sort_colors(nums):
    """
    Sorts colors (0s, 1s, 2s) in-place in O(N) time using three pointers.
    """
    print(f"=== Sorting Colors on {nums} ===")
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            # Swap with low boundary
            print(f"  Found 0 at index {mid}. Swapping with index {low} (value: {nums[low]})")
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Already in middle group
            mid += 1
        else: # nums[mid] == 2
            # Swap with high boundary
            print(f"  Found 2 at index {mid}. Swapping with index {high} (value: {nums[high]})")
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        print(f"    Current state: {nums}")
        
    print(f"🎉 Sort complete: {nums}\n")

# Test it
sort_colors([2, 0, 2, 1, 1, 0])
```

***

## 🤖 Connection to Machine Learning & AI: The KNN Sorting Bottleneck

How do basic sorting complexities affect Machine Learning algorithms?
* **K-Nearest Neighbors (KNN):** KNN is a classification algorithm. To classify a new query point, KNN calculates the geometric distance between the query point and **every single point** in the dataset ($N$ distance computations).
* **The Sort Step:** To find the $K$ closest neighbors, KNN must sort these calculated distances.
* **The Bottleneck:** If KNN uses a simple $O(N^2)$ bubble or selection sort:
  * For $N = 10,000$ points, it would require around $100,000,000$ operations!
  * This makes KNN inference extremely slow on large datasets.
* **Modern Solution:** Production vector search databases (like FAISS, Pinecone, or Milvus) avoid sorting raw arrays. Instead, they pre-index vectors using tree structures (KD-Trees) or graphs (HNSW - Hierarchical Navigable Small World) to look up approximate neighbors in **$O(\log N)$ or $O(1)$** time!
