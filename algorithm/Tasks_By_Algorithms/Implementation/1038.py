def check(number):
  segments=list(str(number))
  length=len(segments)
  for index in range(1,length):
    if segments[index-1] <= segments[index]:
      return False
  return True
    
  
def solution():
  numbers=[]
  index=0
  for i in range(1000000):
    if check(i):
      numbers.append(i)
      if index==n:
        print(numbers[-1])
        return
      index+=1
  print(-1)
    
  
if __name__ == "__main__":
  n=0
  with open("input1038.txt","r") as file:
    n=int(file.readline())
  solution()
  