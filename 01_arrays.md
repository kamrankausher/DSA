# Chapter 01: Arrays & Dynamic Arrays 🚀

Have you ever wondered how Python manages a list of items? How does it magically grow when you call `.append()`? And why is looking up `my_list[0]` so incredibly fast, no matter if the list has 5 items or 5 million?

Welcome to **Arrays and Dynamic Arrays**. Today, we are going to crack open the hood of computer memory and build our very own dynamic array from scratch!

***

## 💡 Real-World Analogy: The Egg Carton & The Accordion Box

To understand arrays, we have to look at two different styles:

### 1. Static Arrays (The Egg Carton)
Imagine a cardboard egg carton that has exactly **6 pockets**.
* **Fixed Size:** You cannot suddenly turn it into a 7-pocket carton. It was manufactured to hold exactly 6 items.
* **Contiguous Space:** The pockets are right next to each other in a straight line.
* **Fast Access:** If you want the egg at index 3, you don't need to count from the beginning. You can point your finger directly at the 4th pocket instantly.

### 2. Dynamic Arrays (The Accordion Box)
Now imagine you want to store toys. You buy a box that starts with room for **2 toys**. 
* **What happens when it's full?** You can't magically stretch cardboard. Instead, you buy a brand new, empty box that is **double the size** (room for 4 toys).
* You move your 2 toys from the old box into the first two spots of the new box.
* Finally, you throw the old box away!
* This is exactly how Python lists work. They hide this "create new box and move items" process so well that you never even notice it!

***

## 📌 In Simple Terms: What is an Array?

* **Static Array:** A contiguous block of computer memory of a **fixed size** where elements of the same type are stored side-by-side.
* **Dynamic Array:** A wrapper around a static array that automatically grows (resizes) when it runs out of space.
* **Contiguous Memory:** This means there are no gaps between elements in RAM. They live in consecutive address boxes.
* **Index:** The numerical address of an element starting at `0`.
* **Addressing Formula:** How does the computer find any element instantly? It uses this simple formula:
  $$\text{Address of element at index } i = \text{Base Address} + (i \times \text{Size of one element})$$
  Because of this math, the computer can jump to any element in **$O(1)$ constant time**!

***

## 🧠 Memory Model: Arrays in RAM

Let's look at how a static array of integers `[10, 20, 30]` is stored in memory. Assume the base address is `1000` and each integer takes `4 bytes`.

```
                  RAM MEMORY HOUSES
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ Address 1000 │ Address 1004 │ Address 1008 │ Address 1012 │
├──────────────┼──────────────┼──────────────┼──────────────┤
│ Value: 10    │ Value: 20    │ Value: 30    │  [Empty]     │
├──────────────┼──────────────┼──────────────┼──────────────┤
│  Index: 0    │  Index: 1    │  Index: 2    │  Index: 3    │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

If we want the element at index 2:
$$\text{Address} = 1000 + (2 \times 4) = 1008$$
The computer goes straight to address `1008` and reads `30`. It doesn't have to scan index 0 or index 1 first!

***

## 🧠 Custom Python Implementation: Building a Dynamic Array

Let's build a `DynamicArray` class using Python's low-level list type as our "raw memory block" to see how resizing, appending, inserting, and deleting work under the hood.

```python
import ctypes

