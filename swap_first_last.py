def swap_first_and_last(arr1):
  for i in range(len(arr1)):
    arr1[0],arr1[-1]=arr1[-1],arr1[0]
    return arr1
arr1=[1,2,3,4,5] 
print(swap_first_and_last(arr1))
