class State:
    def __init__(self, id, accept):
        self.id = id
        self.trans = {}
        self.epsilon_trans = []
        self.accept = accept

class Automata:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final
        self.states = []

    def final_state(self, id):
        self.final = State(id, True)

class DFA:
    def __init__(self):
        self.states = []
        self.initial = None
        self.final = []
        self.trans = {}
        self.signs = []