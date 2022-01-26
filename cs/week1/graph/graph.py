# CS - Data Structure - Graph
# Jennas Lee


# Adjacency Metrix Graph
class Graph:
    # 5 nodes graph
    graph = [[] for tmp in range(5)]

    # add
    def append(self, first_node, second_node, weight):
        self.graph[first_node].append([second_node, weight])
        self.graph[second_node].append([first_node, weight])


def main():
    print("Graph")
    # queue data structure
    graph = Graph()

    graph.append(1, 2, 3)
    graph.append(1, 3, 5)
    graph.append(3, 4, 2)
    graph.append(3, 5, 4)
    graph.append(4, 5, 6)
    #        (3)
    #     1 ----- 2
    #     |
    # (5) |
    #     |  (2)
    #     3 ----- 4
    #      \     /
    #   (4) \   / (6)
    #        \ /
    #         5


if __name__ == '__main__':
    main()
