from collections import defaultdict
def solution():

    tree_types=sorted(tree_counts.keys())

    for tree in tree_types:
        print(f"{tree} {round(tree_counts[tree]/total_trees *100 ,4)}")

if __name__ == "__main__":
    tree_counts=defaultdict(int)
    total_trees=0
    while True:
        try:
            tree=input().strip()
            tree_counts[tree]+=1
            total_trees+=1
        except EOFError:
            break
    
    solution()
