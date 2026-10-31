"""A small, two-player command-line Tic-Tac-Toe game."""


def display_board(board: list[str]) -> None:
	"""Print the current board."""
	print()
	for row in range(3):
		cells = board[row * 3 : row * 3 + 3]
		print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
		if row < 2:
			print("----+---+----")
	print()


def has_won(board: list[str], mark: str) -> bool:
	"""Return whether mark occupies a complete row, column, or diagonal."""
	winning_lines = (
		(0, 1, 2),
		(3, 4, 5),
		(6, 7, 8),
		(0, 3, 6),
		(1, 4, 7),
		(2, 5, 8),
		(0, 4, 8),
		(2, 4, 6),
	)
	return any(all(board[position] == mark for position in line) for line in winning_lines)


def play_game() -> None:
	"""Run one game until a player wins or the board is full."""
	board = [str(number) for number in range(1, 10)]
	current_mark = "X"

	while True:
		display_board(board)
		choice = input(f"Player {current_mark}, choose a square (1-9): ").strip()

		if not choice.isdigit() or not 1 <= int(choice) <= 9:
			print("Please enter a number from 1 to 9.")
			continue

		position = int(choice) - 1
		if board[position] in ("X", "O"):
			print("That square is already taken.")
			continue

		board[position] = current_mark
		if has_won(board, current_mark):
			display_board(board)
			print(f"Player {current_mark} wins!")
			return

		if all(cell in ("X", "O") for cell in board):
			display_board(board)
			print("It's a draw!")
			return

		current_mark = "O" if current_mark == "X" else "X"


if __name__ == "__main__":
	print("Tic-Tac-Toe!")
	play_game()
