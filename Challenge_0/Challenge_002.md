## Number Conversion - Arabic to Geez

### Problem Statement
Given an Arabic number, convert it to a Geez number.
### Input
- n = Arabic Number (integer)
### Output
- Ge'ez representation of the number
### Examples

**Example 1:**  
n = 23  
Output = ፳፫

**Example 2:**  
n = 251  
Output = ፪፻፶፩

**Example 3:**  
n = 10456  
Output = ፼፬፻፶፮

---

### Ge'ez Numeral System Overview

| Value | Symbol |
| :---: | :----: |
|   1   |   ፩    |
|   2   |   ፪    |
|   3   |   ፫    |
|   4   |   ፬    |
|   5   |   ፭    |
|   6   |   ፮    |
|   7   |   ፯    |
|   8   |   ፰    |
|   9   |   ፱    |

| Value | Symbol |
| :---: | :----: |
|  10   |   ፲    |
|  20   |   ፳    |
|  30   |   ፴    |
|  40   |   ፵    |
|  50   |   ፶    |
|  60   |   ፷    |
|  70   |   ፸    |
|  80   |   ፹    |
|  90   |   ፺    |

| Value | Symbol | Name |
| :---: | :---: | :--- |
| 100 | ፻ | ፻ |
| 10000 | ፼ | ፼ |

**Coversion Rules:**

1. **Concatenation**: Ge'ez numbers are formed by concatenating symbols from highest place value to lowest.
2. **Tens + Units**: Tens and units are combined without separators (e.g., 23 → ፳፫).
3. **Hundreds**: A multiplier (1-9) is placed before ፻ (e.g., 200 → ፪፻, 500 → ፭፻).
   - **Exception**: 100 is just ፻ (no leading ፩).
4. **Thousands**: Written as hundreds of ten-thousands.
   - 1000 → ፲፻ (10 × 100)
   - 2000 → ፳፻ (20 × 100)
   - 9000 → ፺፻ (90 × 100)
5. **Ten-thousands**: The symbol ፼ represents 10000.
   - A multiplier (1-9) is placed before ፼ (e.g., 30000 → ፫፼).
   - **Exception**: 10000 is just ፼ (no leading ፩).
6. **After ፼**: The remainder (up to 9999) follows normally.

---

### Approach
Used three principles for Ge'ez conversion
1. **Mapping of ones and tens** - These are mapped directly using a dictionary since they require no further decomposition, stored in a dictionary
2. Chunking in Hundreds - Ge'ez naturally structures itself around groups of 100, so the number is broken down to chunks of pairs
3. There is no zero and 100 doesn't start with the digit mapped to Arabic one, instead stands on its own
---
### Edge Cases

| Case         | Input | Expected       | Handling                                                                                                                   |
| :----------- | :---: | :------------- | :------------------------------------------------------------------------------------------------------------------------- |
| Zero         |   0   | (empty string) | Return "" as no symbol for 0.                                                                                              |
| Single digit |   7   | ፯              | Direct unit mapping.                                                                                                       |
| Tens only    |  60   | ፷              | Direct tens mapping.                                                                                                       |
| 100          |  100  | ፻              | No leading 1 for 100.                                                                                                      |
| 200          |  200  | ፪፻             | Digit + ፻.                                                                                                                 |
| 1000         | 1000  | ፲፻             | 10 × 100.                                                                                                                  |
| 5000         | 5000  | ፶፻             | 50 × 100.                                                                                                                  |
| 10000        | 10000 | ፼              | No leading 1 for 10000.                                                                                                    |
| 20000        | 20000 | ፪፼             | Digit + ፼.                                                                                                                 |
| 10456        | 10456 | ፼፬፻፶፮          | 10000 + 400 + 56.                                                                                                          |


---
### Data Structures & Algorithms (DSA)

- **Data Structure**: **Dictionary / Hash Map** – maps numeric values to their Ge'ez Unicode symbols for O(1) lookup. [[Dictionary - Hash Map]]

- **Algorithm**: **Place-value Decomposition** – iterative division and modulo operations to extract each positional digit. [[Iteration]]

---

### Complexity Analysis

- **Time Complexity**: `O(n)` where `n` is the number of digits (maximum 5 for this problem).
- **Space Complexity**: `O(n)` for storing the resulting string.