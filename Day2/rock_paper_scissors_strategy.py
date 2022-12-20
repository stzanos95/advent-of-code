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

outcomes_calculated = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

class RockPaperScissorsTournament:

    def __init__(self, games_filename: str):
        with open(games_filename, 'r') as f:
            self._games = [game_line for game_line in f.read().splitlines()]

    def get_total_score(self, are_result=False):
        if not are_result:
            return sum([outcomes[game] for game in self._games])
        else:
            return sum([outcomes_calculated[game] for game in self._games])


if __name__ == '__main__':
    player1 = RockPaperScissorsTournament('tournament_games.txt')
    print(f'Total score if XYZ are my picks: {player1.get_total_score()}')
    print(f'Total score if XYZ are game results: {player1.get_total_score(are_result=True)}')