from ShuntingYard import ShuntingYard
from Thompson import *
from Classes import *
from Subconjuntos import *

from graphviz import Digraph

print("hi")
file = open("input.txt", "r")

def draw_automata(initial, states, transitions, accepts, name):
    dot = Digraph()

    dot.node(str(initial), shape="ellipse")

    for state in states:
        dot.node(str(state), shape="circle")

    for transition in transitions:
        state1 = transition[0]
        sign = transition[1]
        state2 = transition[2]

        dot.edge(str(state1), str(state2), label=sign)
    
    for accept in accepts:
        dot.node(str(accept), shape="doublecircle")
    
    dot.render(name, format="png", view=True)

def save_states(state, states, transitions, accepts):
    if state.id not in states:
        states.append(state.id)
    
        if state.accept:
            accepts.append(state.id)
        
        for char, new_state in state.trans.items():
            transitions.append([state.id, char, new_state.id])
            save_states(new_state, states, transitions, accepts)
        
        for eps in state.epsilon_trans:
            transitions.append([state.id, "ɛ", eps.id])
            save_states(eps, states, transitions, accepts)

for line in file:
    print(line)
    parts = line.split()
    postfix2 = ShuntingYard(parts[0])
#    postfix = ShuntingYard("abb(a|b)*")
    postfix = "bb|*a.b.b.ab|*."
    print(postfix)
    print(postfix2)

    nfa = Thompson(postfix)

    initial_state = nfa.initial
    states = []
    transitions = []
    accepts = []

    save_states(initial_state, states, transitions, accepts)
    
    draw_automata(initial_state.id, states, transitions, accepts, "nfa")

"""     print (states)
    print (transitions)
    print (accepts)

    signs = []
    for c in postfix:
        if c not in ["|", "*", "."] and c not in signs:
            signs.append(c)

    dfa = convert_to_dfa(nfa, signs)

    dfa_initial_state = dfa.initial
    dfa_states = []
    dfa_transitions = []
    dfa_accepts = []

    print("=======================")

    save_states(dfa_initial_state, dfa_states, dfa_transitions, dfa_accepts)
    
    print(dfa_states)
    print(dfa_transitions)
    print(dfa_accepts) """

#    draw_automata(dfa_initial_state.id, dfa_states, dfa_transitions, dfa_accepts, "dfa")