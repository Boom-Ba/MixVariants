#Check if two strings can make equal with only one swap 
def checkCanMake(s, b):
  sNeed=[]
  bNeed=[]

  i=0
  j=0
  while i<len(s) and j<len(b):
    if s[i]!=b[j]:
      sNeed.append(i)
      bNeed.append(j)
    
    i+1
    j+=1

  if len(sNeed)>2 or len(bNeed)>2:
    return False
  for i in range(len(sNeed)):
    if sNeed[i]!=bNeed[i]:
      return False
  return True
