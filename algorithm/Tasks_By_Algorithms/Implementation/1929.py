def solution(start,last):
    prime_map=[True] * (last+1)
    prime_numbers=[]
    prime_map[1]=False

    for i in range(2,last+1):
      if prime_map[i] and i>=start:
        prime_numbers.append(i)
      for j in range(2,((last//i)+1)):
        prime_map[i*j]=False
    
    return prime_numbers    

if __name__=="__main__":
  start,last=0,0

  with open("input1929.txt","r") as file:
    start,last=map(int,file.readline().split())

  prime_numbers=solution(start,last)
  
  for prime_number in prime_numbers:
    print(prime_number)
  