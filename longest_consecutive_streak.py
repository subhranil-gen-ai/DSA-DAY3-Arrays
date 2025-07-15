def longest_consecutive_streak(arr):
  max_count=1
  current_count=1
  most_common=arr[0]
  for i in range(1,len(arr)):
    if arr[i]==arr[i-1]:
      current_count += 1
      if current_count>max_count:
        max_count=current_count
        most_common=arr[i]
    else:
      current_count=1
  print(f"Most common item: {most_common} (Count : {max_count})")
  return most_common,max_count
arr=[1,2,2,3,3,3,3,4]
print(longest_consecutive_streak(arr))
