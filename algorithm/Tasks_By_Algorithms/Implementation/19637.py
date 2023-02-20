from collections import defaultdict
def solution():
    degree_transitions=defaultdict(str)

    for degree,uplimit in degrees:
        uplimit=int(uplimit)
        if degree_transitions[uplimit]=="":
            degree_transitions[uplimit]=degree

    degree_list=sorted(degree_transitions.keys())
    degree_index=0
    current_degree=degree_list[degree_index]

    characters.sort()
    result=[""] * n_characters

    for character,index in characters:
        while character > degree_list[degree_index]:
            degree_index+=1
            current_degree=degree_list[degree_index]

        result[index]=degree_transitions[current_degree]

    print("\n".join(result))
if __name__ == "__main__":
    with open("input19637.txt", "r") as file:
        n_degrees,n_characters=map(int,file.readline().split())
        degrees=[file.readline().split() for _ in range(n_degrees)]
        characters=[(int(file.readline()),i) for i in range(n_characters)]
    
    solution()