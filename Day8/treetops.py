from operator import sub, add, lt, gt


class Treetops:

    def __init__(self, treegrid_file: str):
        with open(treegrid_file, 'r') as f:
            self._data = [list(map(int, list(line))) for line in f.read().splitlines()]
        self._data_len = len(self._data)

    def count_visible(self) -> int:
        visibles = (len(self._data) - 1) * 4
        for _i, line in enumerate(self._data[1:-1]):
            for _j, treetop in enumerate(line[1:-1]):
                if self._is_visible(_i + 1, _j + 1, treetop):
                    visibles += 1
        return visibles

    def _is_visible(self, i: int, j: int, treetop: int) -> bool:
        side_map = {
            'top'  : {'axis': 'y', 'counter': i, 'flag': True,
                      'operator': sub, 'comparison': gt, 'endval': 0},
            'bot'  : {'axis': 'y', 'counter': i, 'flag': True,
                      'operator': add, 'comparison': lt, 'endval': self._data_len - 1},
            'left' : {'axis': 'x', 'counter': j, 'flag': True,
                      'operator': sub, 'comparison': gt, 'endval': 0},
            'right': {'axis': 'x', 'counter': j, 'flag': True,
                      'operator': add, 'comparison': lt, 'endval': self._data_len - 1}
        }
        for side in side_map.keys():
            counter = side_map[side]['counter']
            operator = side_map[side]['operator']
            while side_map[side]['comparison'](counter, side_map[side]['endval']):
                if side_map[side]['axis'] == 'y':
                    next_treetop = self._data[operator(counter, 1)][j]
                else:
                    next_treetop = self._data[i][operator(counter, 1)]
                if treetop > next_treetop:
                    counter = operator(counter, 1)
                else:
                    side_map[side]['flag'] = False
                    break
            if side_map[side]['flag']:
                break
        return any([_dict['flag'] for _dict in side_map.values()])


if __name__ == '__main__':
    treetops = Treetops('treegrid.txt')
    print(treetops.count_visible())
