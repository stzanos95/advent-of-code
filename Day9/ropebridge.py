class BridgeCell:

    def __init__(self, with_tail=False, with_head=False, tail_has_visited=False):
        self._with_tail = with_tail
        self._with_head = with_head
        self._tail_has_visited = tail_has_visited

    @property
    def with_tail(self):
        return self._with_tail

    @with_tail.setter
    def with_tail(self, a: bool):
        self._with_tail = a

    @property
    def with_head(self):
        return self._with_head

    @with_head.setter
    def with_head(self, a: bool):
        self._with_head = a

    @property
    def tail_has_visited(self):
        return self._tail_has_visited

    @tail_has_visited.setter
    def tail_has_visited(self, a: bool):
        self._tail_has_visited = a


class RopeBridge:
    pass


if __name__ == '__main__':
    cell = BridgeCell()
    print(cell.with_head)
    cell.with_head = True
    print(cell.with_head)
