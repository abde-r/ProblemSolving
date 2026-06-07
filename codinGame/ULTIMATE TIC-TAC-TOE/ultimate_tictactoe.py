import math
import random
import time

class MCTSNode:
    def __init__(self, state, move=None):
        self.state = state
        self.move = move

        self.wins = 0
        self.visits = 0
        self.children = []

        moves = state.get_legal_moves()
        MOVE_PRIORITY = {4: 3, 0: 2, 2: 2, 6: 2, 8: 2, 1: 1, 3: 1, 5: 1, 7: 1}
        
        def move_sorting_score(m):
            macro, micro = m
            macro_score = MOVE_PRIORITY[macro]
            micro_score = MOVE_PRIORITY[micro]
            
            if state.macro_winners[micro] != 0:
                macro_score -= 10
                
            return (macro_score, micro_score)

        moves.sort(key=move_sorting_score)
        self.untried_moves = moves
    
    def ucb1(self, parent_visits, exploration_constant=0.4):
        if self.visits == 0:
            return float('inf')
        
        exploitation_value = self.wins / self.visits
        exploration_value = exploration_constant * math.sqrt(math.log(parent_visits) / self.visits)

        return exploitation_value + exploration_value

class State:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.macro_winners = [0 for _ in range(9)]
        self.current_player = 1
        self.active_macro = None
        
        self.winning_lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # cols
            (0, 4, 8), (2, 4, 6) # diagonals
        ]
    
    def get_legal_moves(self):
        moves = []
        if self.active_macro is not None and self.macro_winners[self.active_macro] == 0:
            for micro in range(9):
                if self.board[self.active_macro][micro] == 0:
                    moves.append((self.active_macro, micro))
        else:
            for macro in range(9):
                if self.macro_winners[macro] == 0:
                    for micro in range(9):
                        if self.board[macro][micro] == 0:
                            moves.append((macro, micro))
        return moves
    
    def play_moves(self, move):
        new_state = self.clone()
        macro, micro = move
        new_state.board[macro][micro] = self.current_player

        for a, b, c in self.winning_lines:
            if  (new_state.board[macro][a] == self.current_player and
                new_state.board[macro][b] == self.current_player and
                new_state.board[macro][c] == self.current_player):
                new_state.macro_winners[macro] = self.current_player
                break
        
        if new_state.macro_winners[macro] == 0 and 0 not in new_state.board[macro]:
            new_state.macro_winners[macro] = 2
        
        new_state.active_macro = micro

        if new_state.macro_winners[new_state.active_macro] != 0:
            new_state.active_macro = None
        
        new_state.current_player *= -1
        return new_state
    
    def is_terminal(self) -> bool:
        for a, b, c in self.winning_lines:
            if self.macro_winners[a] in [1, -1] and self.macro_winners[a] == self.macro_winners[b] == self.macro_winners[c]:
                return True
        
        if 0 not in self.macro_winners:
            return True
        return False
    
    def get_winner(self):
        for a, b, c in self.winning_lines:
            if self.macro_winners[a] in [1, -1] and self.macro_winners[a] == self.macro_winners[b] == self.macro_winners[c]:
                return self.macro_winners[a]
        
        if 0 not in self.macro_winners:
            return 0
        return None
    
    def clone(self):
        new_state = State()
        new_state.board = [[cell for cell in row] for row in self.board]
        new_state.macro_winners = self.macro_winners[:]
        new_state.current_player = self.current_player
        new_state.active_macro = self.active_macro
        return new_state
    
    def get_smart_move(self, legal_moves):
        local_win_move = None
        for macro, micro in legal_moves:
            self.board[macro][micro] = self.current_player

            for a, b, c in self.winning_lines:
                if  (self.board[macro][a] == self.current_player and
                    self.board[macro][b] == self.current_player and
                    self.board[macro][c] == self.current_player):
                    if local_win_move is None:
                        local_win_move = (macro, micro)
                    
                    old_macro_winner = self.macro_winners[macro]
                    self.macro_winners[macro] = self.current_player
                    for ga, gb, gc in self.winning_lines:
                        if  (self.macro_winners[ga] == self.current_player and
                            self.macro_winners[gb] == self.current_player and
                            self.macro_winners[gc] == self.current_player):
                            self.macro_winners[macro] = old_macro_winner
                            self.board[macro][micro] = 0
                            return (macro, micro)
                    self.macro_winners[macro] = old_macro_winner
            self.board[macro][micro] = 0
        
        if local_win_move:
            return local_win_move
        
        opponent = self.current_player * -1
        local_block_move = None
        for macro, micro in legal_moves:
            self.board[macro][micro] = opponent
            for a, b, c in self.winning_lines:
                if  (self.board[macro][a] == opponent and
                    self.board[macro][b] == opponent and
                    self.board[macro][c] == opponent):
                    if local_block_move is None:
                        local_block_move = (macro, micro)
                    
                    old_macro_winner = self.macro_winners[macro]
                    self.macro_winners[macro] = opponent

                    for ga, gb, gc in self.winning_lines:
                        if (self.macro_winners[ga] == opponent and
                            self.macro_winners[gb] == opponent and
                            self.macro_winners[gc] == opponent):
                            self.macro_winners[macro] = old_macro_winner
                            self.board[macro][micro] = 0
                            return (macro, micro)
                    
                    self.macro_winners[macro] = old_macro_winner
                    break
            self.board[macro][micro] = 0
    
        if local_block_move:
            return local_block_move
        return random.choice(legal_moves)
    
    def get_positional_score(self):
        score = 0
        MACRO_WEIGHT = {4: 25, 0: 10, 2: 10, 6: 10, 8: 10, 1: 5, 3: 5, 5: 5, 7: 5}
        MICRO_WEIGHT = {4: 3, 0: 2, 2: 2, 6: 2, 8: 2, 1: 1, 3: 1, 5: 1, 7: 1}

        for m in range(9):
            if self.macro_winners[m] == 1:
                score += MACRO_WEIGHT[m] * 10
            elif self.macro_winners[m] == -1:
                score -= MACRO_WEIGHT[m] * 10
            else:
                for micro in range(9):
                    if self.board[m][micro] == 1:
                        score += MICRO_WEIGHT[micro]
                    elif self.board[m][micro] == -1:
                        score -= MICRO_WEIGHT[micro]
        return score

