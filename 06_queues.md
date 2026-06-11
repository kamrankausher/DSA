# Chapter 06: Queues & Deques (FIFO Principle) 🚀

Imagine standing in line at a movie theater ticket counter. The first person to join the line is the first person who gets to buy a ticket and leave. If a new person arrives, they must go to the very back of the line. Trying to cut the line is extremely rude—and it violates the rules of computer science!

This is the **FIFO (First In, First Out)** principle, and it is the foundation of **Queues**. Today, we will explore queues, double-ended queues (deques), circular buffers, and learn how to implement them efficiently.

***

## 💡 Real-World Analogy: The Ticket Line & The Sushi Carousel

Think of these two common queue types:

### 1. Movie Ticket Line (Standard Queue)
* **Entering the line:** You stand at the back (rear) of the line. This is called **Enqueue**.
* **Leaving the line:** The person at the front gets their ticket and leaves. This is called **Dequeue**.
* **Rules:** First person in line is the first person served.
* **Warning:** In Python, using a regular list as a queue by calling `list.pop(0)` is slow ($O(N)$) because after removing the first item, every other person in line has to walk forward one step to close the gap!

### 2. Conveyor Belt Sushi (Circular Queue)
* Imagine a circular sushi conveyor belt with **5 plates capacity**.
* When a plate is eaten at the front, that spot becomes empty. 
* The chef at the back continues placing new plates on the moving belt in a circle.
* This is a **Circular Queue (or Circular Buffer)**. It reuses empty space at the beginning of the memory block without shifting any elements!

***

## 📌 In Simple Terms: FIFO Operations

* **FIFO (First In, First Out):** The oldest element added to the queue is the first one removed.
* **Enqueue:** Add an element to the back (rear) of the queue.
* **Dequeue:** Remove and return the element at the front of the queue.
* **Deque (Double-Ended Queue):** A queue where you can add or remove elements from *both* the front and the back.
* **Circular Queue:** A queue that uses a fixed-size array and wraps around to the beginning using **Modulo Arithmetic (`%`)** when it hits the end of the array, preventing wasted memory.

***

## 🧠 Memory Model: Circular Queue Index Wrapping

In a fixed-size circular queue of capacity `5`, we track indices `front` and `rear`.
* When we enqueue past index `4`, we wrap back to index `0` using the formula:
  $$\text{new\_index} = (\text{current\_index} + 1) \% \text{Capacity}$$

```
                CIRCULAR BUFFER (CAPACITY: 5)
                      ┌───────────────┐
                      │   Index: 0    │  ◄── [rear] (Wrapped)
                      │  Value: "F"   │
                      └───────┬───────┘
                              │
             ┌────────────────┴────────────────┐
             │                                 │
     ┌───────▼───────┐                 ┌───────▼───────┐
     │   Index: 4    │                 │   Index: 1    │
     │  Value: "E"   │                 │  Value: "B"   │  ◄── [front]
     └───────┬───────┘                 └───────┬───────┘
             │                                 │
             └────────────────┬────────────────┘
                              │
                      ┌───────▼───────┐
                      │  Indices: 2,3 │
                      │  Values: C, D │
                      └───────────────┘
```

***

## 🧠 Python Implementation: Two Custom Queues

Let's implement a standard Linked List-backed Queue and an array-based Circular Queue in Python.

### 1. Linked List-Backed Queue (Infinite Capacity, O(1) Operations)

By keeping pointers to both `front` and `rear` nodes, we can enqueue and dequeue in $O(1)$ constant time.

```python
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        print("[INIT] Created empty LinkedListQueue.")

    def enqueue(self, item):
        print(f"\n[ENQUEUE] Adding '{item}' to the rear.")
        new_node = QueueNode(item)
        
        if self.rear is None:
            # Queue was empty: both front and rear point to new node
            self.front = new_node
            self.rear = new_node
        else:
            # Link current rear to new node and update rear pointer
            self.rear.next = new_node
            self.rear = new_node
            
        self._size += 1
        print(f"  [DEBUG] Front: Node({self.front.data}), Rear: Node({self.rear.data}), Size: {self._size}")

    def dequeue(self):
        if self.front is None:
            raise IndexError("Dequeue from empty queue!")
            
        popped_val = self.front.data
        print(f"\n[DEQUEUE] Removing front element '{popped_val}'.")
        
        # Move front pointer forward
        self.front = self.front.next
        
        # If the queue is now empty, reset rear pointer
        if self.front is None:
            self.rear = None
            
        self._size -= 1
        print(f"  [DEBUG] New Front: Node({self.front.data if self.front else 'None'}), Size: {self._size}")
        return popped_val


# Test Linked List Queue
ll_queue = LinkedListQueue()
ll_queue.enqueue("Ticket A")
ll_queue.enqueue("Ticket B")
ll_queue.dequeue()
```

---

### 2. Array-Backed Circular Queue (Fixed Memory, Modulo Wrapping)

