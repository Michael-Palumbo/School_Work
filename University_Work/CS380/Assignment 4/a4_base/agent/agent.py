import json
import os
import random

from .state import State


class Q_State(State):
    '''Augments the game state with Q-learning information'''

    def __init__(self, string):
        super().__init__(string)

        # key stores the state's key string (see notes in _compute_key())
        self.key = self._compute_key()

    def _compute_key(self):
        '''
        Returns a key used to index this state.

        The key should reduce the entire game state to something much smaller
        that can be used for learning. When implementing a Q table as a
        dictionary, this key is used for accessing the Q values for this
        state within the dictionary.
        '''

        # this simple key uses the 3 object characters above the frog
        # and combines them into a key string
        return ''.join([
            # 1 Block infront, 3 wide
            self.get(self.frog_x - 1, self.frog_y - 1) or '_',
            self.get(self.frog_x, self.frog_y - 1) or '_',
            self.get(self.frog_x + 1, self.frog_y - 1) or '_',
            # 2 Blcoks infront, 3 wide
            # self.get(self.frog_x - 1, self.frog_y - 2) or '_',
            # self.get(self.frog_x, self.frog_y - 2) or '_',
            # self.get(self.frog_x + 1, self.frog_y - 2) or '_',
            # Block left and right front frog
            self.get(self.frog_x - 1, self.frog_y) or '_',
            self.get(self.frog_x + 1, self.frog_y) or '_',
            # 1 Block behind, 3 wide
            self.get(self.frog_x - 1, self.frog_y + 1) or '_',
            self.get(self.frog_x, self.frog_y + 1) or '_',
            self.get(self.frog_x + 1, self.frog_y + 1) or '_',
        ])

    # I feel like what's holding the code back is the reward system, tho I don't know what I did wrong
    def reward(self):
        '''Returns a reward value for the state.'''

        if self.at_goal:
            return self.score
        elif self.is_done:
            return -15
        else:
            tally = 0
            #distance from goal
            tally += self.score - self.frog_y
            #if car is coming at it
            tally += -2 if self.get(self.frog_x-1,self.frog_y) == '>' else 0
            tally += -2 if self.get(self.frog_x+1,self.frog_y) == '<' else 0

            #if log infront approaching
            tally += +2 if self.get(self.frog_x-1,self.frog_y-1) == ']' else 0
            tally += +2 if self.get(self.frog_x+1,self.frog_y-1) == '[' else 0

            return tally


class Agent:

    def __init__(self, train=None):

        # train is either a string denoting the name of the saved
        # Q-table file, or None if running without training
        self.train = train

        # q is the dictionary representing the Q-table
        self.q = {}

        # name is the Q-table filename
        # (you likely don't need to use or change this)
        self.name = train or 'q'

        # path is the path to the Q-table file
        # (you likely don't need to use or change this)
        self.path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'train', self.name + '.json')

        self.load()

    def load(self):
        '''Loads the Q-table from the JSON file'''
        try:
            with open(self.path, 'r') as f:
                self.q = json.load(f)
            if self.train:
                print('Training {}'.format(self.path))
            else:
                print('Loaded {}'.format(self.path))
        except IOError:
            if self.train:
                print('Training {}'.format(self.path))
            else:
                raise Exception('File does not exist: {}'.format(self.path))
        return self

    def save(self):
        '''Saves the Q-table to the JSON file'''
        with open(self.path, 'w') as f:
            json.dump(self.q, f)
        return self

    def choose_action(self, state_string):

        if self.train:
            action = self.q_learning(state_string)
            self.save()
            return action
        else:
            return random.choice(State.ACTIONS)
        '''
        Returns the action to perform.

        This is the main method that interacts with the game interface:
        given a state string, it should return the action to be taken
        by the agent.

        The initial implementation of this method is simply a random
        choice among the possible actions. You will need to augment
        the code to implement Q-learning within the agent.
        '''
    
    prev_state = None
    prev_action = None

    def q_learning(self, state_string):

        exploration_rate = .1
        alpha = .7
        discount_rate = .99

        state = Q_State(state_string)

        exploration_threshold = random.uniform(0,1)
        if exploration_threshold > exploration_rate:
            action, *_ = self.maxValue(state)
        else: # 10% of the time it'll try to something random
            action = random.choice(State.ACTIONS)
            if not state.key in self.q:
                self.q[state.key] = dict.fromkeys(state.ACTIONS, 0)
        
        reward = state.reward()

        if self.prev_state == None:
            self.prev_state = state
            self.prev_action = action
        else:
            self.q[self.prev_state.key][self.prev_action] = (1 - alpha) * self.q[self.prev_state.key][self.prev_action] + alpha * (reward + discount_rate * self.maxDic(self.q[state.key])[1])
            self.prev_state = state
            self.prev_action = action

        return action

    def maxValue(self, q_state):
        # We have not seen this key before, so add it to the q table
        if not q_state.key in self.q:
            self.q[q_state.key] = dict.fromkeys(q_state.ACTIONS, 0)
            return random.choice(State.ACTIONS)
        else:
            return self.maxDic(self.q[q_state.key])

    def maxDic(self, state):

        maxKey = "u"
        maxVal = state[maxKey]

        for key, value in state.items():
            if maxVal < value:
                maxKey = key
                maxval = value

        return maxKey, maxVal