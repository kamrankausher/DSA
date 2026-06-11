# Chapter 03: Singly Linked Lists 🚀

If arrays are like egg cartons where items are forced to live side-by-side, what do you do when elements want to live freely in different parts of the computer's memory, yet still stay connected in a sequence?

You use a **Singly Linked List**. In this chapter, we will learn how to build dynamic chains of memory blocks using **Nodes** and **Pointers**, trace list traversals, and implement classic interview algorithms.

***

## 💡 Real-World Analogy: The Scavenger Hunt Clues

Imagine you are playing a scavenger hunt game. 
* You are handed a slip of paper (Clue #1) that says: *"Your prize is at the Library. Also, the next clue is hidden inside the hollow tree in the backyard."*
* You go to the hollow tree, find Clue #2, which says: *"Your prize is a chocolate bar. Also, the next clue is inside the kitchen microwave."*
* You go to the microwave, find Clue #3, which says: *"Your prize is a video game. There are no more clues!"*

This is exactly how a Singly Linked List works:
* **The Clues are Nodes:** Each clue contains some data (the prize) and a direction pointing to the next clue.
* **The Locations are Scattered:** The library, the backyard tree, and the kitchen microwave are scattered all over the place—they are not lined up side-by-side.
* **Traversal is Required:** You cannot jump directly to Clue #3 without first finding Clue #1 and Clue #2. You must follow the trail!

***

## 📌 In Simple Terms: Array vs. Linked List

Let's compare arrays and linked lists to see why we need both:

| Feature | Array | Linked List |
| :--- | :--- | :--- |
| **Memory Layout** | **Contiguous:** All elements must sit side-by-side in one massive block. | **Scattered:** Elements can live anywhere in RAM. |
| **Resizing Cost** | **Expensive:** Must copy all elements to a new larger array when full. | **Free:** Just request a new node and link it at the end. |
| **Access Speed** | **Instant $O(1)$:** Can jump directly to any index via formula. | **Slow $O(N)$:** Must start at the head and walk through pointers. |

***

## 🧠 Memory Model: Nodes and Pointers in RAM

In a linked list, each element is wrapped in a **Node**. A node has two parts:
1. **Data:** The actual value we want to store (e.g. `10`).
2. **Next Pointer:** The memory address of the next node.

Let's look at a list `[10 -> 20 -> 30]` stored in memory. The node containing `10` is at address `0x100`, `20` is at `0x450`, and `30` is at `0x880`.

```
          RAM STORAGE (SCATTERED)
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ Address: 0x100   │  │ Address: 0x450   │  │ Address: 0x880   │
├──────────────────┤  ├──────────────────┤  ├──────────────────┤
│ Data: 10         │  │ Data: 20         │  │ Data: 30         │
│ Next: 0x450   ───┼─►│ Next: 0x880   ───┼─►│ Next: None (Null)│
└──────────────────┘  └──────────────────┘  └──────────────────┘
       ▲
       │
   [ HEAD ]
```

***

## 🧠 Python Implementation with Traversal Tracing

Let's build a `SinglyLinkedList` in Python. We will add print statements to trace how pointers shift during insertions and deletions.

```python
class Node:
    def __init__(self, data):
        """A single element container in a linked list."""
        self.data = data
        self.next = None  # Pointer to the next node, defaults to None

class SinglyLinkedList:
    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None
        print("[INIT] Created an empty linked list.")

    def insert_at_head(self, data):
        """Inserts a new node at the very beginning of the list (Fast O(1))."""
        print(f"\n[INSERT HEAD] Inserting value: {data}")
        new_node = Node(data)
        
        # Point the new node's next to the current head
        new_node.next = self.head
        print(f"  [POINTER] New node (value: {data}) now points to current head (value: {self.head.data if self.head else 'None'})")
        
        # Make the new node the head
        self.head = new_node
        print(f"  [HEAD UPDATE] Head is now Node({data})")

    def append(self, data):
        """Appends a new node to the end of the list (Slow O(N))."""
        print(f"\n[APPEND] Appending value: {data}")
        new_node = Node(data)
        
        # If the list is empty, make this the head
        if not self.head:
            self.head = new_node
            print(f"  [HEAD UPDATE] List was empty. Head is now Node({data})")
            return

        # Walk to the end of the list
        current = self.head
        steps = 0
        while current.next:
            steps += 1
            print(f"  [TRAVERSE] Step {steps}: Passed Node({current.data}), moving to next node.")
            current = current.next

        # Link the last node's next to our new node
        print(f"  [TRAVERSE DONE] Reached tail node: Node({current.data})")
        current.next = new_node
        print(f"  [POINTER] Tail Node({current.data}).next set to new Node({data})")

    def delete_value(self, target_val):
        """Deletes the first node containing target_val."""
        print(f"\n[DELETE] Attempting to delete value: {target_val}")
        
        if not self.head:
            print("  ❌ List is empty. Nothing to delete.")
            return False

        # Case 1: The head node holds the target value
        if self.head.data == target_val:
            print(f"  [DELETE HEAD] Target value found at Head. Pointing Head to Node({self.head.next.data if self.head.next else 'None'})")
            self.head = self.head.next
            return True

        # Case 2: Target is in the middle or end
        current = self.head
        prev = None
        steps = 0
        while current and current.data != target_val:
            steps += 1
            print(f"  [SEARCH] Step {steps}: Checking Node({current.data}) -> Not target.")
            prev = current
            current = current.next

        # If target was found
        if current:
            print(f"  🎉 Found target Node({current.data}) after {steps} steps. Re-routing pointers...")
            print(f"  [POINTER] Changing Node({prev.data}).next from Node({current.data}) to Node({current.next.data if current.next else 'None'})")
            prev.next = current.next
            return True
            
        print(f"  ❌ Value {target_val} not found in the list.")
        return False

    def print_list(self):
        """Prints the visual chain of nodes."""
        current = self.head
        chain = []
        while current:
            chain.append(str(current.data))
            current = current.next
        chain.append("None")
        print("Linked List visualization: " + " -> ".join(chain))


# --- Testing our Linked List ---
sll = SinglyLinkedList()
sll.print_list()

sll.insert_at_head(20)
sll.insert_at_head(10)
sll.print_list()

sll.append(30)
sll.print_list()

sll.delete_value(20)
sll.print_list()
```

***

## 🔍 Step-by-Step Pointer Shift Dry Run

Let's look at what happens when deleting `20` from the list `[10 -> 20 -> 30]`. 
* We need to skip `20` by pointing `10.next` directly to `30` (`20.next`).

```
  Step 1: Locate Target Node
  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
  │  Data: 10    │      │  Data: 20    │      │  Data: 30    │
  │  Next: 0x450 ├─────►│  Next: 0x880 ├─────►│  Next: None  │
  └──────────────┘      └──────────────┘      └──────────────┘
      [prev]               [current]             [current.next]
        
  Step 2: Update Pointer (prev.next = current.next)
  ┌──────────────┐                             ┌──────────────┐
  │  Data: 10    │                             │  Data: 30    │
  │  Next: 0x880 ├────────────────────────────►│  Next: None  │
  └──────────────┘                             └──────────────┘
      [prev]                                     [current.next]
                       (Node 20 is orphaned!)
```

***

## 📈 Complexity & Big O Analysis

| Operation | Time Complexity | Space Complexity | Why? |
| :--- | :---: | :---: | :--- |
| **Access (Find by index)** | $O(N)$ | $O(1)$ | Must iterate step-by-step from the head. |
| **Search (Find by value)** | $O(N)$ | $O(1)$ | Must scan nodes one-by-one until match. |
| **Insert at Start (Head)**| $O(1)$ | $O(1)$ | Just adjust new node's next pointer and head. |
| **Insert at End (Tail)** | $O(N)$ | $O(1)$ | Must traverse all nodes to find the end first. |
| **Delete from Start** | $O(1)$ | $O(1)$ | Just shift head pointer to head.next. |
| **Delete in Middle** | $O(N)$ | $O(1)$ | Requires O(N) search steps, but pointer swap is O(1). |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 206: Reverse Linked List (Easy/Medium)
> **Problem:** Given the head of a singly linked list, reverse the list, and return the new head.

#### The Three-Pointer In-Place Technique (O(N) time, O(1) space)
We walk through the list maintaining three pointers: `prev` (nodes we already reversed), `current` (node we are reversing now), and `next_node` (to save the rest of the list before we sever the link).

```python
def reverse_list(head):
    """
    Reverses a linked list in-place and returns the new head.
    """
    print("=== Reversing Linked List ===")
    prev = None
    current = head
    steps = 0
    
    while current:
        steps += 1
        # 1. Save the next node (so we don't lose the rest of the list)
        next_node = current.next
        
        # 2. Reverse the link (point backward!)
        print(f"Step {steps}: Node({current.data}) currently points to Node({next_node.data if next_node else 'None'})")
        current.next = prev
        print(f"  [REVERSED] Node({current.data}) now points backward to Node({prev.data if prev else 'None'})")
        
        # 3. Move pointers forward
        prev = current
        current = next_node
        
    print(f"🎉 Reverse Complete! New Head is Node({prev.data if prev else 'None'})\n")
    return prev

# Create helper to test
h = Node(1)
h.next = Node(2)
h.next.next = Node(3)
reverse_list(h)
```

---

### LeetCode 141: Linked List Cycle (Easy/Medium)
> **Problem:** Given the head of a linked list, determine if the list has a cycle (loop) in it.

#### Floyd's Cycle Detection / Tortoise & Hare Algorithm (O(N) time, O(1) space)
Imagine two runners on a circular track. One runs twice as fast as the other. If there is a loop, the fast runner (Hare) will eventually lap and meet the slow runner (Tortoise). If there is no loop, the fast runner will hit the end of the track (`None`).

```python
def has_cycle(head):
    """
    Returns True if a cycle exists in the linked list using two pointers.
    """
    print("=== Checking for Linked List Cycle ===")
    slow = head
    fast = head
    steps = 0
    
    while fast and fast.next:
        steps += 1
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        print(f"Step {steps}: Slow is at Node({slow.data if slow else 'None'}), Fast is at Node({fast.data if fast else 'None'})")
        
        # If they meet, there is a cycle!
        if slow == fast:
            print("⚠️ [CYCLE DETECTED] Slow and Fast pointers met! The list contains a loop.\n")
            return True
            
    print("🎉 [NO CYCLE] Fast reached the end of the list. No loop detected.\n")
    return False

# Test cycle detection
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
# Create a cycle: 3 -> 2
node3.next = node2
has_cycle(node1)
```

***

## 🤖 Connection to Machine Learning & AI: Deep Learning Memory Allocator

How do linked lists keep GPUs running in AI?
* **GPU Memory (VRAM) Fragmentation:** Deep learning models load massive activation tensors, parameters, and gradients into GPU VRAM during backpropagation.
* **The Problem:** Tensors are allocated and deallocated constantly. This leaves "holes" of empty memory scattered across the GPU, which can lead to Out of Memory (OOM) errors even if the total free memory is sufficient.
* **The Solution:** Frameworks like **PyTorch** use a caching memory allocator that tracks free blocks of memory using a **Doubly Linked List**.
* When a tensor is deleted, its memory block is marked free and merged with adjacent free blocks in the linked list instantly ($O(1)$ operations), preventing VRAM fragmentation and ensuring there is always contiguous space for large neural network batches!
