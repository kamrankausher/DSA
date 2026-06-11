# Chapter 10: Hash Tables & Hash Maps 🚀

Have you ever wondered how Python dictionaries look up values instantly? How does `user_database["kamran"]` return a profile in a fraction of a microsecond, even if there are millions of users?

The secret is the **Hash Table** (also called a Hash Map). It is one of the most important data structures in computer science, blending the instant access speed of arrays with the flexible key-value lookup of a dictionary.

Today, we will learn how hash functions work, how to handle "collisions" when two keys fight for the same spot, and build a fully functional Hash Table from scratch!

***

## 💡 Real-World Analogy: The Filing Cabinet & The Coat Check

To understand hashing, think of two systems:

### 1. The Hashed Filing Cabinet
Imagine you run a large school office and need to file student folders.
* **The Rule (Hash Function):** You decide to file folders based on the **first letter of the student's last name**.
  * Last names starting with **A** go to Drawer 0.
  * Last names starting with **B** go to Drawer 1.
* **The Lookup:** If you need "Kamran Kausher", you don't search all drawers. You look at the first letter **"K"** (the key), jump directly to Drawer 10, and search only the folders inside.
* **The Collision:** What if you have two students named "Kamran Kausher" and "Karan Kapoor"? Both start with "K", so they both go to Drawer 10. This is a **Collision**! You must stack them inside the same drawer.

### 2. The Coat Check Room
* You hand the attendant your coat (value).
* The attendant gives you a numbered plastic ticket (key).
* When you leave, you hand back the ticket, and the attendant retrieves your exact coat instantly without scanning every other coat.

***

## 📌 In Simple Terms: Keys, Values & Hashing

* **Key-Value Pair:** The mapping of a unique identifier (Key) to a piece of data (Value). E.g. `"apple" -> "A sweet red fruit"`.
* **Hash Function:** A mathematical recipe that takes any key (like a string or object) and converts it into a fixed number (hash code).
* **Bucket Index:** The exact array slot where the key-value pair is stored, calculated as:
  $$\text{Index} = \text{Hash Code} \% \text{Size of Array}$$
* **Collision:** When two different keys produce the same Bucket Index.
* **Collision Resolution (Chaining):** Storing colliding items in a linked list at the same bucket index.

***

## 🧠 Memory Model: Hashing with Chaining

Here is how a Hash Table of size `5` stores keys `"apple"` (hashes to index 1), `"banana"` (hashes to index 3), and `"apricot"` (also hashes to index 1 - collision!).

```
      HASH TABLE ARRAY (SIZE 5)
   ┌─────────┬──────────────────────┐
   │ Index 0 │ None                 │
   ├─────────┼──────────────────────┤   ┌────────────────┐     ┌──────────────────┐
   │ Index 1 │ Pointer ─────────────┼──►│ Key: "apple"   │     │ Key: "apricot"   │
   ├─────────┼──────────────────────┤   │ Value: "Red"   │     │ Value: "Orange"  │
   │ Index 2 │ None                 │   │ Next: 0x800  ──┼────►│ Next: None       │
   ├─────────┼──────────────────────┤   └────────────────┘     └──────────────────┘
   │ Index 3 │ Pointer ───────────┐ │
   ├─────────┼────────────────────┼─┤
   │ Index 4 │ None               │ │   ┌────────────────┐
   └─────────┴────────────────────┼─┘   │ Key: "banana"  │
                                  └────►│ Value: "Yellow"│
                                        │ Next: None     │
                                        └────────────────┘
```

***

## 🧠 Python Implementation: Custom Hash Table with Chaining

Let's write a Hash Table in Python, printing detailed indexing logs. We will implement our own simple Node chain for Chaining.

