file = 'data/2.txt'

POINTS = {
	"ROCK": 1,
	"PAPER": 2,
	"SCISSOR": 3
}

RESULT = {
	"X": "LOSS",
	"Y": "DRAW",
	"Z": "WIN"
}

OPPONENT = {
	"A": "ROCK",
	"B": "PAPER",
	"C": "SCISSOR"
}

def get_points(op_move, play_move):
	if op_move == play_move:
		return 3
	if op_move == "ROCK":
		if play_move == "SCISSOR":
			return 0
		return 6
	if op_move == "SCISSOR":
		if play_move == "PAPER":
			return 0
		return 6
	if op_move == "PAPER":
		if play_move == "ROCK":
			return 0
		return 6

def expected_play(op_move, expected_result):
	if expected_result == "DRAW":
		return op_move
	if expected_result == "WIN":
		if op_move == "ROCK":
			return "PAPER"
		if op_move == "PAPER":
			return "SCISSOR"
		if op_move == "SCISSOR":
			return "ROCK"
	if expected_result == "LOSS":
		if op_move == "ROCK":
			return "SCISSOR"
		if op_move == "PAPER":
			return "ROCK"
		if op_move == "SCISSOR":
			return "PAPER"


if __name__ == "__main__":
	total_points = 0
	with open(file, 'r') as open_file:
		data = open_file.read()
		for i in data.split("\n"):
			try:
				[opp, play] = i.split(" ")
				op_move = OPPONENT[opp]
				result = RESULT[play]
				play_move = expected_play(op_move, result)
				game_points = get_points(op_move, play_move)
				play_points = POINTS[play_move]
				print(play_points)
				total_points += game_points + play_points
			except:
				pass
	print(total_points)