# Chapter 11: Binary Trees & BSTs 🚀

Up until now, we have studied linear data structures where elements follow one after another in a straight line (Arrays, Linked Lists, Stacks, Queues). But the real world is often hierarchical.

Think of folders on your hard drive, organizational charts in a company, or a family ancestry tree. These are represented as **Trees**.

Today, we will learn about the **Binary Tree** and the highly efficient **Binary Search Tree (BST)**, understand how to traverse them, and build one in Python.

***

## 💡 Real-World Analogy: The Org Chart & The Decision Flow

Think of these two models:

### 1. The Corporate Org Chart (Binary Tree)
* The **CEO** is at the very top. This is the **Root** of the tree.
* The CEO has two direct managers: the VP of Engineering (Left Child) and the VP of Sales (Right Child).
* Each manager can have at most two direct reports, and so on.
* The interns at the bottom of the chart who manage nobody are the **Leaves**.

### 2. Choose-Your-Own-Adventure (BST Property)
Imagine playing a guessing game where you want to find a number.
* You start at a signpost showing **50**.
* Next to the signpost are two paths:
  * Left path: Labelled *"Smaller numbers (< 50)"*.
  * Right path: Labelled *"Larger numbers (> 50)"*.
* If your target is 30, you go left. If it's 75, you go right.
* This ordering rule is the **Binary Search Tree Property**!

***

## 📌 In Simple Terms: Tree Anatomy & BST Rules

* **Root:** The top node of the tree. There is only one root.
* **Parent / Child:** A node pointing directly to nodes below it is their Parent. The nodes below are its Children.
* **Leaf Node:** A node that has no children (both left and right pointers are `None`).
* **Binary Tree:** A tree where every node has **at most 2 children** (Left and Right).
* **Binary Search Tree (BST):** A binary tree that enforces this sorting rule:
  $$\text{All Left Subtree values} < \text{Parent Node value} < \text{All Right Subtree values}$$
  Because of this rule, searching a balanced BST takes only **$O(\log N)$ time**!

***

## 🧠 Memory Model: A Binary Search Tree

Here is a BST containing values `[8, 3, 10, 1, 6, 14]`. Notice how smaller numbers are always on the left, and larger numbers are always on the right:

```
                      [8]  ◄── ROOT
                     /   \
                  [3]     [10]
                 /   \       \
               [1]   [6]     [14] ◄── LEAF
```

***

## 🧠 Python Implementation: BST with Decision Tracing

Let's implement a `BSTNode` and a `BinarySearchTree` in Python. We will add tracing prints showing the decisions made at each branch.

```python
class BSTNode:
    def __init__(self, key):
        """A single node in a BST with left and right child pointers."""
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        print("[INIT] Created empty Binary Search Tree.")

    def insert(self, key):
        """Inserts a key into the BST."""
        print(f"\n[INSERT] Request to insert: {key}")
        if self.root is None:
            self.root = BSTNode(key)
            print(f"  [ROOT SET] Set {key} as Root.")
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper to recursively find the correct insertion spot."""
        # Case 1: Go Left
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = BSTNode(key)
                print(f"  [INSERT LEFT] Placed Node({key}) as Left child of Node({current_node.key})")
            else:
                print(f"  [DECISION] {key} < {current_node.key}. Moving Left to Node({current_node.left.key})")
                self._insert_recursive(current_node.left, key)
                
        # Case 2: Go Right
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = BSTNode(key)
                print(f"  [INSERT RIGHT] Placed Node({key}) as Right child of Node({current_node.key})")
            else:
                print(f"  [DECISION] {key} > {current_node.key}. Moving Right to Node({current_node.right.key})")
                self._insert_recursive(current_node.right, key)
        else:
            print(f"  [DUPLICATE] Key {key} already exists. Skipping insertion.")

    def search(self, target):
        """Searches for a target value in the tree."""
        print(f"\n[SEARCH] Looking for: {target}")
        return self._search_recursive(self.root, target, step=1)

    def _search_recursive(self, current_node, target, step):
        if current_node is None:
            print(f"  Step {step}: Reached None. Target {target} is NOT in the tree.")
            return False
            
        print(f"  Step {step}: Comparing target {target} with Node({current_node.key})")
        
        if current_node.key == target:
            print(f"  🎉 Found target '{target}' at Step {step}!")
            return True
        elif target < current_node.key:
            print(f"    Target {target} < {current_node.key}. Routing Left.")
            return self._search_recursive(current_node.left, target, step + 1)
        else:
            print(f"    Target {target} > {current_node.key}. Routing Right.")
            return self._search_recursive(current_node.right, target, step + 1)

    def in_order_traversal(self):
        """Traverses and prints BST keys in sorted order."""
        result = []
        self._in_order_recursive(self.root, result)
        print(f"\n[TRAVERSAL] In-Order Sorted Result: {result}")
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)  # Left
            result.append(node.key)                       # Root
            self._in_order_recursive(node.right, result) # Right


# --- Test our BST ---
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)

# Traversal prints keys in ascending sorted order!
bst.in_order_traversal()

# Search queries
bst.search(6)
bst.search(12) # Missing
```

