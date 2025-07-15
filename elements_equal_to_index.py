def elements_equal_to_index(arr):
  count=0
  for i in range(len(arr)):
    if arr[i]==i:
      count += 1
  return count
arr=[2,1,2,7,4]
print(elements_equal_to_index(arr))
