def difference_odd_even_sum(arr):
  even_sum=odd_sum=0
  for i in arr:
    if i % 2 == 0:
      even_sum += i 
    else:
      odd_sum += i
  diff=abs(even_sum - odd_sum)
  print(f"even sum: {even_sum},Odd sum:{odd_sum},Difference:{diff}")
  return diff

arr= [4,5,2,7]      
print(difference_odd_even_sum(arr))
