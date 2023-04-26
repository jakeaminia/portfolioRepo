from operator import methodcaller

class DAGNode:
    def __init__(self, name: str):
        self._name = name
        self._direct_prerequisites = set()
        self._extended_prerequisites = set()
        self._height = None
        self._count_direct_prerequisites = None
        self._parent_dag = None

    def set_parent_dag(self, dag):
        self._parent_dag = dag

    def set_direct_prerequisites_from_string_list(self, prerequisites: list):
        for prerequisite in prerequisites:
            if not self._parent_dag.get(prerequisite):
                self._parent_dag.add(DAGNode(prerequisite))
            self._direct_prerequisites.add(self._parent_dag.get(prerequisite))
            self.set_count_direct_prerequisites()

    def add_direct_prerequisite(self, prerequisite):
        self._direct_prerequisites.append(DAGNode(prerequisite))
        self.set_count_direct_prerequisites()

    def get_direct_prerequisites(self):
        return self._direct_prerequisites

    def get_extended_prerequisites(self):
        return self._extended_prerequisites

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def set_height(self):
        for prerequisite in self._direct_prerequisites:
            self._extended_prerequisites.add(prerequisite)
            prerequisite.set_height()
            self._extended_prerequisites = self._extended_prerequisites | prerequisite.get_extended_prerequisites()
        self._height = len(self._extended_prerequisites)

    def set_count_direct_prerequisites(self):
        self._count_direct_prerequisites = len(self._direct_prerequisites)

    def get_count_direct_prerequisites(self):
        return self._count_direct_prerequisites

    def __str__(self):
        formatted_direct_prerequisites = ''
        for index, prerequisite in enumerate(self._direct_prerequisites):
            formatted_direct_prerequisites += f'{prerequisite.get_name()}'
            self.set_count_direct_prerequisites()
            if index < self._count_direct_prerequisites - 1:
                formatted_direct_prerequisites += ', '
        result = f'{self._name} [{self._height}] ({formatted_direct_prerequisites})'
        return result


class DAG:
    def __init__(self, name: str, document_name: str=None):
        self._node_dict = dict()
        self._name = name
        self._sorted_nodes = list()
        if document_name:
            current_node_name = None
            adjacent_node_names = list()
            with open(document_name, 'r') as document_file:
                for line in document_file:
                    
                    if not line.strip():

                        if current_node_name and not adjacent_node_names:
                            self.add(DAGNode(current_node_name))

                        current_node_name = None
                        adjacent_node_names = list()
                        continue
                    
                    if not current_node_name:

                        current_node_name = line.strip()
                        continue

                    if not self.get(current_node_name):
                        self.add(DAGNode(current_node_name))

                    adjacent_node_names.extend(line.strip().split(', '))

                    self.get(current_node_name).set_direct_prerequisites_from_string_list(adjacent_node_names)
            self.set_sorted_nodes()


    def add(self, node: DAGNode):
        self._node_dict[node.get_name()] = node
        node.set_parent_dag(self)

    def get(self, node: str) -> DAGNode:
        return self._node_dict.get(node, None)

    def get_node_dict(self):
        return self._node_dict

    def set_sorted_nodes(self):
        result = list()
        for node in self._node_dict.values():
            node.set_height()
            result.append(node)
        self._sorted_nodes = sorted(
            result, key=methodcaller('get_height'), reverse=False)

    def get_sorted_nodes(self):
        return self._sorted_nodes

    def __str__(self) -> str:
        result = ''
        for node in self.get_sorted_nodes():
            result += f'\t{node}\n'
        if not result:
            return f'{self._name}:\n' + '\tNo Sorted Nodes'
        return f'{self._name}:\n' + result


def dag_unit_test():
    FILE_NAME = 'ParkourClubProjects/table_doc.txt'
    test_dag = DAG('ParkourTrickingDag', FILE_NAME)
    print(test_dag)


dag_unit_test()
