# Chapter 13: Graphs & Graph Traversals 🚀

So far, we have studied trees where data flows downwards in a strict parent-child structure with no loops. But what if connections are more complex?

Think of Facebook friendships, flights between cities, or roads connecting towns. Here, any node can connect to any other node, forming loops and networks.

In computer science, this is a **Graph**. Today, we will study graph representations, learn how to traverse them using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**, and write tracing implementations in Python.

***

## 💡 Real-World Analogy: Social Networks & Flight Maps

To understand graphs, look at these daily networks:

### 1. The Friendship Network (Undirected Graph)
* Imagine users on a social media app. Each user is a node (called a **Vertex**).
* If two users are friends, there is a connection line between them (called an **Edge**).
* Friendship is two-way: if Arham is friends with Bat, Bat is friends with Arham. This is an **Undirected Graph**.

### 2. Airline Flights (Directed & Weighted Graph)
* Cities are Vertices. Flight paths are Edges.
* Some flights are one-way: you can fly from Paris to Tokyo, but not Tokyo to Paris. This is a **Directed Graph**.
* Each flight has a cost or mileage (e.g. 5,000 miles). This number is a **Weight**. This is a **Weighted Graph**.

***

## 📌 In Simple Terms: Vertices, Edges & Representations

* **Vertex (Plural: Vertices):** A node in the graph.
* **Edge:** A connection between two vertices.
* **Adjacency List:** A way to represent a graph in memory using a dictionary/hash map where:
  $$\text{Key} \rightarrow \text{List of connected neighbor vertices}$$
  * *Why we use it:* Very memory efficient for sparse graphs (graphs with few connections).
* **Adjacency Matrix:** A 2D grid/table of size $V \times V$ where a `1` at row $A$ column $B$ means $A$ is connected to $B$, and `0` means no connection.
  * *Why we use it:* Fast for dense graphs (many connections).

***

## 🧠 Memory Model: Adjacency List in RAM

Let's represent a triangle graph `A - B - C` using an Adjacency List:
* `A` is connected to `B` and `C`.
* `B` is connected to `A` and `C`.
* `C` is connected to `A` and `B`.

```
        ADJACENCY LIST REPRESENTATION (DICT OF LISTS)
   ┌────────────────────────────────────────────────────────┐
   │  {                                                     │
   │    "A": [ "B", "C" ],  ──► Head of list -> B -> C      │
   │    "B": [ "A", "C" ],  ──► Head of list -> A -> C      │
   │    "C": [ "A", "B" ]   ──► Head of list -> A -> B      │
   │  }                                                     │
   └────────────────────────────────────────────────────────┘
```

***

## 🧠 Python Implementation: BFS & DFS Tracing

Let's build a `Graph` class using an Adjacency List, and implement BFS (which uses a queue) and DFS (which uses recursion/stack) with step-by-step logs.

```python
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
        print("[INIT] Created empty Graph.")

    def add_vertex(self, vertex):
        """Adds a vertex (node) to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            print(f"[VERTEX] Added vertex: '{vertex}'")

    def add_edge(self, v1, v2):
        """Adds an undirected edge between v1 and v2."""
        # Ensure vertices exist first
        self.add_vertex(v1)
        self.add_vertex(v2)
        
        # Connect them both ways
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        print(f"[EDGE] Connected '{v1}' <-> '{v2}'")

    def bfs(self, start_node):
        """
        Traverses the graph level-by-level using a Queue (BFS).
        Finds the shortest path in unweighted graphs!
        """
        print(f"\n=== Starting BFS Traversal from '{start_node}' ===")
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        steps = 0
        
        while queue:
            steps += 1
            # Pop the oldest node from the front of the queue
            current = queue.popleft()
            print(f"Step {steps}: Visiting '{current}'. Queue State: {list(queue)}")
            
            # Look at all neighbors
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    print(f"  [QUEUE ADD] Neighbor '{neighbor}' not visited. Enqueuing.")
                    
        print(f"🎉 BFS finished. Visited all nodes in {steps} steps.\n")

    def dfs(self, start_node):
        """
        Traverses the graph by exploring as deep as possible before backtracking (DFS).
        Uses recursion (implicit stack).
        """
        print(f"\n=== Starting DFS Traversal from '{start_node}' ===")
        visited = set()
        self._dfs_recursive(start_node, visited, depth=0)
        print("🎉 DFS Finished.\n")

    def _dfs_recursive(self, node, visited, depth):
        indent = "  " * depth
        print(f"{indent}▶️ [VISIT] DFS visiting '{node}'")
        visited.add(node)
        
        # Loop through neighbors
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                print(f"{indent}  Neighbor '{neighbor}' is unvisited. Diving deeper...")
                self._dfs_recursive(neighbor, visited, depth + 1)
            else:
                print(f"{indent}  Neighbor '{neighbor}' already visited. Skipping.")
        
        print(f"{indent}◀️ [BACKTRACK] Finished checking neighbors of '{node}'. Returning up.")


# --- Test our Graph ---
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

# Run BFS (Should explore level 1: B, C, then level 2: D, E)
g.bfs("A")

# Run DFS (Should dive deep: A -> B -> D -> backtracking...)
g.dfs("A")
```

