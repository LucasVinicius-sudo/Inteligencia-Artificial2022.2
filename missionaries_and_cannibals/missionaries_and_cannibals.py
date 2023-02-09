from .problem import Problem
from .node import Node
from .state import State

class MissionariesAndCannibals(Problem):


    def __init__(self):
        """Neste construtor está iniciado o estado inicial ou seja 3 missionários e 3 Canibais no mesmo lado do rio
            Além do estado desejado ou seja 3 Missionários e 3 Canibais do lado oposto ao que se começou do rio
        """

        initial_state = State((3, 3, 1))
        goal_state = State((0, 0, 0))

        self.all_possible_actions = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]

        super().__init__(initial_state, goal_state)

    def actions(self, node):
        """Retorna as ações que podem ser executadas no dado
         estado. O resultado normalmente seria uma lista, mas se houver
         muitas ações, considere entregá-las uma de cada vez em um
         iterador, em vez de criá-los todos de uma vez."""
        all_nodes = [self.__perform_action(node, action) for action in self.all_possible_actions]
        valid_nodes = filter(lambda n: n.state.is_valid, all_nodes)
        return [n.action for n in valid_nodes]

    def result(self, node, action):
        """Retorne o nó resultante da execução do dado
         ação no estado dado. A ação deve ser uma das
         self.actions(estado)."""
        if action not in self.actions(node):
            raise Exception('action not in actions!')

        return self.__perform_action(node, action)

    @staticmethod
    def __perform_action(node, action):
        """Retorne o nó resultante da execução do dado
         ação no estado dado."""
        if node.depth % 2 == 0:
            state = node.state - action
        else:
            state = node.state + action

        return Node(state, node, action)