class DynamicArray:
    def __init__(self):
        """Initializes an empty dynamic array."""
        self.size = 0         # Number of actual elements currently stored
        self.capacity = 2     # How many elements the raw array can hold before resizing
        self.raw_array = self._make_raw_array(self.capacity) # Create low-level static array
        print(f"[INIT] DynamicArray created. Size: {self.size}, Capacity: {self.capacity}")

    def _make_raw_array(self, capacity):
        """Creates a raw static array of a fixed capacity (using ctypes)."""
        return (capacity * ctypes.py_object)()

    def __len__(self):
        """Returns the number of elements in the array."""
        return self.size

    def __getitem__(self, index):
        """Allows accessing elements using array[index] syntax."""
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds!")
        return self.raw_array[index]

    def append(self, element):
        """Adds an element to the end of the array. Resizes if capacity is reached."""
        print(f"\n[APPEND] Attempting to append '{element}'")
        
        # Check if we have hit the capacity limit
        if self.size == self.capacity:
            print(f"[WARN] Array is full! Size ({self.size}) == Capacity ({self.capacity}). Resizing...")
            self._resize(2 * self.capacity)  # Double the capacity!
            
        self.raw_array[self.size] = element
        print(f"[DEBUG] Stored '{element}' at index {self.size}")
        self.size += 1
        print(f"[STATUS] Current Size: {self.size}, Current Capacity: {self.capacity}")

    def _resize(self, new_capacity):
        """Creates a new static array and copies elements over."""
        print(f"[RESIZE] Creating new raw array of capacity: {new_capacity}")
        new_raw_array = self._make_raw_array(new_capacity)
        
        # Copy elements from old array to new array
        for idx in range(self.size):
            print(f"  [COPY] Copying element '{self.raw_array[idx]}' from old index {idx} to new array")
            new_raw_array[idx] = self.raw_array[idx]
            
        self.raw_array = new_raw_array
        self.capacity = new_capacity
        print(f"[RESIZE DONE] Capacity upgraded to {new_capacity}")

    def insert(self, index, element):
        """Inserts an element at a specific index, shifting all subsequent elements right."""
        print(f"\n[INSERT] Inserting '{element}' at index {index}")
        if not 0 <= index <= self.size:
            raise IndexError("Index out of bounds!")

        if self.size == self.capacity:
            print(f"[WARN] Array full at insert! Resizing...")
            self._resize(2 * self.capacity)

        # Shift elements to the right to make room
        for idx in range(self.size, index, -1):
            print(f"  [SHIFT] Shifting '{self.raw_array[idx-1]}' from index {idx-1} to index {idx}")
            self.raw_array[idx] = self.raw_array[idx-1]

        self.raw_array[index] = element
        self.size += 1
        print(f"[DEBUG] Stored '{element}' at index {index}")
        print(f"[STATUS] Current Size: {self.size}, Current Capacity: {self.capacity}")

    def pop(self):
        """Removes and returns the last element of the array."""
        if self.size == 0:
            raise IndexError("Pop from empty array!")
        
        last_idx = self.size - 1
        val = self.raw_array[last_idx]
        self.raw_array[last_idx] = None  # Clear reference for garbage collection
        self.size -= 1
        print(f"\n[POP] Removed last element '{val}' from index {last_idx}")
        print(f"[STATUS] Current Size: {self.size}, Current Capacity: {self.capacity}")
        return val

    def print_array(self):
        """Prints the visual contents of the array."""
        elements = [str(self.raw_array[i]) for i in range(self.size)]
        capacity_layout = elements + ["_"] * (self.capacity - self.size)
        print("Array visualization: [ " + " | ".join(capacity_layout) + " ]")


# --- Testing our Dynamic Array ---
arr = DynamicArray()
arr.print_array()

arr.append(10)
arr.append(20)
arr.print_array()

# This append will trigger a resize!
arr.append(30)
arr.print_array()

# Let's insert in the middle
arr.insert(1, 15)
arr.print_array()

# Pop an element
arr.pop()
arr.print_array()
```

***

## 🔍 Step-by-Step Dry Run / Trace Table

Let's track how the `size`, `capacity`, and internal layout change when we append values `10`, `20`, and `30` to an empty `DynamicArray` starting with capacity `2`:

| Operation | Value | Size Before | Capacity Before | Resize Triggered? | New Capacity | Size After | Internal Layout (Capacity Slots) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Initialize** | - | - | - | - | 2 | 0 | `[ _ | _ ]` |
| **Append** | 10 | 0 | 2 | No | 2 | 1 | `[ 10 | _ ]` |
| **Append** | 20 | 1 | 2 | No | 2 | 2 | `[ 10 | 20 ]` |
| **Append** | 30 | 2 | 2 | **Yes** (Size == Cap) | 4 | 3 | `[ 10 | 20 | 30 | _ ]` |

### Why is resizing "Amortized" $O(1)$?
You might say: *"Hey! Resizing copies all elements, which takes $O(N)$ steps. Why do we say appending is fast?"*
* **The Math:** If we start with capacity 1 and double every time:
  * Resizing happens at size 1, 2, 4, 8, 16...
  * For $N$ elements, the total cost of copy operations is $1 + 2 + 4 + 8 + \dots + N \approx 2N$ operations.
  * If we share (amortize) these $2N$ copy operations across the $N$ appends, each append only does **2 copy operations on average**.
  * Hence, the **average (amortized) time complexity of append is $O(1)$**!

***

## 📈 Complexity & Big O Analysis

| Operation | Time Complexity (Static) | Time Complexity (Dynamic) | Space Complexity | Why? |
| :--- | :---: | :---: | :---: | :--- |
| **Access (Get item)** | $O(1)$ | $O(1)$ | $O(1)$ | Memory address formula arithmetic is instant. |
| **Search (Find item)** | $O(N)$ | $O(N)$ | $O(1)$ | Must check elements one-by-one from index 0. |
| **Insertion (Start)** | $O(N)$ | $O(N)$ | $O(1)$ | Must shift all elements one index to the right. |
| **Insertion (End)** | N/A | $O(1)$ (Amortized) | $O(1)$ | No shifting required, just drop in last slot. |
| **Deletion (Start)** | $O(N)$ | $O(N)$ | $O(1)$ | Must shift all elements one index to the left. |
| **Deletion (End)** | N/A | $O(1)$ | $O(1)$ | No shifting required, just decrease size by 1. |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 1: Two Sum (Easy)
> **Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

#### The O(N) Hash Map Approach (Efficient)
Instead of comparing every number to every other number ($O(N^2)$), we store numbers we have already seen in a Hash Map. As we loop, we look for our complement: `complement = target - current_number`.

```python
def two_sum(nums, target):
    """
    Finds two indices that sum up to target in O(N) time.
    """
    print(f"=== Running Two Sum for target: {target} ===")
    seen = {} # Dictionary to store: { number: index }
    
    for index, num in enumerate(nums):
        complement = target - num
        print(f"Index {index}: Number is {num}. Complement needed: {complement}")
        
        # Check if the complement is already in our dictionary
        if complement in seen:
            prev_index = seen[complement]
            print(f"🎉 Success! Found {complement} at index {prev_index} and {num} at index {index}")
            return [prev_index, index]
            
        # Store the current number and its index
        seen[num] = index
        print(f"  Stored {num} with index {index} in seen dictionary: {seen}")
        
    print("❌ No pair found that sums to target.")
    return []