def to_macro_micro(opponent_row, opponent_col):
    macro_row = opponent_row // 3
    macro_col = opponent_col // 3
    macro_index = macro_row * 3 + macro_col

    micro_row = opponent_row % 3
    micro_col = opponent_col % 3
    micro_index = micro_row * 3 + micro_col

    return macro_index, micro_index

def to_global_row_col(my_macro, my_micro):
    macro_row = my_macro // 3
    macro_col = my_macro % 3
    micro_row = my_micro // 3
    micro_col = my_micro % 3

    global_row = (macro_row * 3) + micro_row
    global_col = (macro_col * 3) + micro_col

    return global_row, global_col

def advance_tree(current_root, next_state, move_played):
    if current_root is not None:
        for child in current_root.children:
            if child.move == move_played:
                return child
    return MCTSNode(next_state)

def mcts_search(root_node, max_time):
    start_time = time.time()

    while time.time() - start_time < max_time:
        node = root_node
        path = [node]

        while len(node.untried_moves) == 0 and not node.state.is_terminal():
            node = max(node.children, key=lambda child: child.ucb1(node.visits))
            path.append(node)
    
        if len(node.untried_moves) > 0 and not node.state.is_terminal():
            move = node.untried_moves.pop()
            next_state = node.state.play_moves(move)
            child_node = MCTSNode(next_state, move=move)
            node.children.append(child_node)
            path.append(child_node)
            node = child_node
    
        rollout_state = node.state.clone()
        simulation_depth = 0
        while not rollout_state.is_terminal() and simulation_depth < 30:
            legal_moves = rollout_state.get_legal_moves()
            smart_move = rollout_state.get_smart_move(legal_moves)
            rollout_state = rollout_state.play_moves(smart_move)
            simulation_depth += 1

        simulation_winner = rollout_state.get_winner()
        if simulation_winner == 1:
            base_win_val = 1.0
        elif simulation_winner == -1:
            base_win_val = 0.0
        elif simulation_winner == 0 and rollout_state.is_terminal():
            base_win_val = 0.5
        else:
            final_score = rollout_state.get_positional_score()
            base_win_val = 0.5 + (final_score / 1000.0)
            base_win_val = max(0.1, min(0.9, base_win_val))

        for i in range(len(path) - 1, -1, -1):
            current = path[i]
            current.visits += 1

            if i > 0:
                parent_in_path = path[i-1]
                if parent_in_path.state.current_player == 1:
                    current.wins += base_win_val
                else:
                    current.wins += (1.0 - base_win_val)

    best_child = max(root_node.children, key=lambda child: child.visits)
    return best_child.move

state = State()
turn_count = 0
current_node = None

# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]

    if opponent_row >= 0 and opponent_col >= 0:
        opponent_macro, opponent_micro = to_macro_micro(opponent_row, opponent_col)
        opponent_move = (opponent_macro, opponent_micro)
        state = state.play_moves((opponent_macro, opponent_micro))
        current_node = advance_tree(current_node, state, opponent_move)

    turn_count += 1
    think_time = 0.95 if turn_count == 1 else 0.09
    
    if current_node is None:
        current_node = MCTSNode(state)
    
    my_macro, my_micro = mcts_search(current_node, max_time=think_time)
    my_move = (my_macro, my_micro)
    state = state.play_moves((my_macro, my_micro))
    current_node = advance_tree(current_node, state, my_move)
    my_row, my_col = to_global_row_col(my_macro, my_micro)
    print(f"{my_row} {my_col}")