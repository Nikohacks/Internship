## The surviving person

### ### Problem Statement
There were **n** people in a desert. They were caught by thieves and got tortured. The torture was each **k-th** person will be killed in a round and the last one standing survives.

### Input
- n = number of people
- k = interval of elimination

### Output
- Position of the Survivor (1-based indexing)

### Examples
**Example 1:**  
n = 8, k = 2  
Killed order: 2 → 4 → 6 → 8 → 3 → 5 → 7  
Survivor = 1

**Example 2:**  
n = 7, k = 3  
Killed order: 3 → 6 → 2 → 7 → 5 → 1  
Survivor = 4

---
### Approach

The problem is solved through a **direct step-by-step simulation** of the elimination process.

1. **Representation** – The surviving people are maintained in an ordered sequence (list) containing their positions from `1` to `n`.
2. **Pointer tracking** – A `current` index tracks the starting point for counting in the current round.
3. **Victim selection** – The victim is located at index:
   `(current + k - 1) % length_of_sequence`
   - `k - 1` accounts for counting the current person as the first.
   - The modulo operation handles the circular wrap-around.
4. **Removal & continuation** – The victim is removed from the sequence. Since elements shift left after removal, the `current` index automatically points to the next person, allowing the process to continue without additional adjustments.
5. **Termination** – The loop repeats until only one element remains, which is returned as the survivor.

---

### Data Structures & Algorithms (DSA)

- **Data Structure**: **List (Dynamic Array)** – stores the active participants. Provides O(1) access and built-in removal with shifting.[[List(Dynamic Array)]]

- **Algorithmic Pattern**: **Iterative Simulation with Modulo Arithmetic** – uses modular arithmetic to achieve circular traversal over a linear array without physically restructuring the circle.

---

### Complexity Analysis

- **Time Complexity**: `O(n²)`  
  - The loop runs `n - 1` times.
  - Each `.pop(index)` operation on a list shifts subsequent elements, costing `O(n)` in the worst case.
  - Suitable for moderate inputs; the directness of the simulation takes priority over optimization here.

- **Space Complexity**: `O(n)`  
  - The list stores all `n` positions initially.

---

### Edge Cases

| Scenario                     | Input          | Expected Output | Handling                                                                                                                         |
| :--------------------------- | :------------- | :-------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| Single person                | n = 1, k = any | 1               | The loop does not execute; the only element is returned.                                                                         |
| Elimination every 1st person | n = 5, k = 1   | 5               | Formula `(current + 0) % len` removes the current person each time, effectively killing sequentially until the last one remains. |
| k larger than n              | n = 5, k = 7   | 3               | The modulo operation wraps the index around, correctly simulating multiple full circles before the kill.                         |
