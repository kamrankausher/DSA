# Data Structures & Algorithms (DSA) — Zero to Advanced 🚀

Welcome to the ultimate Data Structures and Algorithms (DSA) notebook repository! This repository is designed to build a rock-solid foundation in DSA, tailored for software engineering interviews, advanced programming, and applications in Data Science, Machine Learning, and AI.

Every concept in this repository is designed to be **10th-grade accessible**—meaning we explain complex concepts using simple real-world analogies, intuitive explanations, visual ASCII memory models, and trace tables before showing clean, production-grade Python code.

---

## 📚 Table of Contents

| Chapter | Topic | Analogies & Key Concepts | Status |
| :---: | :--- | :--- | :---: |
| **00** | [Basics of Algorithms & Complexity (Big O)](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/00_complexity_analysis.md) | Phonebook search, step counting, Time & Space complexities | ✅ Completed |
| **01** | [Arrays & Dynamic Arrays](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/01_arrays.md) | Egg cartons, memory blocks, resizing, Python list internals | ✅ Completed |
| **02** | [Recursion & the Call Stack](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/02_recursion.md) | Two mirrors, stack of books, base case, stack overflow | ✅ Completed |
| **03** | [Singly Linked Lists](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/03_singly_linked_lists.md) | Scavenger hunt clues, nodes, pointers, constant-time insertions | ✅ Completed |
| **04** | [Doubly & Circular Linked Lists](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/04_doubly_linked_lists.md) | Browser back/forward history, circular music playlist loop | ✅ Completed |
| **05** | [Stacks (LIFO Principle)](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/05_stacks.md) | Pile of cafeteria plates, undo/redo logs, call stacks in Python | ✅ Completed |
| **06** | [Queues & Deques (FIFO Principle)](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/06_queues.md) | Movie ticket counter line, printer queues, buffers, circular queues | ✅ Completed |
| **07** | [Basic Sorting (Bubble, Selection, Insertion)](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/07_basic_sorting.md) | Sorting cards in hand, bubble rising, shifting items | ✅ Completed |
| **08** | [Advanced Sorting (Merge, Quick, Heap)](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/08_advanced_sorting.md) | Divide & conquer, splitting stacks, pivot partitioning | ✅ Completed |
| **09** | [Searching & Binary Search](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/09_binary_search.md) | Guessing game (higher/lower), dictionary search, O(log n) efficiency | ✅ Completed |
| **10** | [Hash Tables & Maps](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/10_hash_tables.md) | Library classification system, indexing keys, collision resolution | ✅ Completed |
| **11** | [Binary Trees & Binary Search Trees (BST)](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/11_binary_trees.md) | Family tree, decision flows, BST properties, DFS & BFS traversals | ✅ Completed |
| **12** | [Heaps & Priority Queues](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/12_heaps.md) | Emergency room triage priority, Min/Max heaps, representing tree in array | ✅ Completed |
| **13** | [Graphs & Graph Traversals](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/13_graphs.md) | Social network connections, flights between cities, BFS, DFS, Dijkstra | ✅ Completed |
| **14** | [Dynamic Programming & Greedy Algorithms](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/14_dynamic_programming.md) | Saving changes at checkpoint, memoization vs tabulation, knapsack | ✅ Completed |

---

## 🎨 Pedagogical Pillars: What makes these notes special?

1. **Zero Jargon Zone:** Every technical term is instantly demystified with a physical, touchable analogy.
2. **Visual Memory Models:** Clean ASCII diagrams showing what happens inside variables, pointers, and memory blocks (heap/stack).
3. **Interactive Debug Tracing:** Code implementations don't just execute silently; they print step-by-step trace statements showing exactly what changes at each step.
4. **Trace Tables:** Dry-running complex loops or recursions on paper, mapping variable values dynamically.
5. **AI/ML Connection:** Connecting abstract computer science concepts directly to practical AI, Vector Embeddings, Neural Network operations, and Machine Learning models.

---

## 🛠️ How to Generate and Compile Your Notes (Step-by-Step)

Because writing raw Jupyter Notebook JSON directly is highly error-prone for AI models (which can get cut off or write invalid JSON strings), we use a hybrid markdown-to-notebook approach. You write or generate notes in **simple markdown** (a `.md` file), and a Python compiler script automatically turns it into a fully functional Jupyter Notebook (`.ipynb`).

### Step 1: Open the Generator Prompt
Go to [dsa_notes_generator_prompt.md](file:///c:/Study%20material/DATA%20SCIENCE/DS%20with%20sheryians%20Ai%20school/DSA/dsa_notes_generator_prompt.md) and copy the Master Prompt content.

### Step 2: Prompt your AI of Choice
1. Paste the prompt into an LLM (e.g., Gemini 1.5 Pro, Claude 3.5 Sonnet, or ChatGPT).
2. Set the placeholder at the end of the prompt to the chapter you want to build (e.g., `Chapter 03: Singly Linked Lists`).
3. Hit enter. The AI will output a clean, complete markdown document containing explanations, ASCII models, tables, and Python code blocks.

### Step 3: Save the Markdown Draft
Copy the AI's markdown response and save it as a `.md` file in this directory (e.g., save it as `03_singly_linked_lists.md`).

### Step 4: Run the Compiler Script
Open your terminal inside this directory and run:
```bash
python markdown_to_ipynb.py
```
This script will look at all your draft `.md` files (ignoring README and prompt files) and instantly compile them into beautifully structured, ready-to-run Jupyter Notebooks (`.ipynb`)!

To convert a specific file only, you can run:
```bash
python markdown_to_ipynb.py 03_singly_linked_lists.md
```

### Step 5: Start Jupyter & Run Code
Run:
```bash
jupyter notebook
```
Open your newly compiled `.ipynb` file, run the cells, and enjoy interactive coding!

---

## 🧑‍💻 Prerequisites & Setup

Ensure you have Jupyter installed on your environment:
```bash
pip install jupyter
```
All scripts run with standard library dependencies only (no external libraries required).
