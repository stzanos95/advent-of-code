class CargoCrane:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._data = f.read().splitlines()
        self._stacks = self._get_stacks()
        self._directions = self._get_directions()

    def _get_stacks(self) -> {list}:
        return {'': self._data}

    def _get_directions(self) -> {list}:
        return {'': self._data}


if __name__ == '__main__':
    pass
