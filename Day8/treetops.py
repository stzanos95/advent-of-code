from operator import sub, add, lt, gt
from typing import Tuple


class Treetops:

    def __init__(self, treegrid_file: str):
        with open(treegrid_file, 'r') as f:
            self._data = [list(map(int, list(line))) for line in f.read().splitlines()]
        self._data_len = len(self._data)

    def count_visible_with_best_score(self) -> Tuple[int, int]:
        visibles = (len(self._data) - 1) * 4
        best_scenic_score = 0
        for _i, line in enumerate(self._data[1:-1]):
            for _j, treetop in enumerate(line[1:-1]):
                visible, scenic_score = self._is_visible_with_score(_i + 1, _j + 1, treetop)
                if visible:
                    visibles += 1
                if scenic_score > best_scenic_score:
                    best_scenic_score = scenic_score
        return visibles, best_scenic_score

    def _is_visible_with_score(self, i: int, j: int, treetop: int) -> Tuple[bool, int]:
        scenic_score = 1
        side_map = {
            'top'  : {'axis': 'y', 'operator': sub, 'flag': True,
                      'counter': i, 'comparison': gt, 'endval': 0},
            'bot'  : {'axis': 'y', 'operator': add, 'flag': True,
                      'counter': i, 'comparison': lt, 'endval': self._data_len - 1},
            'left' : {'axis': 'x', 'operator': sub, 'flag': True,
                      'counter': j, 'comparison': gt, 'endval': 0},
            'right': {'axis': 'x', 'operator': add, 'flag': True,
                      'counter': j, 'comparison': lt, 'endval': self._data_len - 1}
        }
        for side in side_map.keys():
            counter = side_map[side]['counter']
            operator = side_map[side]['operator']
            tree_counter = 0
            while side_map[side]['comparison'](counter, side_map[side]['endval']):
                if side_map[side]['axis'] == 'y':
                    next_treetop = self._data[operator(counter, 1)][j]
                else:
                    next_treetop = self._data[i][operator(counter, 1)]
                if treetop > next_treetop:
                    counter = operator(counter, 1)
                    tree_counter += 1
                else:
                    side_map[side]['flag'] = False
                    tree_counter += 1
                    break
            scenic_score *= tree_counter
        return any([_dict['flag'] for _dict in side_map.values()]), scenic_score


if __name__ == '__main__':
    treetops = Treetops('treegrid.txt')
    print(treetops.count_visible_with_best_score())
