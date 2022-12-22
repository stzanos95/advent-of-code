from more_itertools import chunked


class CargoCrane:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._data = f.read().splitlines()
        self._stacks = self._get_stacks()
        self._directions = self._get_directions()
        self._move_crates()

    def _move_crates(self):
        pass

    def _get_stacks(self) -> list:
        crate_rows = self._data[:self._get_stack_endpoint_idx()]
        crate_stacks = []
        for crate_row in crate_rows[::-1]:
            for i, crate in enumerate(chunked(crate_row, 4)):
                crate_str = ''.join(crate).strip()
                if crate_str != '':
                    try:
                        crate_stacks[i].append(crate_str)
                    except IndexError:
                        crate_stacks.append([crate_str])
        return crate_stacks

    def _get_directions(self) -> {list}:
        return {'': self._data}

    def _get_stack_endpoint_idx(self) -> int:
        for i, line in enumerate(self._data):
            if '1' in line:
                return i
        return 0


if __name__ == '__main__':
    crane = CargoCrane('stacks_of_crates.txt')
