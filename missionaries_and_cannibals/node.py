#   Adaptado e baseado nesse reposotorio https://github.com/aroques/missionaries-and-cannibals


class Node:


    """A classe nó na arvore , contém o ponteiro para o sucessor e para o estado atual do nó."""

    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.state == other.state and self.action == other.action \
                   and self.depth == other.depth and self.parent == other.parent
        else:
            return False

    def expand(self, problem):#Função para expandir o nó
        return [self.child_node(problem, action)
                for action in problem.actions(self)]

    def child_node(self, problem, action):#
        return problem.result(self, action)

    @property
    def solution(self):
        return [node.action for node in self.path[1:]]

    @property
    def path(self):#Função com  a questão do caminho percorrido na Arvoré
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