***

## 🔍 Depth-First Search (DFS) Traversal Methods

There are three classic ways to walk recursively through a tree's nodes:

```
                      [A]
                     /   \
                  [B]     [C]
```

1. **Pre-Order (Root -> Left -> Right):** Good for copying or cloning trees.
   * Order for tree above: `A -> B -> C`
2. **In-Order (Left -> Root -> Right):** **Crucial rule:** In a BST, In-Order traversal prints numbers in **ascending sorted order**!
   * Order for tree above: `B -> A -> C`
3. **Post-Order (Left -> Right -> Root):** Good for deleting nodes (you delete children before their parent).
   * Order for tree above: `B -> C -> A`

***

## 📈 Complexity & Big O Analysis

| Operation | Best / Average Case (Balanced) | Worst Case (Skewed) | Why? |
| :--- | :---: | :---: | :--- |
| **Search** | $O(\log N)$ | $O(N)$ | Skewed tree degrades to a Linked List chain. |
| **Insertion** | $O(\log N)$ | $O(N)$ | Worst case requires traversing all $N$ nodes. |
| **Deletion** | $O(\log N)$ | $O(N)$ | Requires locating node first, then linking children. |

* **The Skewed Tree Hazard:** If you insert sorted numbers `[1, 2, 3, 4]`, the BST becomes a straight line: `1 -> 2 -> 3 -> 4`. All operations become $O(N)$!
* **The Solution:** Self-Balancing Trees (AVL Trees, Red-Black Trees). They automatically rotate their nodes during insertions to stay balanced and guarantee $O(\log N)$ speeds.

***

## 🎓 Interview & LeetCode Applications

### LeetCode 226: Invert Binary Tree (Easy/Medium)
> **Problem:** Given the root of a binary tree, invert the tree (mirror swap all left and right children) and return its root.

#### The Recursive Mirror Solution (O(N) time, O(H) space)
We swap the left and right pointers of the current node, then recursively invert the left and right subtrees.

```python
def invert_tree(root):
    """
    Inverts a binary tree in-place recursively.
    """
    if root is None:
        return None
        
    print(f"[SWAP] Swapping children of Node({root.key})")
    # Swap pointers
    root.left, root.right = root.right, root.left
    
    # Recursively swap child branches
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# Helper to verify with mock nodes
root_node = BSTNode(4)
root_node.left = BSTNode(2)
root_node.right = BSTNode(7)
invert_tree(root_node)
```

***

## 🤖 Connection to Machine Learning & AI: Random Forest Split Paths

How do tree structures form the core of classical Machine Learning?
* **Decision Trees:** ML models like **XGBoost** and **Random Forests** are constructed as hierarchies of binary decisions.
* **The Split Nodes:** Each node in a trained ML Decision Tree contains a split condition (e.g. `If feature_3 < 0.5`). The left child represents "True", the right child represents "False".
* **Evaluating Inference:** When classifying a new data vector:
  1. The program starts at the root node of the decision tree.
  2. It evaluates the split condition using the input data.
  3. If True, it routes to the Left child; if False, to the Right child.
  4. It recursively routes down the tree until reaching a Leaf node, which outputs the classification label.
* Because the decision path is a balanced binary tree, the classification model can evaluate complex decisions on tabular data in just **$O(D)$ steps** (where $D$ is the depth of the tree, typically 4 to 10 layers), making it incredibly fast to run on web servers!