This implementation uses a fixed capacity array. It avoids element-shifting cost entirely.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0
        print(f"[INIT] CircularQueue created. Capacity: {capacity}")

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        print(f"\n[ENQUEUE] Trying to enqueue '{item}'...")
        if self.is_full():
            print("  ❌ Queue Full! Cannot add element.")
            return False
            
        if self.is_empty():
            self.front = 0
            
        # Move rear pointer forward circularly using Modulo (%)
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        
        print(f"  [DEBUG] Stored at index {self.rear}. Front pointer: {self.front}, Rear pointer: {self.rear}")
        self.print_queue_raw()
        return True

    def dequeue(self):
        print(f"\n[DEQUEUE] Trying to dequeue...")
        if self.is_empty():
            print("  ❌ Queue Empty! Nothing to dequeue.")
            return None
            
        val = self.queue[self.front]
        self.queue[self.front] = None # Clear element in memory
        
        # Move front pointer forward circularly
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        # Reset pointers if queue becomes empty
        if self.size == 0:
            self.front = -1
            self.rear = -1
            print("  [DEBUG] Queue became empty. Pointers reset to -1.")
        else:
            print(f"  [DEBUG] Removed value '{val}'. New Front pointer: {self.front}")
            
        self.print_queue_raw()
        return val

    def print_queue_raw(self):
        print(f"  Raw Memory: {self.queue} | Size: {self.size}/{self.capacity}")


# Test Circular Queue
cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40) # Fails (Full)
cq.dequeue()
cq.enqueue(40) # Succeeds! (Pushed at index 0 after wrapping)
```

***

## 🔍 Step-by-Step Circular Queue Index Wrapping Dry Run

Let's track queue variables when performing operations on a `CircularQueue` of capacity `3`:

* Size limit: 3

| Operation | Value | size | front index | rear index | Raw Memory | Modulo Math |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Initialize** | - | 0 | -1 | -1 | `[None, None, None]` | - |
| **Enqueue** | 10 | 1 | 0 | 0 | `[10, None, None]` | `(-1 + 1) % 3 = 0` |
| **Enqueue** | 20 | 2 | 0 | 1 | `[10, 20, None]` | `(0 + 1) % 3 = 1` |
| **Enqueue** | 30 | 3 | 0 | 2 | `[10, 20, 30]` | `(1 + 1) % 3 = 2` |
| **Dequeue** | 10 | 2 | 1 | 2 | `[None, 20, 30]` | Front shifted: `(0 + 1) % 3 = 1` |
| **Enqueue** | 40 | 3 | 1 | 0 | `[40, 20, 30]` | **Rear Wrapped!** `(2 + 1) % 3 = 0` |

***

## 📈 Complexity & Big O Analysis

| Operation | Dynamic Array (`pop(0)`) | Linked List Queue | Circular Queue | Why? |
| :--- | :---: | :---: | :---: | :--- |
| **Enqueue** | $O(1)$ (Amortized) | $O(1)$ | $O(1)$ | Elements are added at the end directly. |
| **Dequeue** | $O(N)$ (Slow!) | $O(1)$ | $O(1)$ | Circular Queue and LL do not shift items in RAM. |
| **Peek** | $O(1)$ | $O(1)$ | $O(1)$ | Simply access `queue[front]` in memory. |
| **Space Complexity**| $O(N)$ | $O(N)$ | $O(\text{Capacity})$ | Memory scales linearly with elements stored. |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 232: Implement Queue using Stacks (Easy/Medium)
> **Problem:** Implement a first-in-first-out (FIFO) queue using only two stacks. The implemented queue should support `push`, `pop`, `peek`, and `empty` operations.

#### The Two Stacks Swap Technique
Since a stack is LIFO, pushing elements to Stack A and popping from Stack A reverses the sequence. If we dump Stack A into Stack B, the order reverses *again*, turning it back into FIFO order!
* `stack_in`: Where we push new elements.
* `stack_out`: Where we pop elements. If `stack_out` is empty, we pour everything from `stack_in` into it.

```python
class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        print("[INIT] QueueUsingStacks created.")

    def push(self, x):
        print(f"[PUSH] Pushing {x} to stack_in.")
        self.stack_in.append(x)

    def _transfer(self):
        """Helper to transfer elements from input stack to output stack."""
        if not self.stack_out:
            print("  [TRANSFER] Transferring elements from stack_in to stack_out...")
            while self.stack_in:
                val = self.stack_in.pop()
                self.stack_out.append(val)
            print(f"    stack_out contents: {self.stack_out}")

    def pop(self):
        self._transfer()
        if not self.stack_out:
            raise IndexError("Pop from empty queue!")
        val = self.stack_out.pop()
        print(f"[POP] Dequeued: {val}")
        return val

    def peek(self):
        self._transfer()
        return self.stack_out[-1] if self.stack_out else None

    def empty(self):
        return not self.stack_in and not self.stack_out


# Test the implementation
q_stack = QueueUsingStacks()
q_stack.push(1)
q_stack.push(2)
q_stack.pop() # Returns 1!
```

***

## 🤖 Connection to Machine Learning & AI: Async DataLoader Queue

How do queues speed up Deep Learning model training?
* **The CPU-GPU Bottleneck:** GPUs are extremely fast at performing neural network calculations, but they are bottlenecked by how fast the CPU can read raw images from the hard drive, crop/augment them, and load them into GPU VRAM.
* **Synchronous Loading (Slow):** If the CPU loads a batch, then the GPU computes, then the GPU sits idle waiting for the next CPU batch, training takes forever.
* **Asynchronous Loading with Queues (Fast):** PyTorch uses a multi-threaded **DataLoader Queue**.
  * While the GPU is computing backpropagation on Batch $N$, multiple CPU worker threads are pre-fetching and preparing Batch $N+1$, $N+2$, etc., and pushing them into a FIFO **prefetch queue**.
  * As soon as the GPU finishes computing, it dequeues the next batch instantly from the queue.
  * This keeps the GPU running at 100% utilization, saving massive amounts of compute time and money!
