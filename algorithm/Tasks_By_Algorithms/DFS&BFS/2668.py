import sys
def dfs(first,second,number):
    next_number=numbers[number]
    first.add(number)
    second.add(next_number)

    if next_number in first:
        if first==second:
            answer.update(first)
        return
    
    dfs(first,second,next_number)

def solution():
    for number in numbers:
        if number not in answer:
            dfs(set(),set(),number)

    print(len(answer))
    print("\n".join(map(lambda x: str(x+1),sorted(answer))))
if __name__ == "__main__":
    sys.stdin=open("input2668.txt","r")
    n=int(input())
    numbers=[int(input())-1 for _ in range(n)]
    answer=set()

    solution()