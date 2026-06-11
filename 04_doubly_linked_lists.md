# Chapter 04: Doubly & Circular Linked Lists 🚀

Singly Linked Lists are great, but they have one major limitation: they are a one-way street. If you are at Node #5, you cannot go back to Node #4 without starting all the way over at the Head and walking forward again.

Today, we are going to solve this by creating **two-way roads** inside our memory using **Doubly Linked Lists** and **Circular Linked Lists**!

***

## 💡 Real-World Analogy: Browser History & The Playlist Loop

To understand these structures, think of daily technology tools:

### 1. Browser Navigation (Doubly Linked List)
Think about your web browser's **Back** and **Forward** buttons.
* If you go from `Google -> Wikipedia -> YouTube`:
  * `Wikipedia` knows you came from `Google` (Prev) and are going to `YouTube` (Next).
  * Because there are pointers in both directions, you can click "Back" to go to Wikipedia, or "Forward" to return to YouTube.
  * This is a **Doubly Linked List**!

### 2. Music Playlist Loop (Circular Linked List)
Imagine a music playlist containing three songs. 
* When the 3rd song (the tail) ends, instead of stopping, the music player automatically jumps back to play the 1st song (the head).
* This continuous loop is a **Circular Linked List**!

***

## 📌 In Simple Terms: Nodes with Two Arms

* **Doubly Linked List (DLL):** A list where each node has **two pointers** (arms):
  1. `next`: Points to the node ahead.
  2. `prev`: Points to the node behind.
  * We also keep track of both the **Head** (start) and the **Tail** (end) of the list.
* **Circular Linked List:** A list (singly or doubly linked) where the **last node points back to the first node**, forming a ring. There is no `None` boundary at the end!

***

## 🧠 Memory Model: Doubly Linked Lists in RAM

Let's look at a Doubly Linked List `[10 <-> 20 <-> 30]`. 
* Pointers point in both directions!
* The Head's `prev` is `None`.
* The Tail's `next` is `None`.

```
                    RAM STORAGE (TWO-WAY LINKS)
  ┌────────────────────────────────────────────────────────┐
  │  [HEAD] ──► Node(10)      Node(20)      Node(30) ◄── [TAIL]
  ├────────────────────────────────────────────────────────┤
  │             Address:0x10  Address:0x45  Address:0x88   │
  │             ┌──────────┐  ┌──────────┐  ┌──────────┐   │
  │   None ◄────┼─ prev    │  │   prev ──┼──┼─ prev    │   │
  │             │ Data: 10 │  │ Data: 20 │  │ Data: 30 │   │
  │    0x45 ◄───┼─ next    │  │   next ──┼──┼─ next ───┼─►None
  │             └──────────┘  └──────────┘  └──────────┘   │
  └────────────────────────────────────────────────────────┘
```

***

## 🧠 Python Implementation with Forward & Backward Tracing

Let's implement a Node and a Doubly Linked List in Python, complete with step-by-step connection trace logs.

