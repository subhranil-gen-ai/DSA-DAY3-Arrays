arr = [4, -1, 0, 3, -2, 0]
for i in range(len(arr)):
  if arr[i] < 0:
    arr[i] = 0
print(arr)
