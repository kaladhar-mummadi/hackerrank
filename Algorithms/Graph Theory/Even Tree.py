"""
https://www.hackerrank.com/contests/master/challenges/even-tree?h_r=internal-search
"""
def children(adjacency_list,index, number_of_nodes):
    childNodes = adjacency_list[index]
    if len(childNodes) == 0:
        number_of_nodes[index] = 1
        return 1
    for i in childNodes:
        number_of_nodes[index] += children(adjacency_list,i, number_of_nodes)
    number_of_nodes[index] += 1
    return number_of_nodes[index]
if __name__ == '__main__':
    n,m = input().split(' ')
    n,m = [int(n), int(m)]
    number_of_nodes = [0]*n
    adjacency_list = [[] for i in range(n)]
    for _ in range(m):
        u,v = input().split(' ')
        u,v = [int(u),int(v)]
        adjacency_list[v-1].append(u - 1)
    children(adjacency_list,0, number_of_nodes)
    res = 0
    for i in number_of_nodes:
        if i!= 0 and i%2 == 0:
            res +=1
    print(res - 1)


# def count(arr, adjacency_list, number_of_nodes):
#     visited = [False]*n
#     stack = [1]
#     while len(stack) != 0:
#         if len(adjacency_list[arr[-1]]) == 0:
#             vertex = stack.pop()
#             visited[vertex] = True
#             number_of_nodes[vertex] = 1
#         else:
#             for i in adjacency_list[arr[-1]]:
#                 visited[i] = True
#                 stack.append(i)
#
#         if visited[vertex]:
#             number_of_nodes[]
#


# while i>=0:
#     temp = 0
#     for j in adjacency_list[i]:
#         temp += len(adjacency_list[j - 1])
#     number_of_nodes[i] = temp + 1
#     i -= 1