```python
class DLLNode:
    def __init__(self, data):
        """A node in a doubly linked list containing two pointers."""
        self.data = data
        self.next = None  # Points to the next node
        self.prev = None  # Points to the previous node

class DoublyLinkedList:
    def __init__(self):
        """Initializes an empty doubly linked list."""
        self.head = None
        self.tail = None
        print("[INIT] Created empty Doubly Linked List.")

    def insert_at_head(self, data):
        """Inserts a node at the head (Fast O(1))."""
        print(f"\n[INSERT HEAD] Inserting: {data}")
        new_node = DLLNode(data)

        if not self.head:
            # List is empty: head and tail are the same node
            self.head = new_node
            self.tail = new_node
            print(f"  [STATUS] List was empty. Head & Tail set to Node({data})")
            return

        # Link new node and old head
        new_node.next = self.head
        self.head.prev = new_node
        print(f"  [POINTER] Linked Node({data}) <-> Node({self.head.data})")
        
        # Update head pointer
        self.head = new_node
        print(f"  [HEAD UPDATE] Head is now Node({data})")

    def append(self, data):
        """Appends a node to the tail (Fast O(1) because we track tail)."""
        print(f"\n[APPEND] Appending: {data}")
        new_node = DLLNode(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            print(f"  [STATUS] List was empty. Head & Tail set to Node({data})")
            return

        # Link new node and old tail
        self.tail.next = new_node
        new_node.prev = self.tail
        print(f"  [POINTER] Linked Node({self.tail.data}) <-> Node({data})")
        
        # Update tail pointer
        self.tail = new_node
        print(f"  [TAIL UPDATE] Tail is now Node({data})")

    def delete_node(self, target_node):
        """Deletes a specific node from the list by re-routing links in O(1) time."""
        if not self.head or not target_node:
            print("  ❌ List is empty or node is invalid.")
            return

        print(f"\n[DELETE] Deleting Node({target_node.data})")

        # Case 1: Deleting the Head node
        if target_node == self.head:
            self.head = target_node.next
            if self.head:
                self.head.prev = None
            print("  [DELETE HEAD] Head pointer shifted forward.")
            
        # Case 2: Deleting the Tail node
        elif target_node == self.tail:
            self.tail = target_node.prev
            if self.tail:
                self.tail.next = None
            print("  [DELETE TAIL] Tail pointer shifted backward.")

        # Case 3: Deleting a node in the middle
        else:
            prev_node = target_node.prev
            next_node = target_node.next
            
            # Bridge the gap
            prev_node.next = next_node
            next_node.prev = prev_node
            print(f"  [POINTER] Bridged gap: Node({prev_node.data}) <-> Node({next_node.data})")

        # Clean pointers of deleted node for garbage collection
        target_node.next = None
        target_node.prev = None

    def print_forward(self):
        """Prints the list starting from Head to Tail."""
        current = self.head
        chain = []
        while current:
            chain.append(str(current.data))
            current = current.next
        chain.append("None")
        print("Forward:  " + " -> ".join(chain))

    def print_backward(self):
        """Prints the list starting from Tail to Head."""
        current = self.tail
        chain = []
        while current:
            chain.append(str(current.data))
            current = current.prev
        chain.append("None")
        print("Backward: " + " -> ".join(chain))


# --- Testing our Doubly Linked List ---
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.insert_at_head(5)
dll.print_forward()
dll.print_backward()

# Let's delete the middle element (20)
node_to_delete = dll.head.next.next  # This is the 20 node
dll.delete_node(node_to_delete)
dll.print_forward()
```

***

## 🔍 Step-by-Step Pointer Shift Dry Run

When deleting a node in the middle of a Doubly Linked List, we must update **four pointers** to bridge the gap completely:

```
  Before deleting Node(20):
  Node(10) .next ──► Node(20) .next ──► Node(30)
  Node(10) ◄── prev Node(20) ◄── prev Node(30)
  
  Re-routing pointers (prev_node.next = next_node AND next_node.prev = prev_node):
  Node(10) .next ─────────────────────► Node(30)
  Node(10) ◄─────────────────────────── Node(30) .prev
```

| Pointer Variable | Old Target | New Target | Why? |
| :--- | :---: | :---: | :--- |
| `node_10.next` | `node_20` | `node_30` | Skip node 20 moving forward |
| `node_30.prev` | `node_20` | `node_10` | Skip node 20 moving backward |

***

## 📈 Complexity & Big O Analysis

| Operation | Singly Linked List | Doubly Linked List (with Tail) | Why? |
| :--- | :---: | :---: | :--- |
| **Access (Index)** | $O(N)$ | $O(N)$ | Must still walk from the nearest end. |
| **Insert at Head** | $O(1)$ | $O(1)$ | Swap pointers at start instantly. |
| **Insert at Tail** | $O(N)$ (without tail) | $O(1)$ | Directly write to `tail.next` in constant time! |
| **Delete at Tail** | $O(N)$ | $O(1)$ | Shift tail pointer backwards instantly via `tail.prev`. |
| **Delete Node (Mid)**| $O(N)$ (must find prev) | $O(1)$ (if node pointer is given) | Bridge pointers instantly without searching! |

***

## 🎓 Interview & LeetCode Applications

### LeetCode-Style: LRU Cache (Least Recently Used)
> **Problem:** Design a data structure that follows the constraints of a Least Recently Used (LRU) Cache. It should support `get` and `put` operations in $O(1)$ constant time.

#### Why DLL + Hash Map is the Magic Combo
1. **The Hash Map:** Gives us $O(1)$ lookups for keys.
2. **The Doubly Linked List:** Maintains usage order. The Head represents the **Least Recently Used** item, and the Tail represents the **Most Recently Used** item.
* When we access a key, we remove its node from the middle of the DLL ($O(1)$) and move it to the Tail ($O(1)$).
* If cache is full, we delete the Head node ($O(1)$) and remove its key from the Hash Map ($O(1)$).

```python
class CacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """Initializes LRU cache with a capacity."""
        self.capacity = capacity
        self.map = {} # Key -> CacheNode
        
        # Dummy head and tail nodes to avoid Null pointer checks
        self.head = CacheNode(0, 0)
        self.tail = CacheNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        print(f"[LRU INIT] Capacity set to {capacity}")

    def _remove(self, node):
        """Removes a node from the doubly linked list in O(1)."""
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add_to_tail(self, node):
        """Inserts a node at the tail (MRU end) of the list in O(1)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """Gets value of key and marks it as recently used."""
        if key in self.map:
            node = self.map[key]
            print(f"\n[GET] Key {key} found! Value: {node.value}. Moving to Tail (MRU)...")
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        print(f"\n[GET] Key {key} not found.")
        return -1

    def put(self, key, value):
        """Stores key-value pair. Evicts LRU item if capacity exceeded."""
        print(f"\n[PUT] key: {key}, value: {value}")
        if key in self.map:
            self._remove(self.map[key])
            
        new_node = CacheNode(key, value)
        self.map[key] = new_node
        self._add_to_tail(new_node)
        
        # Check if we exceeded capacity
        if len(self.map) > self.capacity:
            # Evict head node (Least Recently Used)
            lru_node = self.head.next
            print(f"  ⚠️ [EVICT] Cache Full! Evicting LRU Node(key: {lru_node.key}, val: {lru_node.value}) from Head...")
            self._remove(lru_node)
            del self.map[lru_node.key]


# Test our LRU Cache
cache = LRUCache(2)
cache.put(1, 100) # [1]
cache.put(2, 200) # [1, 2]
cache.get(1)      # [2, 1] (key 1 moved to end)
cache.put(3, 300) # Evicts key 2! Cache becomes [1, 3]
cache.get(2)      # Returns -1 (Evicted)
```

***

## 🤖 Connection to Machine Learning & AI: GPU Weight Swapping

How do Doubly Linked Lists optimize training in Large Language Models (LLMs)?
* **Deep Learning Model Size:** Modern LLMs (like Llama-3 or GPT-4) contain billions of parameters. They are too large to fit entirely in the GPU's memory (VRAM) during training or inference.
* **CPU-GPU Memory Swapping (Offloading):** To run these models on cheaper hardware, frameworks use **Layer Offloading**. Only the active layers of the neural network are kept in GPU memory, while the rest reside in slower CPU RAM.
* **LRU Layer Swapping:** The layers are represented as nodes in a **Doubly Linked List** based on when they are needed.
* When the GPU needs layer $X$ but is out of memory:
  1. The allocator queries a hash map to find the layer node.
  2. The layer node is detached from the list in $O(1)$ and loaded into VRAM.
  3. The Least Recently Used layers (at the Head of the DLL) are swapped out back to CPU RAM.
* Without the $O(1)$ DLL operations, calculating which layer to swap next would create an execution bottleneck, slowing down model execution!