# Test the function
two_sum([2, 7, 11, 15], 9)
```

---

### LeetCode 88: Merge Sorted Array (Easy/Medium)
> **Problem:** You are given two sorted integer arrays `nums1` and `nums2`. Merge them into a single sorted array. To make it space-efficient, `nums1` has empty slots at the end to fit `nums2`.

#### The Three-Pointer Approach (O(N + M))
Instead of merging and then sorting (which is slow), we use three pointers starting from the **end** of both arrays. We compare values and write the larger value into the back of `nums1`.

```python
def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merges nums2 into nums1 in-place in O(n + m) time using three pointers.
    m: Number of actual initialized elements in nums1
    n: Number of elements in nums2
    """
    print(f"=== Merging Sorted Arrays ===")
    p1 = m - 1          # Pointer for nums1 elements
    p2 = n - 1          # Pointer for nums2 elements
    p_write = m + n - 1 # Pointer to write in nums1 from the back
    
    print(f"Initial positions: p1={p1}, p2={p2}, p_write={p_write}")
    
    while p2 >= 0:
        # If nums1 element is larger, put it at the write pointer
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            print(f"[MOVE] nums1[{p1}] ({nums1[p1]}) is larger than nums2[{p2}] ({nums2[p2]}). Writing {nums1[p1]} at index {p_write}")
            nums1[p_write] = nums1[p1]
            p1 -= 1
        else:
            # Otherwise, write the element from nums2
            print(f"[MOVE] nums2[{p2}] ({nums2[p2]}) is larger or p1 is empty. Writing {nums2[p2]} at index {p_write}")
            nums1[p_write] = nums2[p2]
            p2 -= 1
        p_write -= 1
        print(f"  Current state of nums1: {nums1}")
        
    print(f"🎉 Merge complete! Final array: {nums1}\n")

# Test the function
# Note: nums1 has three zeros at the end acting as buffers
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge_sorted_arrays(nums1, 3, nums2, 3)
```

***

## 🤖 Connection to Machine Learning & AI: GPU Tensor Locality

Why are arrays crucial for artificial intelligence?
* **Tensors are Arrays:** In machine learning libraries like **PyTorch** and **TensorFlow**, neural network inputs, weights, and biases are represented as multi-dimensional arrays called **Tensors**.
* **Cache Locality:** CPUs and GPUs have high-speed "Cache" memory. When a processor fetches a number from RAM, it doesn't fetch just that number; it fetches an entire contiguous block next to it.
* **Why contiguous layouts speed up ML:** Because elements in a static array are stored directly next to each other, the processor loads them into the cache all at once. When performing large matrix multiplications (the core of LLM attention and Neural Networks), the processor reads data straight from the super-fast Cache instead of waiting for slow RAM.
* If tensors were stored in scattered memory (like Linked Lists), training a model would be **thousands of times slower**!