***

## 🔍 BFS vs. DFS: The Traversal Trace Table

Let's trace how BFS and DFS visit nodes on the graph:
```
           [A]
          /   \
        [B]   [C]
         |     |
        [D]   [E]
```

| Traversal | Queue/Stack State Timeline | Node Visited Order | Why? |
| :--- | :--- | :--- | :--- |
| **BFS** | `['A']` $\rightarrow$ `['B', 'C']` $\rightarrow$ `['C', 'D']` $\rightarrow$ `['D', 'E']` $\rightarrow$ `['E']` $\rightarrow$ `[]` | `A -> B -> C -> D -> E` | BFS uses a queue to explore all neighbors of `A` first, then neighbors of `B`, etc. |
| **DFS** | Stack Frames: `A` $\rightarrow$ `B` $\rightarrow$ `D` $\rightarrow$ backtrack to `A` $\rightarrow$ `C` $\rightarrow$ `E` $\rightarrow$ `[]` | `A -> B -> D -> C -> E` | DFS recursively dives down the first branch (`A -> B -> D`) completely before backtrack-searching `C`. |

***

## 📈 Complexity & Big O Analysis

| Operation / Search | Adjacency List | Adjacency Matrix | Space Complexity | Why? |
| :--- | :---: | :---: | :---: | :--- |
| **BFS** | $O(V + E)$ | $O(V^2)$ | $O(V)$ | Must visit every vertex and edge. Queue holds at most $V$ vertices. |
| **DFS** | $O(V + E)$ | $O(V^2)$ | $O(V)$ | Recursion stack depth goes up to $V$ frames. |
| **Space Required** | $O(V + E)$ | $O(V^2)$ | - | Matrix always uses $V^2$ slots. List only stores actual links. |

***

## 🎓 Interview & LeetCode Applications

### LeetCode 200: Number of Islands (Medium)
> **Problem:** Given an $M \times N$ 2D grid map of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

#### The 2D Grid DFS Traversal Approach (O(M * N) time, O(M * N) space)
We scan the grid. When we hit `'1'` (land), we trigger a DFS traversal. The DFS visits all connected land cells (up, down, left, right) and marks them as `'0'` (sunk/visited) so we don't count them again. This count represents our islands.

```python
def num_islands(grid):
    """
    Counts islands in a 2D grid using DFS traversal.
    """
    if not grid: return 0
    
    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    print(f"=== Counting Islands on {rows}x{cols} grid ===")

    def dfs_sink(r, c):
        # Base Case: Out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
            
        # Sink the land cell (mark visited)
        grid[r][c] = '0'
        
        # Recursively sink all 4 adjacent directions
        dfs_sink(r + 1, c) # Down
        dfs_sink(r - 1, c) # Up
        dfs_sink(r, c + 1) # Right
        dfs_sink(r, c - 1) # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                print(f"  🎉 Found Island #{islands} starting at cell ({r}, {c}). Sinking connected lands...")
                dfs_sink(r, c)
                
    print(f"🎉 Final Island Count: {islands}\n")
    return islands

# Test
mock_grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
num_islands(mock_grid)
```

***

## 🤖 Connection to Machine Learning & AI: RAG Knowledge Graphs

How do graphs power modern Generative AI models?
* **LLM Fact Limitations:** Large Language Models (LLMs) often hallucinate facts because they only generate words based on statistics, not a structured database.
* **Graph RAG (Retrieval-Augmented Generation):** To make LLMs 100% accurate, companies use **Knowledge Graphs**.
  * Concepts are Vertices (e.g. `"Diabetes"`, `"Insulin"`, `"Pancreas"`).
  * Relationships are Edges (e.g. `"Pancreas" -- produces --> "Insulin"`).
* **The Retrieval Step:** When you ask the LLM: *"How is pancreas connected to insulin?"*, the system runs a graph query (BFS/DFS traversal) to find the path connecting `"Pancreas"` and `"Insulin"`.
* It extracts the exact facts along the edges and feeds them to the LLM as context.
* This ensures the LLM's answers are anchored in verified database facts rather than statistical guesswork!
