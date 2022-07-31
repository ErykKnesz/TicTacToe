STARTER_BOARD = """
   | _ | _ | _ |
   | _ | _ | _ |
   | _ | _ | _ |
"""

cells = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
row_1 = [' ', ' ', ' ']
row_2 = [' ', ' ', ' ']
row_3 = [' ', ' ', ' ']

letters_value = {
    "a": 1,
    "b": 2,
    "c": 3
}

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{self.name}"


class TicTacToeGame:
    def __init__(self, player_x=Player("X"), player_o=Player("O")):
        self.player_x = player_x
        self.player_o = player_o
        self.current_player = None
        self.board = [row_1, row_2, row_3]
        self.game_on = False

    def display_board(self):
        print("-------------")
        for row in self.board:
            print(f"| {' | '.join(row)} |")
            print("-------------")

    def update_board(self, coord):
        if coord[0] == "a":
            index = 0
        elif coord[0] == "b":
            index = 1
        else:
            index = 2
        if coord[1] == 1:
            self.board[0][index] = self.current_player.name
        elif coord[1] == 2:
            self.board[1][index] = self.current_player.name
        else:
            self.board[2][index] = self.current_player.name

    def ask_for_coordinates(self):
        col = input("Enter Column (a, b, c): ").lower()
        while True:
            try:
                row = input("Enter Row (1, 2, 3): ").lower()
                row = int(row)
                break
            except ValueError:
                continue
        return col, row

    def coordinates_valid(self, coord):
        if coord in cells:
            return True
        return False

    def is_winner(self):
        col_1 = [row[0] for row in self.board]
        col_2 = [row[1] for row in self.board]
        col_3 = [row[2] for row in self.board]
        slant_1 = []
        slant_2 = []
        last_item = len(self.board) - 1
        for i in range(len(self.board)):
            try:
                a = self.board[i][i]
                b = self.board[i + 1][i + 1]
                c = self.board[i + 2][i + 2]
                slant_1.extend([a, b, c])
                x = self.board[last_item][i]
                y = self.board[last_item - 1][i + 1]
                z = self.board[last_item - 2][i + 2]
                slant_2.extend([x, y, z])
            except IndexError:
                pass

        return any([all(x == self.current_player.name for x in row_1),
                   all(x == self.current_player.name for x in row_2),
                   all(x == self.current_player.name for x in row_3),
                   all(x == self.current_player.name for x in col_1),
                   all(x == self.current_player.name for x in col_2),
                   all(x == self.current_player.name for x in col_3),
                   all(x == self.current_player.name for x in slant_1),
                   all(x == self.current_player.name for x in slant_2)]
                   )

    def check_score(self):
        if self.current_player.score == 3:
            print(f"You won! Player {self.current_player.name} "
                  f"is the winner!")
            self.game_on = False
        elif not cells:
            print("It's a draw!")
            self.game_on = False

    def run_game(self):
        self.game_on = True
        self.current_player = self.player_x
        while self.game_on:
            self.display_board()
            print(f"Current player: {self.current_player}")
            coord = self.ask_for_coordinates()
            if self.coordinates_valid(f"{coord[0]}{coord[1]}"):
                cells.remove(f"{coord[0]}{coord[1]}")
                self.update_board(coord)
                if self.is_winner():
                    self.current_player.score = 3
                self.check_score()
                self.current_player = (self.player_o if self.current_player
                                       is self.player_x else self.player_x)
            else:
                print("Invalid choice! Field already taken or wrong input!")
        self.display_board()


game = TicTacToeGame()
game.run_game()
