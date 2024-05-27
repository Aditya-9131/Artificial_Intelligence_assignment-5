import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def game_over(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Check for draw
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return None
        return 'Draw'

    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

class Minimax:
    def __init__(self, game):
        self.game = game

    def evaluate(self):
        # Evaluation function for Tic-Tac-Toe
        score = 0
        # Check rows and columns
        for i in range(3):
            if self.game.board[i][0] == self.game.board[i][1] == self.game.board[i][2]:
                score += 1 if self.game.board[i][0] == 'X' else -1
            if self.game.board[0][i] == self.game.board[1][i] == self.game.board[2][i]:
                score += 1 if self.game.board[0][i] == 'X' else -1

        # Check diagonals
        if self.game.board[0][0] == self.game.board[1][1] == self.game.board[2][2]:
            score += 1 if self.game.board[0][0] == 'X' else -1
        if self.game.board[0][2] == self.game.board[1][1] == self.game.board[2][0]:
            score += 1 if self.game.board[0][2] == 'X' else -1
        return score

    def minimax(self, depth, maximizing_player, alpha, beta):
        result = self.game.game_over()
        if result is not None:
            if result == 'X':
                return 1
            elif result == 'O':
                return -1
            else:
                return 0

        if maximizing_player:
            max_eval = -math.inf
            for move in self.game.get_available_moves():
                self.game.make_move(move[0], move[1], 'X')
                eval = self.minimax(depth + 1, False, alpha, beta)
                self.game.board[move[0]][move[1]] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.game.get_available_moves():
                self.game.make_move(move[0], move[1], 'O')
                eval = self.minimax(depth + 1, True, alpha, beta)
                self.game.board[move[0]][move[1]] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self):
        best_move = None
        max_eval = -math.inf
        alpha = -math.inf
        beta = math.inf
        for move in self.game.get_available_moves():
            self.game.make_move(move[0], move[1], 'X')
            eval = self.minimax(0, False, alpha, beta)
            self.game.board[move[0]][move[1]] = ' '
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move

if __name__ == "__main__":
    game = TicTacToe()
    minimax = Minimax(game)

    while True:
        game.print_board()
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if game.make_move(row, col, 'O'):
            result = game.game_over()
            if result is not None:
                game.print_board()
                print("Game Over. Result:", result)
                break

            best_move = minimax.get_best_move()
            game.make_move(best_move[0], best_move[1], 'X')
            result = game.game_over()
            if result is not None:
                game.print_board()
                print("Game Over. Result:", result)
                break
        else:
            print("Invalid move. Try again.")
