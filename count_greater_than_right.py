def count_greater_than_right(arr):
  count=0
  max_right=float('-inf')
  for i in reversed(arr):
    if i > max_right:
     count += 1
     max_right=i
  print(f"Count of elements greater than all elements to their right: {count}")   
  return count
arr=[10,4,6,3,5]
print(count_greater_than_right(arr))
