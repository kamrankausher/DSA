# Chapter 12: Heaps & Priority Queues 🚀

Imagine entering a hospital Emergency Room with a sprained ankle. You check in, sit down, and wait. Ten minutes later, an ambulance arrives carrying a patient with a severe chest pain. 

Does the doctor treat you first because you arrived first? Absolutely not. The doctor treats the chest pain patient immediately.

In programming, this is a **Priority Queue**, and the most efficient way to build one is using a data structure called a **Heap**. Today, we will learn how heaps represent trees inside simple arrays, implement a heap from scratch, and see how they guide AI decision-making.

***

## 💡 Real-World Analogy: The ER Triage & The Corporate Ladder

Think of these two priority models:

### 1. The ER Triage (Priority Queue)
* In a standard Queue, elements follow FIFO (First In, First Out).
* In a Priority Queue, elements are dequeued based on their **priority value**, regardless of arrival order. 
* To make this super fast, we use a Heap.

### 2. The Corporate Promotion Ladder (Heap Tree)
* A heap is structured like a corporate ladder.
* The most qualified person (highest priority/value) sits at the root (CEO).
* Every parent node has higher status than its direct children.
* When the CEO retires (is popped), the person at the bottom of the ladder is temporarily moved to the CEO chair. 
* To fix this, we compare them with the vice presidents below them and "demote" (bubble down) them step-by-step until everyone is in their correct rank.

***

## 📌 In Simple Terms: Min-Heaps vs. Max-Heaps

* **Min-Heap:** A binary tree where the parent node is **always smaller than or equal to** its children. The smallest value is always at the Root.
* **Max-Heap:** A binary tree where the parent node is **always larger than or equal to** its children. The largest value is always at the Root.
* **Complete Tree Property:** Heaps are always complete binary trees—every level is fully packed, filled left-to-right.
* **The Array Trick:** Because heaps have no holes, we don't need pointers! We can store the entire tree in a flat array and navigate using simple index formulas:
  * For any node at index $i$:
    * Parent Index:
      $$\text{Parent}(i) = (i - 1) // 2$$
    * Left Child Index:
      $$\text{Left}(i) = 2 \times i + 1$$
    * Right Child Index:
      $$\text{Right}(i) = 2 \times i + 2$$

***

## 🧠 Memory Model: A Min-Heap represented in an Array

Here is a Min-Heap tree and its identical representation in a flat array. 

```
           Tree Representation                 Array Representation
                 [5] (Idx 0)                Index: [  0  |  1  |  2  |  3  |  4  ]
                /   \                       Value: [  5  | 12  |  9  | 25  | 18  ]
             [12]   [9]
            (Idx 1)(Idx 2)                  Parent index formulas:
             /   \                          * Left child of Idx 0: 2(0) + 1 = 1 (Value 12)
          [25]   [18]                       * Right child of Idx 0: 2(0) + 2 = 2 (Value 9)
         (Idx 3) (Idx 4)                    * Parent of Idx 4: (4 - 1)//2 = 1 (Value 12)
```

***

## 🧠 Python Implementation: Custom Min-Heap from Scratch

Let's write a complete `MinHeap` in Python using an array backend, showing tracing prints of heapify swaps.

```python
class MinHeap:
    def __init__(self):
        self.heap = []
        print("[INIT] Created empty MinHeap.")

    def peek(self):
        """Returns the smallest element (Root) without removing it."""
        return self.heap[0] if self.heap else None

    def push(self, val):
        """Inserts a new value into the heap and bubbles it up."""
        print(f"\n[PUSH] Adding: {val}")
        # 1. Place the new element at the very end of the array
        self.heap.append(val)
        new_idx = len(self.heap) - 1
        print(f"  [DEBUG] Placed {val} at index {new_idx}. Heap State: {self.heap}")
        
        # 2. Bubble it up to restore Min-Heap property
        self._heapify_up(new_idx)

    def _heapify_up(self, index):
        """Restores heap property by swapping upward with parents."""
        parent_idx = (index - 1) // 2
        
        # While we are not at the root and current value is smaller than parent
        while index > 0 and self.heap[index] < self.heap[parent_idx]:
            print(f"  [HEAPIFY UP] Swapping index {index} ({self.heap[index]}) < parent index {parent_idx} ({self.heap[parent_idx]})")
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            print(f"    Current Heap: {self.heap}")
            
            # Move index up
            index = parent_idx
            parent_idx = (index - 1) // 2

    def pop(self):
        """Removes and returns the smallest element (Root)."""
        if not self.heap:
            raise IndexError("Pop from empty heap!")
            
        print(f"\n[POP] Request to remove smallest element (Root: {self.heap[0]})")
        
        # Case 1: Only one element left
        if len(self.heap) == 1:
            val = self.heap.pop()
            print("  [DEBUG] Heap now empty.")
            return val

        # Case 2: Multi-node heap
        root_val = self.heap[0]
        # Swap root with the last element
        self.heap[0] = self.heap.pop()
        print(f"  [SWAP TAIL] Moved last element to Root. Heap: {self.heap}")
        
        # Bubble down the root to its correct spot
        self._heapify_down(0)
        
        return root_val

    def _heapify_down(self, index):
        """Restores heap property by swapping downward with smaller child."""
        n = len(self.heap)
        smallest = index
        
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            
            # Check if left child is smaller than current smallest
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Check if right child is smaller than current smallest
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            # If the smallest is still the parent, heap property is restored
            if smallest == index:
                print(f"  [HEAPIFY DOWN DONE] Index {index} is in place.")
                break
                
            print(f"  [HEAPIFY DOWN] Swapping parent index {index} ({self.heap[index]}) with smaller child index {smallest} ({self.heap[smallest]})")
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            print(f"    Current Heap: {self.heap}")
            
            # Shift index down
            index = smallest


# --- Test our Min-Heap ---
h = MinHeap()
h.push(15)
h.push(12)
h.push(9)
h.push(25)
h.push(5)

# Smallest element (5) should be at root (index 0)
print(f"\nSmallest element peeked: {h.peek()}")

# Pop elements (they come out in sorted order!)
h.pop()
h.pop()
```

