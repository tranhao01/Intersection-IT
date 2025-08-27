import matplotlib.pyplot as plt
import networkx as nx

# Các nút chính
nodes = {
    "Y học": (0, 0),
    "AI": (1, 1),
    "Công nghệ sinh học": (-1, 1),
    "Nano": (-1, -1),
    "IoT & Wearables": (1, -1),
    "Robot & In 3D": (0, -1.8)
}

# Tạo đồ thị
G = nx.Graph()
for node in nodes:
    G.add_node(node)

# Liên kết tất cả công nghệ với "Y học"
for node in nodes:
    if node != "Y học":
        G.add_edge("Y học", node)

# Vẽ sơ đồ
plt.figure(figsize=(8, 8))
nx.draw_networkx_nodes(G, nodes, node_size=2500, node_color="lightblue", edgecolors="black")
nx.draw_networkx_edges(G, nodes, width=2, alpha=0.7)
nx.draw_networkx_labels(G, nodes, font_size=10, font_family="sans-serif")

plt.title("Giao điểm: Y học + Công nghệ", fontsize=14, fontweight="bold")
plt.axis("off")
plt.show()
