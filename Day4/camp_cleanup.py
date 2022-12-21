class CampCleanup:

    def __init__(self, assignment_pairs_filename: str):
        with open(assignment_pairs_filename, 'r') as f:
            assignment_pairs = f.read().splitlines()
        self._pairs_list = [[list(map(int, pair.split('-'))) for pair in two_pair.split(',')]
                            for two_pair in assignment_pairs]

    def count_full_containment(self) -> int:
        return [self._have_fully_contained(*two_pair) for two_pair in self._pairs_list].count(True)

    @staticmethod
    def _have_fully_contained(range_1: [int, int], range_2: [int, int]) -> bool:
        sorted_ranges = sorted([range_1, range_2], key=lambda x: x[0])
        if sorted_ranges[0][0] == sorted_ranges[1][0] or sorted_ranges[0][1] >= sorted_ranges[1][1]:
            return True
        else:
            return False


if __name__ == '__main__':
    camp_cleanup = CampCleanup('assignment_pairs.txt')
    print(f'Sum of pairs that have full containment: {camp_cleanup.count_full_containment()}')
