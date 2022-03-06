def solution(n):
  binary_digit=list(bin(n))
  binary_digit=binary_digit[2:]
  binary_digit.reverse()
  
  length=len(binary_digit)
  for i in range(length):
    if binary_digit[i]=='1':
      print(i,end=" ")
  print()


if __name__=="__main__":
  n=0
  with open("input3460.txt","r") as file:
    n=int(file.readline())
  solution(n)