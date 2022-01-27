#Maximum CPU used
"""
Rule1: if no two job overlaps, maxCPU used is max of each of them
Rule2: if overlaps, the maximum is sum of overlapped ranges
"""

#(start, end, CPU used)
#1 2 4 5, maxcpu used is 7
#1.minheap
import heapq
def MaxCPUuse(jobs):
  jobs.sort(key=lambda x: x[0])
  minheap=[]
  currCPUUse=0
  maxCPUUse=0
  for j in jobs:
    #(1,4,3),(2,5,4),(7,9,6)]
    #check if the top of job standing at heap can be finished before current job starts
    while minheap and len(minheap)>0 and minheap[0][1]<=j[0]:
      currCPUUse-=minheap[0][2]
      heapq.heappop(minheap)
    heapq.heappush(minheap,(j[0],j[1],j[2]))
    currCPUUse+=j[2]
    maxCPUUse=max(maxCPUUse,currCPUUse)
  return maxCPUUse
jobs=[(1,4,3),(2,5,4),(7,9,6)]
res=MaxCPUuse(jobs)
print(res)
