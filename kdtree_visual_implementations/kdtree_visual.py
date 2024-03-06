import pandas as pd
import random

# Import data, retrieve only coordinate information
data = pd.read_csv('house_chunked_random.csv', sep=',')[['X', 'Y', 'Z']]

# Function that creates unique id
node_ids = set()
def generate_node_id(node_ids):
    new_id = random.randint(1, 1e5)
    while new_id in node_ids:
        new_id = random.randint(1, 1e5)
    node_ids.add(new_id)
    return new_id

# Node structure for k-d tree
class Node:
    def __init__(self, point, id, depth, left=None, right=None):
        self.point = point
        self.id = id
        self.depth = depth
        self.left = left
        self.right = right

# Adjust the build_kdtree function to limit depth
def build_kdtree(points, depth=0, max_depth=4):
    if not points or depth >= max_depth:  # Stop building more levels after reaching max_depth
        return None

    k = len(points[0]) - 1  # Assuming the last column is the point ID
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    node_id = generate_node_id(node_ids)

    return Node(
        point=points[median][:-1],
        id=points[median][-1],
        depth=depth,
        left=build_kdtree(points[:median], depth + 1, max_depth),
        right=build_kdtree(points[median + 1:], depth + 1, max_depth)
    )

# Adjust the traverse_kdtree function to consider the depth limit
def traverse_kdtree(node, nodes=[], edges=[], degree_count={}, depth=0, max_depth=4):
    if node and depth < max_depth:
        nodes.append({'Id': node.id, 'Depth': node.depth})
        degree_count[node.id] = degree_count.get(node.id, 0)

        if node.left:
            edges.append({'Source': node.id, 'Target': node.left.id, 'Type': 'Directed'})
            degree_count[node.id] += 1
            traverse_kdtree(node.left, nodes, edges, degree_count, depth + 1, max_depth)

        if node.right:
            edges.append({'Source': node.id, 'Target': node.right.id, 'Type': 'Directed'})
            degree_count[node.id] += 1
            traverse_kdtree(node.right, nodes, edges, degree_count, depth + 1, max_depth)

    return nodes, edges, degree_count

# The rest of the code remains unchanged


# Main function to build k-d tree and output CSV files including node degrees
def main():
    points_with_id = data.assign(Id=data.index).values.tolist()
    kdtree = build_kdtree(points_with_id)
    nodes_data, edges_data, degree_count = traverse_kdtree(kdtree)
    nodes_df = pd.DataFrame(nodes_data)
    edges_df = pd.DataFrame(edges_data)

    # Apply degree information and reorder columns
    nodes_df['Degree'] = nodes_df['Id'].apply(lambda x: degree_count.get(x, 0))
    nodes_df = nodes_df[['Id', 'Degree', 'Depth']]  # Adjust column order here

    nodes_df.to_csv('kdtree_nodes.csv', index=False)
    edges_df.to_csv('kdtree_edges.csv', index=False)
    print('Node and edge data saved to kdtree_nodes.csv and kdtree_edges.csv')

if __name__ == '__main__':
    main()