***

## 🔍 Step-by-Step Pop Heapify-Down Dry Run

Let's trace what happens when we `pop()` the minimum element `5` from our heap `[5, 12, 9, 25, 18]`:

1. **Pop and Swap Last:** Remove `5` from root, place the last element `18` at root index 0. Array becomes: `[18, 12, 9, 25]`.
2. **Heapify Down (Index 0):**
   * Compare parent `18` with left child `12` (index 1) and right child `9` (index 2).
   * Smallest child is `9`. Since `18 > 9`, swap them!
   * Array becomes: `[9, 12, 18, 25]`.
3. **Heapify Down (Index 2):**
   * Pointers for index 2: left child index is $2(2)+1 = 5$, which is out of bounds.
   * Process terminates! Heap is restored.

| Heap State After Swap | Checked Index | Left Child Index (Val) | Right Child Index (Val) | Smallest Index | Action |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `[18, 12, 9, 25]` | 0 | 1 (12) | 2 (9) | 2 | Swap 18 and 9 |
| `[9, 12, 18, 25]` | 2 | 5 (None) | 6 (None) | 2 | Stop (No children) |

***

## 📈 Complexity & Big O Analysis

| Operation | Heap Time Complexity | Unsorted Array Complexity | Sorted Array Complexity | Why? |
| :--- | :---: | :---: | :---: | :--- |
| **Insert (Push)** | $O(\log N)$ | $O(1)$ | $O(N)$ | Tree height is $\log N$; bubbling up takes at most $\log N$ swaps. |
| **Extract Min/Max (Pop)**| $O(\log N)$ | $O(N)$ (must scan) | $O(N)$ (must shift) | Swapping is $O(1)$, bubbling down takes at most $\log N$ swaps. |
| **Get Min/Max (Peek)** | $O(1)$ | $O(N)$ (must scan) | $O(1)$ (at index 0) | The minimum is always stored at root index 0. |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 703: Kth Largest Element in a Stream (Easy/Medium)
> **Problem:** Design a class to find the `k`th largest element in a stream of numbers. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

#### The Min-Heap Window Strategy (O(log K) insertion)
We maintain a **Min-Heap** containing exactly **$K$ elements**. 
* The root of this Min-Heap represents the *smallest* of our top $K$ largest elements, which is exactly the **$K$th largest element overall**!
* If a new number is larger than the root, we pop the root and push the new number.

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        """Initializes a Min-Heap of size k containing the largest elements."""
        self.k = k
        self.heap = nums
        
        # Turn list into a Min-Heap in-place
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
            
        print(f"[KTH STREAM INIT] Initialized with top {k} elements: {self.heap}")

    def add(self, val):
        """Adds a new number to the stream and returns the Kth largest element."""
        print(f"\n[ADD] Stream gets number: {val}")
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            print(f"  {val} is larger than current Kth largest ({self.heap[0]}). Swapping...")
            heapq.heappushpop(self.heap, val)
            
        result = self.heap[0]
        print(f"  🎉 Current {self.k}th largest element is: {result}")
        return result


# Test Stream
stream = KthLargest(3, [4, 5, 8, 2])
stream.add(3) # Heap remains [4, 5, 8] -> returns 4
stream.add(5) # Heap becomes [5, 5, 8] -> returns 5
```

***

## 🤖 Connection to Machine Learning & AI: LLM Beam Search Decoding

How do heaps run generative Large Language Models?
* **Text Generation:** When an LLM generates a response, it outputs predicted probabilities for the next word (token).
* **Greedy Search (Simple):** The model just picks the single highest probability token at each step. This can lead to repetitive, low-quality text.
* **Beam Search (Smart):** Instead of picking just 1 word, the model keeps track of the top $B$ (Beam Width, e.g., $B=4$) most likely sentence sequences.
* **The Heap Optimizer:** At each generation step:
  1. The model computes the probability for all possible next words extending our 4 sentences. This creates thousands of candidate sentence paths.
  2. To track the top 4 candidate paths, the algorithm pushes all candidates into a **Min-Heap of size 4**.
  3. If a candidate path's probability is higher than the root of the heap, we pop the root and push the new candidate path in $O(\log B)$ time.
* By using heaps, the LLM can generate high-quality text in real time without wasting computing power tracking thousands of dead-end sentences!
