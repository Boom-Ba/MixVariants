#Maximum CPU used
"""
Rule 1: the maximum CPU for two overlap jobs is the sum of each CPU used. 
Rule 2: The maximum CPU for non-overlap jobs is the CPU that is currently in use.
"""
#1.minheap
import heapq
def MaxCPUuse(jobs):
  jobs.sort(key=lambda x: x[0])
  minheap=[]
  currCPUUse=0
  maxCPUUse=0
  for j in jobs:
    #check if the top of job standing at heap can be finished before current job starts
    while minheap and len(minheap)>0 and minheap[0][1]<=j[0]:
      #if current job starts later than prev, the Current CPU used - previous use
      currCPUUse-=minheap[0][2]
      heapq.heappop(minheap)
      
    heapq.heappush(minheap,(j[0],j[1],j[2]))
    currCPUUse+=j[2]
    maxCPUUse=max(maxCPUUse,currCPUUse)
  return maxCPUUse
jobs=[(1,4,3),(2,5,4),(7,9,6)]
res=MaxCPUuse(jobs)
print(res)
