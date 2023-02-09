
from .utils import is_in

class Problem(object):
    """A classe abstrata para um problema formal. Você deve criar uma subclasse
       isso e implementar as ações e resultados dos métodos, e possivelmente
       __init__, goal_test e path_cost. Então você criará instâncias
       da sua subclasse e resolva-os com as várias funções de pesquisa."""


    def __init__(self, initial_state, goal=None):
      """O construtor especifica o estado inicial e possivelmente um objetivo
         estado, se houver um objetivo único. O construtor da sua subclasse pode adicionar
         outros argumentos"""
        self.initial_state = initial_state
        self.goal = goal

    def actions(self, state):
      """Retorna as ações que podem ser executadas no dado
         estado. O resultado normalmente seria uma lista, mas se houver
         muitas ações, considere entregá-las uma de cada vez em um
         iterador, em vez de criá-los todos de uma vez."""
        raise NotImplementedError

    def result(self, state, action):
      """Retorna o estado resultante da execução do dado
         ação no estado dado. A ação deve ser uma das
         self.actions(estado)."""
        raise NotImplementedError

    def goal_is(self, state):
      """Retorna True se o estado for uma meta. O método padrão compara o
         estado para self.goal ou verifica o estado em self.goal se for um
         list, conforme especificado no construtor. Substitua este método se
         comparar com um único objetivo pessoal não é suficiente."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal
