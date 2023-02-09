
from .utils import is_in

class Problem(object):
    


    def __init__(self, initial_state, goal=None):
     
        self.initial_state = initial_state
        self.goal = goal

    def actions(self, state):
     
        raise NotImplementedError

    def result(self, state, action):
     
        raise NotImplementedError

    def goal_is(self, state):
     
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal
