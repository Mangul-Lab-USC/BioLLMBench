import matplotlib.pyplot as plt
import networkx as nx

# Define a directed graph
G = nx.DiGraph()

# Adding nodes with their labels; these will correspond to the various steps and elements in the user's datastream
nodes = {
    'Math': 'Mathematical\nProblem Solving',
    'Coding': 'Coding',
    'Visualization': 'Visualization',
    'Domain_Knowledge': 'Domain Knowledge',
    'ChatGPT': 'ChatGPT',
    'Bard': 'Bard',
    'Llama': 'LLaMA',
    'Run_Same': 'Same Window\n(20x)',
    'Run_New': 'New Window\n(20x)',
    'Metrics': 'Evaluation\nMetrics',
    'Summary': 'Results\nSummary'
}

# Add nodes to the graph with subset information for multipartite layout
for node in nodes:
    G.add_node(node, label=nodes[node], subset=int(node in ['ChatGPT', 'Bard', 'Llama']))

# Define the edges connecting the nodes
edges = [
    ('Math', 'ChatGPT'), ('Coding', 'ChatGPT'), ('Visualization', 'ChatGPT'), ('Domain_Knowledge', 'ChatGPT'),
    ('Math', 'Bard'), ('Coding', 'Bard'), ('Visualization', 'Bard'), ('Domain_Knowledge', 'Bard'),
    ('Math', 'Llama'), ('Coding', 'Llama'), ('Visualization', 'Llama'), ('Domain_Knowledge', 'Llama'),
    ('ChatGPT', 'Run_Same'), ('ChatGPT', 'Run_New'),
    ('Bard', 'Run_Same'), ('Bard', 'Run_New'),
    ('Llama', 'Run_Same'), ('Llama', 'Run_New'),
    ('Run_Same', 'Metrics'), ('Run_New', 'Metrics'),
    ('Metrics', 'Summary')
]

# Add edges to the graph
G.add_edges_from(edges)

# Generate positions for the nodes using multipartite layout
pos = nx.multipartite_layout(G, subset_key='subset')

# Draw the graph with customized node and edge appearance
nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), node_size=4500, 
        node_color='lightblue', font_size=8, edge_color='black', arrowstyle='-|>', 
        arrowsize=25, width=1.5)

# Set the figure size, turn off the axis and apply a tight layout
plt.figure(figsize=(12, 8))
plt.axis('off')
plt.tight_layout()

# Show the plot
plt.show()
