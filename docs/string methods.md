

# Python String Methods

## **1. Case Manipulation Methods**
- **`lower()`**: Converts all characters in the string to lowercase.
  ```python
  "Hello".lower()  # Output: "hello"
  ```

- **`upper()`**: Converts all characters in the string to uppercase.
  ```python
  "hello".upper()  # Output: "HELLO"
  ```

- **`capitalize()`**: Capitalizes the first character of the string and makes all other characters lowercase.
  ```python
  "hello world".capitalize()  # Output: "Hello world"
  ```

- **`title()`**: Converts the first character of each word to uppercase.
  ```python
  "hello world".title()  # Output: "Hello World"
  ```

- **`swapcase()`**: Swaps the case of all characters in the string.
  ```python
  "Hello World".swapcase()  # Output: "hELLO wORLD"
  ```

---

## **2. Trimming and Formatting Methods**
- **`strip()`**: Removes leading and trailing whitespace (or specified characters).
  ```python
  "  hello  ".strip()  # Output: "hello"
  ```

- **`lstrip()`**: Removes leading whitespace (or specified characters).
  ```python
  "  hello".lstrip()  # Output: "hello"
  ```

- **`rstrip()`**: Removes trailing whitespace (or specified characters).
  ```python
  "hello  ".rstrip()  # Output: "hello"
  ```

---

## **3. Search and Replace Methods**
- **`index()`**: Returns the index of the first occurrence of a substring. Raises `ValueError` if not found.
  ```python
  "hello".index("e")  # Output: 1
  ```

- **`rindex()`**: Returns the index of the last occurrence of a substring. Raises `ValueError` if not found.
  ```python
  "hello".rindex("l")  # Output: 3
  ```

- **`find()`**: Returns the index of the first occurrence of a substring. Returns `-1` if not found.
  ```python
  "hello".find("e")  # Output: 1
  ```

- **`rfind()`**: Returns the index of the last occurrence of a substring. Returns `-1` if not found.
  ```python
  "hello".rfind("l")  # Output: 3
  ```

- **`replace()`**: Replaces all occurrences of a substring with another substring.
  ```python
  "hello world".replace("world", "Python")  # Output: "hello Python"
  ```

- **`count()`**: Counts the number of occurrences of a substring.
  ```python
  "hello".count("l")  # Output: 2
  ```

---

## **4. String Testing Methods**
- **`startswith()`**: Returns `True` if the string starts with a specified prefix.
  ```python
  "hello".startswith("he")  # Output: True
  ```

- **`endswith()`**: Returns `True` if the string ends with a specified suffix.
  ```python
  "hello".endswith("lo")  # Output: True
  ```

- **`islower()`**: Returns `True` if all characters are lowercase.
  ```python
  "hello".islower()  # Output: True
  ```

- **`isupper()`**: Returns `True` if all characters are uppercase.
  ```python
  "HELLO".isupper()  # Output: True
  ```

- **`isalpha()`**: Returns `True` if all characters in the string are alphabetic.
  ```python
  "hello".isalpha()  # Output: True
  ```

- **`isdigit()`**: Returns `True` if all characters in the string are digits.
  ```python
  "123".isdigit()  # Output: True
  ```

- **`isalnum()`**: Returns `True` if all characters in the string are alphanumeric.
  ```python
  "hello123".isalnum()  # Output: True
  ```

- **`istitle()`**: Returns `True` if the string follows title case.
  ```python
  "Hello World".istitle()  # Output: True
  ```

- **`isspace()`**: Returns `True` if the string contains only whitespace.
  ```python
  "   ".isspace()  # Output: True
  ```

---

## **5. Other Useful String Methods**
- **`split()`**: Splits the string into a list using a delimiter (default is whitespace).
  ```python
  "hello world".split()  # Output: ["hello", "world"]
  ```

- **`rsplit()`**: Splits the string from the right.
  ```python
  "a,b,c".rsplit(",", 1)  # Output: ['a,b', 'c']
  ```

- **`join()`**: Joins elements of an iterable into a string, separated by the string calling the method.
  ```python
  ", ".join(["apple", "banana"])  # Output: "apple, banana"
  ```

- **`partition()`**: Splits the string into a tuple of three parts: before the separator, the separator, and after the separator.
  ```python
  "hello world".partition(" ")  # Output: ('hello', ' ', 'world')
  ```

- **`zfill()`**: Pads the string with zeros on the left to fill the specified width.
  ```python
  "42".zfill(5)  # Output: "00042"
  ```

- **`format()`**: Formats the string using placeholders.
  ```python
  "Hello, {}!".format("Alice")  # Output: "Hello, Alice!"
  ```

- **`format_map()`**: Similar to `format()`, but takes a dictionary.
  ```python
  data = {"name": "Alice"}
  "Hello, {name}!".format_map(data)  # Output: "Hello, Alice!"
  ```

- **`encode()`**: Encodes the string into a specified encoding (e.g., UTF-8).
  ```python
  "hello".encode("utf-8")  # Output: b'hello'
  ```

- **`casefold()`**: Converts the string to lowercase for caseless comparisons.
  ```python
  "ß".casefold()  # Output: "ss"
  ```

- **`expandtabs()`**: Replaces tab characters with spaces.
  ```python
  "a\tb\tc".expandtabs(4)  # Output: "a   b   c"
  ```
