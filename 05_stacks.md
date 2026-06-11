# Chapter 05: Stacks (LIFO Principle) 🚀

Have you ever cleaned up a tall pile of dinner plates in a cafeteria? You wash the top plate, dry it, and set it down. You never pull a plate straight out from the bottom of the stack—otherwise, the whole pile would collapse!

This is the **LIFO (Last In, First Out)** principle, and it is the foundation of the **Stack** data structure. Today, we will learn how stacks function, build them using both arrays and linked lists, and discover how they manage your code's execution.

***

## 💡 Real-World Analogy: The Plate Pile & The Undo Button

Think of these common examples of stacks:

### 1. Cafeteria Plate Stack
* **Adding plates:** You place a new plate on the top of the pile. This is called a **Push**.
* **Removing plates:** You take the top plate off the pile. This is called a **Pop**.
* **Peeking:** You look at the color of the top plate without removing it. This is called a **Peek**.
* **Rules:** You cannot touch the plates at the bottom without removing all the plates above them first.

### 2. The Undo Log (Ctrl + Z)
* As you type in a document:
  * Type "Hello" -> Pushed to undo stack.
  * Type "World" -> Pushed to undo stack.
* When you press **Undo (Ctrl + Z)**, the computer pops the most recent action ("World") off the stack and reverses it. Last action typed = First action undone!

***

## 📌 In Simple Terms: The LIFO Rule

* **LIFO (Last In, First Out):** The last element added to the stack is the very first one to be removed.
* **Push:** Add an item to the top of the stack.
* **Pop:** Remove the top item from the stack.
* **Peek / Top:** Look at the top item without removing it.
* **Underflow:** An error that occurs when you try to `pop` an item from an empty stack.

***

## 🧠 Memory Model: Stack Growth in RAM

In memory, a stack can be implemented using an array or a linked list. Let's look at a stack containing `[10, 20, 30]` (where 30 is at the top).

```
        VISUAL STACK MODEL (GROWING UPWARD)
      
      ┌──────────────┐
      │  Value: 30   │  ◄── TOP OF STACK (Active element)
      ├──────────────┤
      │  Value: 20   │
      ├──────────────┤
      │  Value: 10   │  ◄── BOTTOM OF STACK
      └──────────────┘
       
      Operations happen ONLY at the TOP!
      Push: Drops a new plate on top of 30.
      Pop: Lifts 30 off the pile, revealing 20 as the new TOP.
```

***

## 🧠 Python Implementation: Two Ways to Build a Stack

We can build a stack using a simple Python list (Dynamic Array) or a Singly Linked List. Let's implement both with step-by-step trace statements.

### 1. Array-Backed Stack (Simple & Fast)

```python
class ArrayStack:
    def __init__(self):
        self.stack = []
        print("[INIT] Created empty ArrayStack.")

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        print(f"\n[PUSH] Adding '{item}' to the stack.")
        self.stack.append(item)
        print(f"  [DEBUG] Stack state: {self.stack} <- TOP")

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack (Stack Underflow)!")
        
        item = self.stack.pop()
        print(f"\n[POP] Removed '{item}' from the top.")
        print(f"  [DEBUG] Stack state: {self.stack} <- TOP")
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Test Array Stack
as_stack = ArrayStack()
as_stack.push(10)
as_stack.push(20)
as_stack.push(30)
as_stack.pop()
print(f"Top element: {as_stack.peek()}")
```

---

### 2. Linked List-Backed Stack (Dynamic Memory Allocation)

This approach avoids array resizing because each element is a Node. We push/pop at the **Head** of the list since head operations are always $O(1)$.

```python
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0
        print("[INIT] Created empty LinkedListStack.")

    def is_empty(self):
        return self.top is None

    def push(self, data):
        print(f"\n[PUSH] Creating Node({data}) and pushing to top.")
        new_node = StackNode(data)
        
        # Point new node to the current top
        new_node.next = self.top
        # Update top pointer
        self.top = new_node
        self._size += 1
        print(f"  [POINTER] Top node is now Node({data}). Next is Node({new_node.next.data if new_node.next else 'None'})")

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack (Stack Underflow)!")
        
        popped_node = self.top
        # Shift top pointer to the next node
        self.top = self.top.next
        self._size -= 1
        
        print(f"\n[POP] Removed top Node({popped_node.data}).")
        print(f"  [DEBUG] New top is Node({self.top.data if self.top else 'None'})")
        return popped_node.data

    def peek(self):
        return self.top.data if self.top else None

    def size(self):
        return self._size


# Test Linked List Stack
lls = LinkedListStack()
lls.push("Plate A")
lls.push("Plate B")
lls.pop()
```

***

## 🔍 Step-by-Step Parentheses Matching Dry Run

Stacks are perfect for checking if brackets are matched correctly (e.g., `{[()]}`).
* **Rule:** If we see an opening bracket (`(`, `[`, `{`), we **push** it to the stack.
* If we see a closing bracket (`)`, `]`, `}`), we **pop** the top of the stack and check if they make a matching pair.
* If they don't match, or the stack is empty when we try to pop, the brackets are invalid!

