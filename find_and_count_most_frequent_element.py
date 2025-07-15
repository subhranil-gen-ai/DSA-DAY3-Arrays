def most_frequent_element(arr):
  freq={}
  for i in arr:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1 
  max_count = max(freq.values()) 
  most_common=[key for key,value in freq.items() if value==max_count]   
  print(f"Most frequent item: {most_common} (Count : {max_count})")
  return most_common,max_count
arr=[2,4,4,1,1,3,9,4]
print(most_frequent_element(arr))
