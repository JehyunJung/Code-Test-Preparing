from itertools import permutations
def solution():
    prev_value=0
    for permutation in list(permutations(A,len(A))):
        value=int("".join(permutation)) 
        if value > B:
            continue
        prev_value=value

    if prev_value==0:
        print(-1)
    else:
        print(prev_value)

if __name__ == "__main__":
    A,B=0,0
    B_length=0
    with open("input16943.txt","r") as file:
        A,B=map(str,file.readline().split())
    
    B=int(B)
    A=list(A)

    solution()
