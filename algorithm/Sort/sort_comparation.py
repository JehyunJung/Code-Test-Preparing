from selection_sort import selection_Sort
import time

if __name__ == "__main__":
  n=0
  data=[]
  with open("data.txt","r") as file:
    n=file.readline()
    data=list(map(int,file.readline().split()))

  
  start_time=time.time()
  selection_Sort(n,data)
  end_time=time.time()
  print("selection sort time: "+ end_time-start_time+"seconds")
