# python3
import sys
import threading
#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 

def evaluatedepth(parents,i,depth):
    if depth[i]!=-1:
        return depth[i]
    if parents[i]==-1:
        depth[i]=1
        return depth[i]
    if depth[parents[i]]==-1:
        depth[parents[i]]=evaluatedepth(parents,parents[i],depth)
    depth[i]=1+depth[parents[i]]
    return 1+depth[parents[i]]
def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    depth=[-1 for i in range(n)]
    st=0
    for i in range(n):
        evb=evaluatedepth(parents,i,depth)
        st=max(st,evb)
    return st


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
