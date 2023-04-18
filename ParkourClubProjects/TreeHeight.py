# Input file is loosely formatted because it was derived from a copy-and-paste of a google doc table
def parse_google_doc_table(doc_name: str):
    matrix = dict()
    current_node = None
    adjacent_nodes = list()
    with open(doc_name, 'r') as doc_file:
        for line in doc_file:
            if not line.strip():
                if current_node and not adjacent_nodes:
                    matrix[current_node] = adjacent_nodes
                current_node = None
                adjacent_nodes = list()
                continue
            if not current_node:
                current_node = line.strip()
                continue
            adjacent_nodes.extend(line.strip().split(', '))
            matrix[current_node] = adjacent_nodes
    return matrix


def get_all_prerequisites(node: str, matrix: dict) -> set:
    result = set()
    if not matrix.get(node):
        return result
    for prerequisite in matrix.get(node):
        result.add(prerequisite)
        for second_order_prerequisite in get_all_prerequisites(prerequisite, matrix):
            result.add(second_order_prerequisite)
    return result

# Defining "node height" as the total number of prerequisites for a given node
def get_heights(matrix: dict):
    node_heights_dict = dict()
    sorted_nodes = list()
    sorted_nodes_heights = list()
    for node in matrix.keys():
        node_heights_dict[node] = len(get_all_prerequisites(node, matrix))
    while node_heights_dict:
        min_node = min(node_heights_dict, key=node_heights_dict.get)
        min_node_height = node_heights_dict.pop(min_node)
        sorted_nodes.append(min_node)
        sorted_nodes_heights.append(min_node_height)
    return sorted_nodes, sorted_nodes_heights


def print_matrix(matrix: dict):
    with open('result_doc.txt', 'w') as result_doc:
        nodes, node_heights = get_heights(matrix)
        requisite_map = dict()
        for i, value in enumerate(nodes):
            num_prerequisites = node_heights[i]
            if num_prerequisites not in requisite_map:
                requisite_map[num_prerequisites] = list()
            requisite_map[num_prerequisites].append((value, matrix.get(value)))
        for index, value in enumerate(sorted(requisite_map.keys())):
            items = requisite_map.get(value)
            # print(f'Level {index}:\n')
            result_doc.write(f'Level {index}:\n\n')
            for item in items:
                pre_str = ''
                if not item[1]:
                    pre_str += 'None1'
                else:
                    for pre in item[1]:
                        pre_str += f'{pre}, '
                # print(f'\t{item[0]} ({pre_str.strip()[0:-1]})')
                result_doc.write(f'\t{item[0]} ({pre_str.strip()[0:-1]})\n')

            # print('')
            result_doc.write('\n')


FILE_NAME = 'table_doc.txt'
adjacency_matrix = parse_google_doc_table(FILE_NAME)
print_matrix(adjacency_matrix)
