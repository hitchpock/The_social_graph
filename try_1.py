import matplotlib.pyplot as plt
import networkx as nx
from random import randint, shuffle

def random_edge(graph):
    for index in graph.node:
        for jindex in graph.node:
            if index != jindex and randint(0, 4) == 1 and ((jindex, index) in graph.edges) == False:
                graph.add_edge(index, jindex)
    return graph

names = []
with open('names.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        names.append(line[:-1])
shuffle(names)
names = names[:19]
#print(names)
graph = nx.Graph()

graph.add_nodes_from(names)

#graph.add_edge(1, 3)
graph = random_edge(graph)
print(graph.number_of_edges())
print(graph.number_of_nodes())
pos = nx.circular_layout(graph)

nx.draw_networkx_nodes(graph, pos, node_size=300)
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges)

nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif', font_color='blue')
plt.axis('off')
plt.show()