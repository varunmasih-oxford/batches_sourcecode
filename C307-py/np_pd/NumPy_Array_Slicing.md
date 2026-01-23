# NumPy Array Slicing (Simple & Clear)

**Array slicing** in NumPy means extracting a part (subset) of an array
using index ranges.\
It works on **1D, 2D, and multi-dimensional arrays**.

------------------------------------------------------------------------

## 1️⃣ Slicing 1D Arrays

### Syntax

``` python
array[start : stop : step]
```

-   `start` → index to begin (included)
-   `stop` → index to end (excluded)
-   `step` → gap between elements

### Example

``` python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])    # [20 30 40]
print(arr[:3])     # [10 20 30]
print(arr[3:])     # [40 50 60]
print(arr[::2])    # [10 30 50]
print(arr[-3:])    # [40 50 60]
```

------------------------------------------------------------------------

## 2️⃣ Slicing 2D Arrays (Rows & Columns)

### Syntax

``` python
array[row_start:row_end, col_start:col_end]
```

### Example

``` python
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2d[0:2, 1:3])
```

### Output

    [[2 3]
     [5 6]]

------------------------------------------------------------------------

## 3️⃣ Selecting Entire Rows or Columns

``` python
print(arr2d[1, :])   # Entire 2nd row → [4 5 6]
print(arr2d[:, 2])   # Entire 3rd column → [3 6 9]
```

------------------------------------------------------------------------

## 4️⃣ Slicing with Steps in 2D

``` python
print(arr2d[::2, ::2])
```

### Output

    [[1 3]
     [7 9]]

------------------------------------------------------------------------

## 5️⃣ Important Rule (Very Important for Students)

👉 **NumPy slicing returns a VIEW, not a copy**

``` python
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 99

print(a)  # [1 99 3 4 5]
```

To avoid this:

``` python
b = a[1:4].copy()
```

------------------------------------------------------------------------

## 6️⃣ Real-World Example (Data Analysis)

``` python
sales = np.array([1200, 1500, 1700, 1600, 1800, 2000])

# First 3 months sales
print(sales[:3])

# Last 2 months sales
print(sales[-2:])
```

------------------------------------------------------------------------

## 🔑 Summary

  Feature          Description
  ---------------- -------------------------------
  `start:stop`     Select range
  `::step`         Skip values
  `:`              Select all
  Negative index   Count from end
  View             Changes affect original array

------------------------------------------------------------------------

**Author:** Varun Masih\
**Topic:** NumPy Basics -- Array Slicing
