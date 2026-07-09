ort random
import sys

class Minesweeper:
    def __init__(self, size=8, num_mines=10):
        self.size = size
        self.num_mines = num_mines
        self.visible_board = [[' ' for _ in range(size)] for _ in range(size)]
        self.hidden_board = [[0 for _ in range(size)] for _ in range(size)]
        self.flags = set()
        self.revealed = set()
        self.game_over = False
        self.won = False
        
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        """Randomly places mines on the hidden board."""
        mines_placed = 0
        while mines_placed < self.num_mines:
            r = random.randint(0, self.size - 1)
            c = random.randint(0, self.size - 1)
            if self.hidden_board[r][c] != '*':
                self.hidden_board[r][c] = '*'
                mines_placed += 1def _get_neighbors(self, r, c):
        """Returns valid adjacent coordinates for a cell."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    neighbors.append((nr, nc))
        return neighbors

    def _calculate_numbers(self):
        """Calculates nearby mine counts for every empty cell."""
        for r in range(self.size):
            for c in range(self.size):
                if self.hidden_board[r][c] == '*':
                    continue
                mine_count = 0
                for nr, nc in self._get_neighbors(r, c):
                    if self.hidden_board[nr][nc] == '*':
                        mine_count += 1
                self.hidden_board[r][c] = mine_count

    def print_board(self):
        """Renders the current game state to the console."""
        print("\n   " + " ".join(str(i) for i in range(self.size)))
        print("  " + "-" * (self.size * 2 + 1))
        for r in range(self.size):
            row_str = f"{r} |"
            for c in range(self.size):
                if (r, c) in self.flags:
                    cell = "F"
                elif (r, c) in self.revealed:
                    cell = str(self.hidden_board[r][c])
                else: cell = "."
                row_str += f" {cell}"
            print(row_str + " |")
        print("  " + "-" * (self.size * 2 + 1))

    def dig(self, r, c):
        """Reveals a chosen square. Triggers a chain reaction if it hits 0."""
        if (r, c) in self.revealed or (r, c) in self.flags:
            return True

        self.revealed.add((r, c))

        if self.hidden_board[r][c] == '*':
            self.game_over = True
            return False

        if self.hidden_board[r][c] == 0:
            for nr, nc in self._get_neighbors(r, c):
                if (nr, nc) not in self.revealed:
                    self.dig(nr, nc)

        # Check for victory conditions
        if len(self.revealed) == (self.size * self.size) - self.num_mines:
            self.won = True
        return True

    def toggle_flag(self, r, c):
        """Places or removes a safety flag on the board."""
        if (r, c) in self.revealed:
            return
        if (r, c) in self.flags:
            self.flags.remove((r, c))
        else:
            self.flags.add((r, c))
f main():
    print("Welcome to Python Minesweeper!")
    size = 8
    mines = 10
    game = Minesweeper(size, mines)

    while not game.game_over and not game.won:
        game.print_board()
        print(f"Flags placed: {len(game.flags)}/{mines}")
        
        try:
            action = input("Enter 'd' to dig or 'f' to flag, followed by row and col (e.g., d 0 3): ").strip().split()
            if not action or len(action) != 3:
                print("Invalid input format.")
                continue
                
            act, r, c = action[0].lower(), int(action[1]), int(action[2])
            
            if not (0 <= r < size and 0 <= c < size):
                print("Coordinates out of bounds.")
                continue
                
            if act == 'd':
                game.dig(r, c)
            elif act == 'f':
                game.toggle_flag(r, c)
            else:
                print("Unknown action. Use 'd' or 'f'.")
        except ValueError:
            print("Please enter valid integers for row and column.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting game.")
            sys.exit() 
            
# End game sequence
    game.revealed = {(r, c) for r in range(size) for c in range(size)} # Reveal everything
    game.print_board()
    
    if game.won:
        print("Congratulations! You cleared the minefield!")
    else:
        print("BOOM! You hit a mine. Game Over.")

if __name__ == "__main__":
    main()