```python
class HashNode:
    def __init__(self, key, value):
        """A key-value node for our bucket chains."""
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.buckets = [None] * capacity  # Array of chains
        self.size = 0
        print(f"[INIT] HashTable created with capacity: {capacity}")

    def _hash_function(self, key):
        """Simple hash function summing ASCII values of characters."""
        ascii_sum = sum(ord(char) for char in str(key))
        index = ascii_sum % self.capacity
        print(f"  [HASH] Key '{key}' -> Sum: {ascii_sum} -> Bucket Index: {index}")
        return index

    def put(self, key, value):
        """Inserts or updates a key-value pair."""
        print(f"\n[PUT] Storing key-value: '{key}' -> '{value}'")
        idx = self._hash_function(key)
        
        # Check if bucket is empty
        if not self.buckets[idx]:
            self.buckets[idx] = HashNode(key, value)
            self.size += 1
            print(f"  [INSERT] Bucket {idx} was empty. Created head node.")
            return

        # Handle collision: walk down the chain
        current = self.buckets[idx]
        prev = None
        while current:
            # If key already exists, update the value
            if current.key == key:
                print(f"  [UPDATE] Key '{key}' already exists in bucket {idx}. Updating value from '{current.value}' to '{value}'.")
                current.value = value
                return
            prev = current
            current = current.next

        # Key not in chain, add to the end
        prev.next = HashNode(key, value)
        self.size += 1
        print(f"  ⚠️ [COLLISION] Key '{key}' collided at bucket {idx}. Linked to end of chain.")

    def get(self, key):
        """Retrieves the value associated with key. Returns None if not found."""
        print(f"\n[GET] Looking up key: '{key}'")
        idx = self._hash_function(key)
        
        current = self.buckets[idx]
        steps = 0
        while current:
            steps += 1
            if current.key == key:
                print(f"  🎉 Found! Value: '{current.value}' in {steps} steps.")
                return current.value
            current = current.next
            
        print(f"  ❌ Key '{key}' not found in bucket {idx} after {steps} steps.")
        return None

    def remove(self, key):
        """Removes the key-value pair from the table."""
        print(f"\n[REMOVE] Deleting key: '{key}'")
        idx = self._hash_function(key)
        
        current = self.buckets[idx]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[idx] = current.next
                self.size -= 1
                print(f"  🎉 Removed key '{key}' from bucket {idx}.")
                return True
            prev = current
            current = current.next
            
        print(f"  ❌ Key '{key}' not found. Nothing to remove.")
        return False


# --- Test our Hash Table ---
ht = HashTable(3)
ht.put("apple", "Red Fruit")
ht.put("banana", "Yellow Fruit")

# Colliding key (let's check collision output)
ht.put("apricot", "Orange Fruit")

ht.get("apple")
ht.get("apricot")
ht.get("grape") # Missing

ht.remove("apple")
ht.get("apricot") # Still exists!
```

***

## 🔍 Collision & Search Dry Run (Trace Table)

Let's track how keys are placed in `HashTable(capacity=3)`.
* Hash Formula: `Sum(ASCII) % 3`

| Key | ASCII Sum | Bucket Index | Operations / Chaining State | Size |
| :--- | :---: | :---: | :--- | :---: |
| **"apple"** | $97+112+112+108+101 = 530$ | $530 \% 3 =$ **2** | Stored at Head of Bucket 2 | 1 |
| **"banana"** | $98+97+110+97+110+97 = 609$ | $609 \% 3 =$ **0** | Stored at Head of Bucket 0 | 2 |
| **"apricot"**| $97+112+114+105+99+111+116 = 754$| $754 \% 3 =$ **2** | **Collision!** Appended after "apple" in Bucket 2 | 3 |

***

## 📈 Complexity & Big O Analysis

| Operation | Average Case Time | Worst Case Time | Space Complexity | Why? |
| :--- | :---: | :---: | :---: | :--- |
| **Insertion** | $O(1)$ | $O(N)$ | $O(N)$ | Constant time index math. Worst case when all keys collide. |
| **Search** | $O(1)$ | $O(N)$ | $O(1)$ | Instant lookup if buckets are short. Worst case scans chain of size $N$. |
| **Deletion** | $O(1)$ | $O(N)$ | $O(1)$ | Instant deletion via pointers. Worst case traverses full chain. |

* **Maintaining O(1) Speed:** To prevent chains from growing long, libraries automatically double the array capacity and re-hash all elements when the table is 70% full. This percentage is called the **Load Factor**.

***

## 🎓 Interview & LeetCode Applications

### LeetCode 387: First Unique Character in a String (Easy)
> **Problem:** Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

#### The Hash Map Frequency Counter Approach (O(N))
We loop through the string once to count the frequency of each character in a Hash Map. Then we loop a second time to find the first character with a count of `1`.

```python
def first_uniq_char(s):
    """
    Finds the first unique character index in O(N) time using a Hash Map.
    """
    print(f"=== Running First Unique Character for '{s}' ===")
    frequency = {}
    
    # Pass 1: Count characters
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
        
    print(f"  Frequencies computed: {frequency}")
    
    # Pass 2: Find the first character with count 1
    for index, char in enumerate(s):
        if frequency[char] == 1:
            print(f"  🎉 Found! '{char}' is unique. First index is {index}\n")
            return index
            
    print("  ❌ No unique characters found.\n")
    return -1

# Test
first_uniq_char("leetcode")
first_uniq_char("loveleetcode")
```

***

## 🤖 Connection to Machine Learning & AI: Dataset MinHash Deduplication

How do hash tables help train Large Language Models (LLMs)?
* **The Web Crawl Data Problem:** LLMs are trained on massive crawls of the internet (e.g. Common Crawl). This raw text contains millions of duplicate articles, spam, and scraped pages.
* **The Danger:** Training on duplicates causes the LLM to overfit, memorize text, and waste millions of dollars in GPU computing time.
* **The Solution: MinHash & Locality Sensitive Hashing (LSH):**
  1. We break each web page into small phrases (shingles).
  2. We pass these phrases through different hash functions and take the minimum hash values (**MinHash**).
  3. LSH groups similar documents into the same **Hash Table Buckets**.
  4. If two different web pages hash to the same bucket, the system flags them as duplicates.
* By using hash tables to filter out duplicates, researchers can clean up training data instantly, reducing training datasets by **up to 50%** and saving millions in computation!
