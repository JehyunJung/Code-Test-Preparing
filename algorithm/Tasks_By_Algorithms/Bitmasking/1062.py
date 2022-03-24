from itertools import combinations
from string import ascii_lowercase
def bit_convertion(c):
    return ord(c)-ord('a')

def str_to_bit(word):
    bit=0b0
    for c in word:
        bit = bit | 1 << bit_convertion(c) 
    return bit
N,k=0,0
words=[]
bit_maps=[]
with open("input1062.txt","r") as file:
  N,k=map(int,file.readline().split())
  for _ in range(N):
    bit_maps.append(str_to_bit(set(file.readline().strip())))
common_set=set(['a','c','i','t','n'])
alpha_sets=set(ascii_lowercase).difference(common_set)

if k < 5:
    print(0)
elif k==26:
    print(N)
else:
    base_bit=str_to_bit(common_set)
    max_readable=0
    for combination in list(combinations(alpha_sets,k-5)):
        combination_bit=base_bit |str_to_bit(combination) 
        readable=0
        for bit_map in bit_maps:
            if combination_bit & bit_map == bit_map:
                readable+=1
        max_readable=max(max_readable,readable)
    print(max_readable)