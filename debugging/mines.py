#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_mines = mines
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # Print column headers
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            # Print row header
            print(f"{y:2d}", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        # Auto-reveal adjacent cells if no nearby mines
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        # Win condition: number of unrevealed cells equals total mines
        unrevealed_count = sum(row.count(False) for row in self.revealed)
        return unrevealed_count == self.total_mines

    def play(self):
        while True:
            self.print_board()

            # Check for win condition before next move
            if self.check_win():
                self.print_board(reveal=True)
                print("\nCongratulations! You cleared the minefield and won!")
                break

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    input("Coordinates out of bounds! Press Enter to retry...")
                    continue

                if self.revealed[y][x]:
                    input("Cell already revealed! Press Enter to retry...")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\nGame Over! You hit a mine.")
                    break
            except ValueError:
                input("Invalid input. Please enter numbers only. Press Enter to retry...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
