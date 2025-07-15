def replace_max_element_with_zero(arr):
  for i in arr:
    max_arr=max(arr)
  for i in range(len(arr)):
    if arr[i]==max_arr:
      arr[i]=0
  return arr
arr=[4,6,6,2,6]  
print(replace_max_element_with_zero(arr))
