arr=[4,-1,0,3,-2,0]
count1=count2=count3=0
for i in arr:
  if i==0:
    count1 += 1
  elif i>0:
    count2 += 1
  else:
    count3 += 1    
print(count1) 
print(count2)
print(count3)           
