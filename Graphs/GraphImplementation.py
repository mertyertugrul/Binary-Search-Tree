class Graph(object):
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        # undirected graph
        if self.adjacent_list[node1] is None:
            self.add_vertex(node1)
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def search(self, node):
        for k in self.adjacent_list.keys():
            if k == node:
                return self.adjacent_list[node]
