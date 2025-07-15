def element_with_min_non_zero_freq(arr):
  freq={}
  for i in arr:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] =1  
  min_count=min(freq.values())
  elements=[key for key,value in freq.items() if value==min_count]
  return elements
arr=[4,6,6,2,6]  
print(element_with_min_non_zero_freq(arr))
