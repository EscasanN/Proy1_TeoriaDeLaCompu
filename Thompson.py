from Classes import *

def BasicAutomata(char, counter):
    initial = State(counter, False)
    counter += 1
    final = State(counter, True)
    counter += 1

    initial.trans[char] = final

    new_auto = Automata(initial, final)
    
    return new_auto, counter

def PipeAutomata(auto1, auto2, counter):
    initial = State(counter, False)
    counter += 1
    final = State(counter, True)
    counter += 1

    auto1.final.accept = False
    auto2.final.accept = False

    initial.epsilon_trans.append(auto1.initial)            
    initial.epsilon_trans.append(auto2.initial)            
    auto1.final.epsilon_trans.append(final)
    auto2.final.epsilon_trans.append(final)
    
    new_auto = Automata(initial, final)

    return new_auto, counter

def KleenAutomata(auto, counter):
    initial = State(counter, False)
    counter += 1
    final = State(counter, True)
    counter += 1

    auto.final.accept = False

    initial.epsilon_trans.append(auto.initial)
    auto.final.epsilon_trans.append(auto.initial)
    auto.final.epsilon_trans.append(final)

    initial.epsilon_trans.append(final)

    new_auto = Automata(initial, final)

    return new_auto, counter

def ConcatAutomata(auto1, auto2, counter):
    auto1.final.accept = False
    auto1.final.epsilon_trans.append(auto2.initial)

    return Automata(auto1.initial, auto2.final)

def Thompson(postfix):
    stack = []
    counter = 0
    concat = False

    for c in postfix:
        if not concat:
            if c == "*":
                auto = stack.pop()
                new_auto, counter = KleenAutomata(auto, counter)
                stack.append(new_auto)
            elif c == "|":
                auto1 = stack.pop()
                auto2 = stack.pop()

                new_auto, counter = PipeAutomata(auto1, auto2, counter)
            
                stack.append(new_auto)
            elif c == ".":
                if len(stack) > 1:
                    auto1 = stack.pop()
                    auto2 = stack.pop()

                    new_auto = ConcatAutomata(auto2, auto1, counter)

                    stack.append(new_auto)
                
                else:
                    concat = True

            else:
                auto, counter = BasicAutomata(c, counter)

                stack.append(auto)
        else:
            auto1 = stack.pop()
            auto2, counter = BasicAutomata(c, counter)

            new_auto = ConcatAutomata(auto1, auto2, counter)

            stack.append(new_auto)
            concat = False

    nfa = stack.pop()

    return nfa
