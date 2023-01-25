from more_itertools import chunked
from operator import mul, add
from math import floor


class MonkeyKeepAway:

    _rounds = 20

    def __init__(self, notes_file: str):
        with open(notes_file, 'r') as f:
            listed_notes = [line.strip().split(':') for line in f.read().splitlines()]
        self._monkeys = {}
        for monkey, monkey_notes in enumerate(chunked(listed_notes, 7)):
            starting_items = list(map(int, monkey_notes[1][1].strip().split(',')))
            expression = monkey_notes[2][1].split('old')[1].strip().split(' ')
            operation = self._operation(expression)
            divisor = int(monkey_notes[3][1].split()[-1])
            monkey_true = int(monkey_notes[4][1].split()[-1])
            monkey_false = int(monkey_notes[5][1].split()[-1])
            self._monkeys[monkey] = {
                'starting_items': starting_items,
                'operation': operation,
                'divisor': divisor,
                'monkey_true': monkey_true,
                'monkey_false': monkey_false
            }
        self._monkey_inspections = [0] * len(self._monkeys)

    def inspect_items(self) -> int:
        for _ in range(self._rounds):
            for monkey, note in self._monkeys.items():
                for item in list(note['starting_items']):
                    self._monkey_inspections[monkey] += 1
                    note['starting_items'].remove(item)
                    new_item = floor(note['operation'](item) / 3)
                    if new_item % note['divisor'] == 0:
                        self._monkeys[note['monkey_true']]['starting_items'].append(new_item)
                    else:
                        self._monkeys[note['monkey_false']]['starting_items'].append(new_item)
        self._monkey_inspections.sort(reverse=True)
        return self._monkey_inspections[0] * self._monkey_inspections[1]

    @staticmethod
    def _operation(expression: []):
        if expression[0] == '*':
            if len(expression) == 2:
                return lambda x: mul(x, int(expression[1]))
            else:
                return lambda x: mul(x, x)
        else:
            if len(expression) == 2:
                return lambda x: add(x, int(expression[1]))
            else:
                return lambda x: add(x, x)


if __name__ == '__main__':
    mka = MonkeyKeepAway('notes.txt')
    print(mka.inspect_items())
