import matplotlib.pyplot as plt
import networkx as nx
from random import randint, shuffle, seed
from Graph import Graph
from Node import Node

def random_edge(graph):
    """
        Случайное соединение узлов графа.
    """
    for index in graph.nodes:
        for jindex in graph.nodes:
            if randint(1, 6) == 1 and index != jindex:
                index.add(jindex)
    return graph

def binding(graph, gr):
    """
        Перенос абстракного графа на библиотеку networkx.
    """
    for node in graph.nodes:
        for friend in node.friends:
            gr.add_edge(node, friend)
    return gr

def draw(graph, gr):
    """
        Отрисовка графа.
    """
    count = 0
    color_edge = ['red', 'green', 'blue', 'yellow']
    pos = nx.circular_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=300)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, edge_color='black')
    for i in range(1, 5, 1):
        h = nx.Graph()
        h = color(gr, i)
        graph.add_edges_from(h.edges)
        if count == 4:
            count = 0
        nx.draw_networkx_edges(graph, pos, edgelist=h.edges, edge_color=color_edge[count])
        count += 1
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif', font_color='blue')
    plt.axis('off')
    plt.show()

def color(graph, friend):
    """
        Нахождение узлов, содержащих N общих соседей.
    """
    array_edge = []
    h = nx.Graph()
    for inode in graph.nodes:
        for jnode in graph.nodes:
            if len(set(inode.friends) & set(jnode.friends)) == friend:
                array_edge.append((inode, jnode))
    h.add_edges_from(array_edge)
    return h


graph = Graph()
names = []
with open('names.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        names.append(line[:-1])

shuffle(names)
names = names[:100]
for i in names:
    graph.add(Node(i))
graph = random_edge(graph)
for i in graph.nodes:
    print("{0} -- {1}".format(i, " -- ".join(str(friend) for friend in i.friends)))

gr = nx.Graph()
gr.add_nodes_from(graph.nodes)
gr = binding(graph, gr)
print(gr.number_of_edges())


draw(gr, graph)
