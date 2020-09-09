def ArrayChallenge(strArr):

  # code goes here
  n = len(strArr)
  keep = []
  dic = {}
  for i in range(1,n):
    k = strArr[i].split(":")
    keep.append(k)

  
  current = 0
  
  for i in range(0,len(keep)):
    j = i
    count = 0
    keeptrack = 1

    while count < len(keep):
      if j>=len(keep):
        j=j%len(keep)
      current += int(keep[j][0])
      current -= int(keep[j][1])
      
      if current > 0:
        keeptrack = keeptrack+1  
      dic[str(i+1)] = keeptrack
      j = j+1
      count = count+1
    
  for k,v in dic.items():
    if v == len(keep):
      strArr = k
      break;
    strArr = "impossible"
  
 
  return strArr 

# keep this function call here 
print(ArrayChallenge(input()))