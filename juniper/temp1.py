from abc import ABCMeta, abstractmethod


class Node(object):
    __metaclass__ = ABCMeta
    """
    Node object
    """

    def __init__(self):
        self.parent_node = None
        self.child_nodes = []

    def add_child_node(self, node):
        """
        Add child node
        :param node:
        :type node: Node
        :return:
        """
        self.child_nodes.append(node)
        node.parent_node = self

    @abstractmethod
    def step_up(self, *args, **kwargs):
        pass

    @abstractmethod
    def step_down(self, *args, **kwargs):
        pass


class NodeOperations(object):
    @staticmethod
    def path_to_the_root(node):
        """
        Calculate path to the root node
        :param node:
        :type node: Node
        :return:
        """
        path = [node]
        while node.parent_node:
            node = node.parent_node
            path.append(node)
        return path

    @staticmethod
    def calculate_route_steps(source_node, dest_node):
        """
        Calculate route between two nodes,
        :param source_node:
        :type source_node: Node
        :param dest_node:
        :type dest_node: Node
        :return: List of functions, needed to call to get from source to dest node
        :rtype: list
        """
        source_node_root_path = NodeOperations.path_to_the_root(source_node)
        print(source_node_root_path)
        dest_node_root_path = NodeOperations.path_to_the_root(dest_node)
        print(dest_node_root_path)

        def down_steps(down_route):
            steps = []
            for node in down_route:
                steps.append(node.step_down)
            return steps

        def up_steps(up_route):
            steps = []
            for node in up_route:
                steps.append(node.step_up)
            return steps

        index = 0
        while True:
            if source_node_root_path[index] in dest_node_root_path:
                dest_index = len(source_node_root_path) - index
                return down_steps(source_node_root_path[:index]) + up_steps(dest_node_root_path[::-1][dest_index:])
            else:
                index += 1

class Prompt(Node):
    DEFINED_PROMPTS = []
    def __init__(self, name, enter_command, exit_command, default_action=None, expected_map=None, error_map=None):
        super(Prompt, self).__init__()
        self._name = name
        self._enter_command = enter_command
        self._exit_command = exit_command
        self._default_actions = default_action
        self._expected_map = expected_map
        self._error_map = error_map

    def add_prompt(self, prompt):
        self.add_child_node(prompt)
        Prompt.DEFINED_PROMPTS.append(prompt)

    def step_down(self, session):
        session.hardware_expect()

    def step_up(self):
        print('enter ' + str(self._name))


if __name__ == '__main__':
    pp1 = Prompt(1, 'as', 'sas', Prompt(2, 'dd', 'gg', Prompt(4, 'fdfd', 'gfgq')), Prompt(3, 'ewe', '55'))
    pp2 = Prompt(2)
    pp3 = Prompt(3)
    pp4 = Prompt(4)
    pp5 = Prompt(5)
    pp6 = Prompt(6)

    pp1.add_child_node(pp2)
    pp2.add_child_node(pp3)
    pp3.add_child_node(pp4)
    pp4.add_child_node(pp5)
    pp3.add_child_node(pp6)
    steps = NodeOperations.calculate_route_steps(pp2, pp6)
    map(lambda x: x(), steps)




    # dd = pp1.get_path_to_the_Node(pp6)
    # print(dd)
