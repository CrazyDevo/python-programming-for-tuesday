## Python List Methods

Below are the explanations of the **list methods** in Python, along with examples for each:

---

### 1. **`append()`**
Adds a single element to the end of the list.

**Syntax:** `list.append(element)`

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

---

### 2. **`clear()`**
Removes all elements from the list, making it an empty list.

**Syntax:** `list.clear()`

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```

---

### 3. **`extend()`**
Adds all elements of an iterable (e.g., another list) to the end of the list.

**Syntax:** `list.extend(iterable)`

```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

---

### 4. **`sort()`**
Sorts the elements of the list in ascending order by default. You can sort in descending order using the `reverse` parameter.

**Syntax:** `list.sort(key=None, reverse=False)`

```python
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]

# Sorting in descending order
my_list.sort(reverse=True)
print(my_list)  # Output: [4, 3, 2, 1]
```

---

### 5. **`reverse()`**
Reverses the elements of the list in place (i.e., the order of elements is flipped).

**Syntax:** `list.reverse()`

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
```

---

### 6. **`copy()`**
Returns a shallow copy of the list (i.e., creates a new list with the same elements).

**Syntax:** `list.copy()`

```python
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]
```

---

### 7. **`remove()`**
Removes the first occurrence of the specified element from the list. If the element is not found, it raises a `ValueError`.

**Syntax:** `list.remove(element)`

```python
my_list = [1, 2, 3, 2]
my_list.remove(2)  # Removes the first 2
print(my_list)  # Output: [1, 3, 2]
```

---

### 8. **`pop()`**
Removes and returns the element at the specified position (index). If no index is specified, it removes and returns the last element.

**Syntax:** `list.pop(index=-1)`

```python
my_list = [1, 2, 3]
last_item = my_list.pop()
print(last_item)  # Output: 3
print(my_list)    # Output: [1, 2]

# Removing by index
item = my_list.pop(0)
print(item)  # Output: 1
print(my_list)  # Output: [2]
```

---

### 9. **`insert()`**
Inserts an element at a specified position (index).

**Syntax:** `list.insert(index, element)`

```python
my_list = [1, 2, 3]
my_list.insert(1, "a")
print(my_list)  # Output: [1, 'a', 2, 3]
```

---

### 10. **`index()`**
Returns the index of the first occurrence of a specified element in the list. Raises a `ValueError` if the element is not found.

**Syntax:** `list.index(element, start=0, end=len(list))`

```python
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

# Finding an element in a specific range
index = my_list.index(2, 2)
print(index)  # Output: 3
```

---

### 11. **`count()`**
Returns the number of occurrences of a specified element in the list.

**Syntax:** `list.count(element)`

```python
my_list = [1, 2, 2, 3]
count = my_list.count(2)
print(count)  # Output: 2
```

---

## Summary Table

| **Method**   | **Description**                                                                 |
|--------------|---------------------------------------------------------------------------------|
| `append()`   | Adds an element to the end of the list.                                         |
| `clear()`    | Removes all elements from the list.                                            |
| `extend()`   | Adds all elements of an iterable to the end of the list.                       |
| `sort()`     | Sorts the list in ascending (default) or descending order.                     |
| `reverse()`  | Reverses the order of elements in the list.                                    |
| `copy()`     | Returns a shallow copy of the list.                                            |
| `remove()`   | Removes the first occurrence of a specified element.                           |
| `pop()`      | Removes and returns an element by index (default is the last element).         |
| `insert()`   | Inserts an element at a specified index.                                       |
| `index()`    | Returns the index of the first occurrence of an element.                      |
| `count()`    | Returns the number of occurrences of an element in the list.                  |
