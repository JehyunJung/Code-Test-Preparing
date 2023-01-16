def solution(str):
    global answer
    if answer:
        return
        
    if len(str)==len(start):
        answer=(start==str)
        return

    if str[0]=="B":
        solution(str[:0:-1])
    if str[-1]=="A":
        solution(str[:-1])


if __name__ == "__main__":
    with open("input12919.txt","r") as file:
        start=list(file.readline().strip())
        end=list(file.readline().strip())

    answer=False
    solution(end)

    print(1 if answer else 0)