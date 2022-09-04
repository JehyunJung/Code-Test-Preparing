def solution():
    weights.sort()

    maximum_weight=1

    for weight in weights:
        if maximum_weight < weight:
            break
        maximum_weight+=weight
    return maximum_weight
if __name__ == "__main__":
    N=0
    weights=[]

    with open("input2437.txt","r") as file:
        N=int(file.readline())
        weights=list(map(int,file.readline().split()))
    print(solution())