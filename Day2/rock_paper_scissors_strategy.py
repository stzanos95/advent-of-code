selection_scores = {'X': 1, 'Y': 2, 'Z': 3}
draw_games = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
win_games = [('A', 'Z'), ('B', 'X'), ('C', 'Y')]

class RockPaperScissorsTournament:

    def __init__(self, games_filename: str):
        with open(games_filename, 'r') as f:
            self._games = [game_line.split(' ') for game_line in f.read().splitlines()]

    def get_total_score(self):
        return sum([self._get_game_score(*game) for game in self._games])

    @staticmethod
    def _get_game_score(opponent_selection: str, player_selection: str) -> float:
        score = selection_scores[player_selection]
        if (opponent_selection, player_selection) in draw_games:
            score += 3
        elif (opponent_selection, player_selection) in win_games:
            score += 6
        return score


if __name__ == '__main__':
    player1 = RockPaperScissorsTournament('tournament_games.txt')
    print(player1.get_total_score())
