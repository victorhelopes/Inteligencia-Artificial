import util,mdp
from learningAgents.py import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() 
        "*** YOUR CODE HERE ***"

        self.values = util.Counter() # A Counter is a dict with default 0
        states = mdp.getStates()

        for i in range(0,iterations):
            novo_valor = util.Counter()
            for state in states:
                acao = self.getAction(state)
                if acao is not None:
                    novo_valor[state] = self.getQValue(state, acao)
            self.values = novo_valor
    def getValue(self, state):
            
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        total = 0
        TransitionStatesAndProbs = self.mdp.getTransitionStatesAndProbs(state,action)
        
        for i in TransitionStatesAndProbs:
            estadoT = i[0]
            probabilidade = i[1]
            reward = self.mdp.getReward(state,action,estadoT)
            value = self.getValue(estadoT)
            total = probabilidade * (reward + (self.discount * value)) 
            return total
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        if(self.mdp.isTerminal(state)):
            return None
        else:
            acoes = self.mdp.getPossibleActions(state)
            max_value = self.getQValue(state,acoes[0])
            max_action = acoes[0]
            for i in acoes:
                value = self.getQValue(state,i)
                if (max_value <= value):
                    max_value = value
                    max_action = i
            return max_action
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

