class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        numberOfNodes, numberOfEdges = input().split(' ')
        numberOfNodes, numberOfEdges = [int(numberOfNodes), int(numberOfEdges)]
        distances = [-1]*numberOfNodes
        nodes = [None]*numberOfNodes
        head = None
        for i in range(numberOfEdges):
            n1, n2 = input().split(' ')
            n1, n2 = [int(n1), int(n2)]
            if nodes[n1] == None:
                temp = Node(n1)
                distances[n1] = 0
                nodes[n1] = temp
            if nodes[n2] == None:
                temp = Node(n2)
                distances[n2] = 0
                nodes[n2] = temp


