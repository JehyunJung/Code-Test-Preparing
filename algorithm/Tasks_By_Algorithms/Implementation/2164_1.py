from math import log2
def solution():
    left_bit_index=2**int(log2(n))
    
    if left_bit_index==n:
        print(n)
    else:
        print(2*(n-left_bit_index))

if __name__ == "__main__":
    """ with open("input2164.txt","r") as file:
        n=int(file.readline()) """
    
    for n in range(1,101):
        solution()