from selection_sort import selection_Sort
from insertion_sort import insertion_Sort
from quick_sort import quick_Sort
from count_sort import count_Sort
from merge_sort import merge_Sort
import sys
import time

if __name__ == "__main__":
  sys.setrecursionlimit(2000)
  n=0
  data=[]
  with open("big_data.txt","r") as file:
    n=int(file.readline())
    data=list(map(int,file.readline().split()))
  
  functions=[selection_Sort,insertion_Sort,quick_Sort,count_Sort,merge_Sort]  
  for function in functions:
    start_time=time.time()
    function(n,data,0,n-1)
    end_time=time.time()
    print(function)
    print("sort time: "+ str((end_time-start_time))+" seconds")

#Built-In Sort
  start_time=time.time()
  data.sort()
  end_time=time.time()
  print(sorted)
  print("sort time: "+ str((end_time-start_time))+" seconds")