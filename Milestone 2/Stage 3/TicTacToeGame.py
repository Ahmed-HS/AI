import random
import math

class TicTacToe:

    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        """Make a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        elif self.board[position] != " " and player is " " :
            self.board[position] = player
            return True
        else:
            print("Invalid Move")
            return False

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def minimax(self, node, depth, player):
        """
        Recursively analyze every possible game state and choose
        the best move location.
        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")

        """
        if depth == 9 or self.gameOver():
            Winner = self.checkWin()
            if Winner == "O":
                return 10 - depth
            elif Winner == "X":
                return -10 + depth
            else:
                return 0
        
        OpenMoves = self.availableMoves()
        Result = 0
        if player == "O":
            Result = -10
            for Move in OpenMoves:
                node.makeMove(Move,player)
                Result = max(Result,self.minimax(node,depth+1,changePlayer(player)))
                node.makeMove(Move," ")

        elif player == "X":
            Result = 10
            for Move in OpenMoves:
                node.makeMove(Move,player)
                Result = min(Result,self.minimax(node,depth+1,changePlayer(player)))
                node.makeMove(Move," ")

        return Result


    def AlphaBeta(self, node, depth, player ,Alpha,Beta):
        """
        Recursively analyze every possible game state and choose
        the best move location.
        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")

        """
        if depth == 9 or self.gameOver():
            Winner = self.checkWin()
            if Winner == "O":
                return 10 - depth
            elif Winner == "X":
                return -10 + depth
            else:
                return 0
        
        OpenMoves = self.availableMoves()
        Result = 0
        if player == "O":
            Result = -10
            for Move in OpenMoves:
                node.makeMove(Move,player)
                Result = max(Result,self.AlphaBeta(node,depth + 1,changePlayer(player),Alpha,Beta))
                Alpha = max(Alpha,Result)
                node.makeMove(Move," ")
                if Alpha >= Beta:
                    return Alpha

        elif player == "X":
            Result = 10
            for Move in OpenMoves:
                node.makeMove(Move,player)
                Result = min(Result,self.AlphaBeta(node,depth + 1,changePlayer(player),Alpha,Beta))
                Beta = min(Beta,Result)
                node.makeMove(Move," ")
                if Alpha >= Beta:
                    return Beta

        return Result




def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"


def make_best_move(board, depth, player):
    """
    Controllor function to initialize minimax and keep track of optimal move choices
    board - what board to calculate best move for
    depth - how far down the tree to go
    player - who to calculate best move for (Works ONLY for "O" right now)
    """
    neutralValue = 0
    choices = []
    print(depth)
    for move in board.availableMoves():
        board.makeMove(move, player)
        Alpha = -10
        Beta = 10
        moveValue = board.AlphaBeta(board,depth,changePlayer(player),Alpha,Beta)
        board.makeMove(move, " ")

        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    print("choices: ", choices)

    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.availableMoves())


# Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()
    while game.gameOver() == False:

        isValid = False
        while not isValid:
            person_move = int(input("You are X: Choose number from 1-9: "))
            isValid =  game.makeMove(person_move - 1, "X")
        game.show()

        if game.gameOver() == True:
            break

        print("Computer choosing move...")
        ai_move = make_best_move(game, -1, "O")
        game.makeMove(ai_move, "O")
        game.show()

print("Game Over. " + game.whoWon() + " Wins")
