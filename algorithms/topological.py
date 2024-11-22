"""
Topological sorting
https://en.wikipedia.org/wiki/Topological_sorting
"""

from __future__ import print_function


class Graph(object):
    """ Simple implementation of directed acyclic graph
    nodes : set
            set of all nodes in the graph
    dependencies : list
            list of tuples (node1, node2) which show connection
            between nodes of the graph
    """
    def __init__(self, nodes, dependencies):
        self.nodes = nodes
        self.dependencies = dependencies

    def __str__(self):
        """ string representation of the graph """
        string = ''
        for node in sorted(self.nodes):
            strnode = ["{} -> {}".format(start, end)
                       for start, end in self.dependencies if start == node]
            string += "node {}: {}\n".format(node, " ".join(strnode))
        return string[:-1]

    def topological_sort(self):
        """ Topological sort implementation
        Returns
        -------
        out : list
              list of tolopological sorted nodes
        """
        # determine order and stack lists
        order, stack = [], set(self.nodes)
        # colors : default - WHITE, 1 - GRAY, 2 - BLACK
        colors = {}

        def dfs(node):
            """ Depth-first search """
            # set gray color for current node
            colors[node] = 1
            for start, sub in self.dependencies:
                if start != node:
                    # skip node
                    continue
                # get color
                color = colors.get(sub, 0)
                if color == 1:
                    # gray color
                    raise ValueError('Cycle')
                elif color == 2:
                    # black color
                    continue
                # remove sub node from stack
                stack.discard(sub)
                # recursive call
                dfs(sub)
            # insert to top of list
            order.insert(0, node)
            # set black color for current node
            colors[node] = 2

        while stack:
            dfs(stack.pop())
        return order


if __name__ in '__main__':
    GRAPH_NODES = {'a', 'b', 'c', 'd'}
    GRAPH_DEPENDECIES = [('a', 'b'), ('c', 'b'), ('c', 'a'), ('d', 'c'), ('a', 'd')]
    GRAPH = Graph(GRAPH_NODES, GRAPH_DEPENDECIES)
    print("Show Graph:\n{}\n".format(GRAPH))
    print("Show nodes in topological order: {}".format(GRAPH.topological_sort()))