Let's dry-run `"{[()]}"`:

| Char | Action | Stack State (Bottom -> Top) | Match Checked? | Result |
| :---: | :--- | :--- | :---: | :--- |
| **{** | Push | `['{']` | - | Valid so far |
| **[** | Push | `['{', '[']` | - | Valid so far |
| **(** | Push | `['{', '[', '(']` | - | Valid so far |
| **)** | Pop and Compare | `['{', '[']` | `'('` matches `')'` | Valid so far |
| **]** | Pop and Compare | `['{']` | `'['` matches `']'` | Valid so far |
| **}** | Pop and Compare | `[]` (Empty) | `'{'` matches `'}'` | Valid so far |
| **End** | Check if stack empty | `[]` (Empty) | - | **Success! Parentheses Balanced.** |

***

## 📈 Complexity & Big O Analysis

| Operation | Time Complexity (Array Stack) | Time Complexity (Linked List Stack) | Space Complexity | Why? |
| :--- | :---: | :---: | :---: | :--- |
| **Push** | $O(1)$ (Amortized) | $O(1)$ | $O(1)$ | No searching, element dropped straight on top. |
| **Pop** | $O(1)$ | $O(1)$ | $O(1)$ | Directly remove the top item, no index shifting. |
| **Peek** | $O(1)$ | $O(1)$ | $O(1)$ | Instant lookup of the top index/node address. |
| **Search** | $O(N)$ | $O(N)$ | $O(1)$ | Must scan through elements to find target. |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 20: Valid Parentheses (Easy)
> **Problem:** Given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.

```python
def is_valid_parentheses(s):
    """
    Checks if brackets are correctly closed and matched using a Stack.
    """
    print(f"=== Validating Parentheses for '{s}' ===")
    stack = []
    # Map closing brackets to their matching opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # We found a closing bracket. Pop from stack (or use dummy if empty)
            top_element = stack.pop() if stack else '#'
            print(f"  Found closing '{char}'. Popped '{top_element}' from stack.")
            
            # Check if popped bracket matches current closing bracket
            if mapping[char] != top_element:
                print(f"  ❌ Mismatch! '{mapping[char]}' does not match '{top_element}'")
                return False
        else:
            # It's an opening bracket, push it
            stack.append(char)
            print(f"  Found opening '{char}'. Pushed to stack. Current stack: {stack}")
            
    # If the stack is empty, all brackets were matched successfully
    is_valid = len(stack) == 0
    print(f"🎉 Validation result: {is_valid}\n")
    return is_valid

# Test cases
is_valid_parentheses("{[()]}")
is_valid_parentheses("{[(])}")
```

---

### LeetCode 155: Min Stack (Medium)
> **Problem:** Design a stack that supports push, pop, top, and retrieving the minimum element in $O(1)$ time.

#### The Dual-Stack Technique
To do this in $O(1)$, we use a second stack called the `min_stack`. It keeps track of the minimum value seen *at each level* of the main stack.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        print("[INIT] MinStack initialized.")

    def push(self, val):
        self.stack.append(val)
        # Push the new minimum onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        print(f"[PUSH] Added: {val}. Current Min: {self.getMin()}")

    def pop(self):
        if not self.stack:
            return
        val = self.stack.pop()
        self.min_stack.pop()
        print(f"[POP] Removed top element. Current Min: {self.getMin() if self.stack else 'None'}")
        return val

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None


# Test Min Stack
m_stack = MinStack()
m_stack.push(30)
m_stack.push(10)
m_stack.push(20)
m_stack.push(5)
m_stack.pop()
```

***

## 🤖 Connection to Machine Learning & AI: Neural Network Activation Stacks

How do stacks run deep neural networks during training?
* **Training Flow:** Training a neural network consists of two passes:
  1. **Forward Pass:** The input data runs through the network layers ($L_1 \rightarrow L_2 \rightarrow L_3$) to compute a prediction.
  2. **Backward Pass (Backpropagation):** The prediction error is pushed backward ($L_3 \rightarrow L_2 \rightarrow L_1$) to update layer weights using gradients.
* **The Activation Stack:** During the forward pass, each layer computes intermediate numbers called **Activations**. These activations are needed during the backward pass to calculate gradients.
* **Why it's a Stack:** Because backpropagation flows in the **exact reverse order** of the forward pass, activations are pushed onto an execution stack layer-by-layer during the forward pass:
  * `[Push L1 Activations] -> [Push L2 Activations] -> [Push L3 Activations]`
* During backpropagation, the gradients are calculated by popping these activations off in LIFO order:
  * `[Pop L3 Activations] -> [Pop L2 Activations] -> [Pop L1 Activations]`
* This is why training models requires so much GPU memory—it must keep the entire stack of layer activations in memory until the backward pass completes!
