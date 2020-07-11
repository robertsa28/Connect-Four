# Student Name: Alex Roberts
# Date: December 6th, 2018


from Board import Board
from sys import exit

def game_on(board):
	move_num = 1
	while move_num <= Board.MAX_MOVES:
		player_num = (move_num + 1) % 2 + 1
		move = board.take_turn(player_num)
		print(board)
		if board.has_winner(move[0], move[1]):
			return (True, player_num)
		move_num += 1
	return (False, 0)

def main():
	board = Board()
	print(board)
	(won, player) = game_on(board)
	if won:
		print("Player", player, "Wins!")
	else:
		print("Game has ended in a tie.")

main()