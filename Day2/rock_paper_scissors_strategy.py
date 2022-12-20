outcomes = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

class RockPaperScissorsTournament:

    def __init__(self, games_filename: str):
        with open(games_filename, 'r') as f:
            self._games = [game_line for game_line in f.read().splitlines()]

    def get_total_score(self):
        return sum([outcomes[game] for game in self._games])


if __name__ == '__main__':
    player1 = RockPaperScissorsTournament('tournament_games.txt')
    print(player1.get_total_score())
