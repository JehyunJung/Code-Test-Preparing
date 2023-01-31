from collections import defaultdict
def bit_difference(str1,str2):
    bit_count=0

    for char1,char2 in zip(str1,str2):
        if char1 != char2:
            bit_count+=1

    return bit_count

def create_bit_transition():
    bit_count=0
    bit_transitions=[defaultdict(list) for _ in range(10)]
    bit_expression=["1110111","0010100","0111011","0111110","1011100","1101110","1101111","0110100","1111111","1111110"]
    for i in range(10):
        for j in range(10):
            bit_count=bit_difference(bit_expression[i],bit_expression[j])
            bit_transitions[i][bit_count].append(j)    

    return bit_transitions

def solution(index,transition_count,after_transition):
    global probable_floor
    if index==k:
        if 1<=transition_count <=p and 1<=after_transition <=n:
            probable_floor.add(after_transition)
        return

    before_transition=current_floor[current_floor_length-index-1] if index < current_floor_length else 0

    for i in range(6):
        for floor in bit_transitions[before_transition][i]:
            solution(index+1,transition_count+i,after_transition+floor*(10**index))


if __name__ == "__main__":
    with open("input22251.txt","r") as file:
        n,k,p,x=map(int,file.readline().split())

    bit_transitions=create_bit_transition()
    probable_floor=set()
    current_floor=list(map(int,str(x)))
    current_floor_length=len(current_floor)
    print(current_floor)
    solution(0,0,0)

    print(len(probable_floor),probable_floor)