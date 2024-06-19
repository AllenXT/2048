from __future__ import absolute_import, division, print_function
import copy, random
from game import Game

MOVES = {0: 'up', 1: 'left', 2: 'down', 3: 'right'}
MAX_PLAYER, CHANCE_PLAYER = 0, 1 

# Tree node. To be used to construct a game tree. 
class Node: 
    # Recommended: do not modify this __init__ function
    def __init__(self, state, player_type):
        self.state = (state[0], state[1])

        # to store a list of (direction, node) tuples
        self.children = []

        self.player_type = player_type

    # returns whether this is a terminal state (i.e., no children)
    def is_terminal(self):
        return self.children == []

# AI agent. Determine the next move.
class AI:
    # Recommended: do not modify this __init__ function
    def __init__(self, root_state, search_depth=3): 
        self.root = Node(root_state, MAX_PLAYER)
        self.search_depth = search_depth
        self.simulator = Game(*root_state)

    # Useful functions: 
    # self.simulator.current_state, self.simulator.set_state, self.simulator.move

    def build_tree(self, node = None, depth = 0):
        # up to the given depth
        if depth == 0:
            return
        
        self.simulator.set_state(*node.state)
        # player
        if node.player_type == MAX_PLAYER:
            prev_state = copy.deepcopy(self.simulator.current_state())
            for action in MOVES:
                if self.simulator.move(action):
                    curr_state = self.simulator.current_state()
                    node.children.append((action, Node(curr_state, CHANCE_PLAYER)))
                self.simulator.set_state(*prev_state)
     
        # computer
        if node.player_type == CHANCE_PLAYER:
            prev_state = copy.deepcopy(self.simulator.current_state())
            open_tiles = self.simulator.get_open_tiles()     
            for i, j in open_tiles:
                curr_state = self.simulator.current_state()
                child_node = Node(curr_state, MAX_PLAYER)
                child_node.state[0][i][j] = 2
                node.children.append((None, child_node))
                self.simulator.set_state(*prev_state)

        for _, child_node in node.children:
            self.build_tree(child_node, depth-1)

    # Return a (best direction, expectimax value) tuple if node is a MAX_PLAYER
    # Return a (None, expectimax value) tuple if node is a CHANCE_PLAYER
    def expectimax(self, node = None):
        # "terminal"
        if node.is_terminal():
            return None, node.state[1]
        
        # player
        if node.player_type == MAX_PLAYER:
            best_val = float('-inf')
            for direction, child_node in node.children:
                _, child_val = self.expectimax(child_node)
                if child_val >= best_val:
                    best_val = child_val
                    best_dir = direction
            return best_dir, best_val
            
        # computer
        if node.player_type == CHANCE_PLAYER:
            exp_val = 0
            # prob = 1 / len(node.children)
            for _, child_node in node.children:
                _, child_val = self.expectimax(child_node)
                exp_val += child_val / (len(node.children))
            return None, exp_val

    # Return decision at the root
    def compute_decision(self):
        self.build_tree(self.root, self.search_depth)
        direction, _ = self.expectimax(self.root)
        return direction

