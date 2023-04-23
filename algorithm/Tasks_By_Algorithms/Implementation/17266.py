from math import ceil
import sys
def solution():
    required_lights=[lights[0],n-lights[-1]]
    
    for i in range(m-1):
        required_lights.append(ceil((lights[i+1]-lights[i])/2))
     
    print(max(required_lights))
if __name__ == "__main__":
    sys.stdin=open("input17266.txt","r")
    n=int(input())
    m=int(input())
    lights=list(map(int,input().split()))
    
    solution()