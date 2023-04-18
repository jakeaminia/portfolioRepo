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


def find_expanded_requirements(node: str, matrix: dict) -> set:
    result = set()
    if not matrix.get(node):
        return result
    for element in matrix.get(node):
        result.add(element)
        for item in find_expanded_requirements(element, matrix):
            result.add(item)
    return result


def get_heights(matrix: dict):
    new_dict = dict()
    result = list()
    result2 = list()
    for key in matrix.keys():
        # new_dict[key] = find_height(key, matrix, dict())
        new_dict[key] = len(find_expanded_requirements(key, matrix))
    while new_dict:
        lowest_node = min(new_dict, key=new_dict.get)
        node_height = new_dict.pop(lowest_node)
        result.append(lowest_node)
        result2.append(node_height)
    return result, result2


def print_matrix(matrix: dict):
    with open('result_doc.txt', 'w') as result_doc:
        arr, arr2 = get_heights(matrix)
        requisite_map = dict()
        for i, value in enumerate(arr):
            num_prerequisites = arr2[i]
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
