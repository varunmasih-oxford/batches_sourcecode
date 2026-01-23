import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original array:", data)
print(data[3:5])
print(data[1:8:2])
print(data[1:])
print(data[:5])
print(data[::2])
print(data[-3::])
print(data[:-2:])
print(data[::-1])
print(data[::-2])







arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2d[0, :]) # row 0
print(arr2d[:, 1]) # column 1


print(arr2d[1, 1:]) # column 1