n,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

swapping_count=0
index=0

while swapping_count < k:
  if A[index] < B[index]:
    A[index],B[index]=B[index],A[index]
    index+=1
    swapping_count+=1
  else:
    break

print(sum(A))

