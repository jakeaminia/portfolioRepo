class node:
    def __init__(self, name, prerequisites):
        self._name = name
        self._direct_prerequisites = set(prerequisites)
        self._extended_prerequisites = set()
        self._height = None
        self._count_direct_prerequisites = None

    def add_direct_prerequisite(self, prerequisite):
        self._direct_prerequisites.append(prerequisite)

    def get_direct_prerequisites(self):
        return self._direct_prerequisites

    def get_extended_prerequisites(self):
        return self._extended_prerequisites

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def set_height(self):
        print('re-calculate extended prerequisites')
        print('re-calculate height')
        for prerequisite in self._direct_prerequisites:
            self._extended_prerequisites.add(prerequisite)
            prerequisite.set

    def set_count_direct_prerequisites(self):
        self._count_direct_prerequisites = len(self._direct_prerequisites)
    
    def get_count_direct_prerequisites(self):
        return self._count_direct_prerequisites

    def __str__(self):
        formatted_direct_prerequisites = ''
        for index, prerequisite in enumerate(self._direct_prerequisites):
            formatted_direct_prerequisites += f'{prerequisite}'
            if index < self._count_direct_prerequisites:
                formatted_direct_prerequisites += ', '
        result = f'{self._name} ({formatted_direct_prerequisites})'


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
        sorted_nodes, sorted_nodes_heights = get_heights(matrix)
        # node_height_levels maps height numbers to a list of (node, [node prerequisites]) for nodes of that height in sorted_nodes
        node_height_levels = dict()
        for i, value in enumerate(sorted_nodes):
            num_prerequisites = sorted_nodes_heights[i]
            if num_prerequisites not in node_height_levels:
                node_height_levels[num_prerequisites] = list()
            node_height_levels[num_prerequisites].append(
                (value, matrix.get(value)))
        for index, value in enumerate(sorted(node_height_levels.keys())):
            items = node_height_levels.get(value)
            result_doc.write(f'Level {index}:\n\n')
            for item in items:
                pre_str = ''
                if not item[1]:
                    pre_str += 'None.'
                else:
                    for pre in item[1]:
                        pre_str += f'{pre}, '
                result_doc.write(f'\t{item[0]} ({pre_str.strip()[0:-1]})\n')

            result_doc.write('\n')


FILE_NAME = 'table_doc.txt'
adjacency_matrix = parse_google_doc_table(FILE_NAME)
print_matrix(adjacency_matrix)
