from more_itertools import chunked
from operator import mul, add


class MonkeyKeepAway:

    def __init__(self, notes_file: str):
        with open(notes_file, 'r') as f:
            listed_notes = [line.strip().split(':') for line in f.read().splitlines()]
        self._monkeys = {}
        self._LCM = 1
        for monkey, monkey_notes in enumerate(chunked(listed_notes, 7)):
            starting_items = list(map(int, monkey_notes[1][1].strip().split(',')))
            expression = monkey_notes[2][1].split('old')[1].strip().split(' ')
            operation = self._operation(expression)
            divisor = int(monkey_notes[3][1].split()[-1])
            monkey_true = int(monkey_notes[4][1].split()[-1])
            monkey_false = int(monkey_notes[5][1].split()[-1])
            self._monkeys[monkey] = {
                'items': starting_items,
                'operation': operation,
                'divisor': divisor,
                'monkey_true': monkey_true,
                'monkey_false': monkey_false
            }
            self._LCM *= divisor
        self._monkey_inspections = [0] * len(self._monkeys)

    def inspect_items(self, rounds: int, too_worried=False) -> int:
        for i in range(rounds):
            for monkey, note in self._monkeys.items():
                monkey_true = note['monkey_true']
                monkey_false = note['monkey_false']
                divisor = note['divisor']
                operation = note['operation']
                for item in list(note['items']):
                    self._monkey_inspections[monkey] += 1
                    if too_worried:
                        new_item = operation(item)
                    else:
                        new_item = operation(item) // 3
                    if new_item > self._LCM:
                        new_item %= self._LCM
                    if new_item % divisor == 0:
                        self._monkeys[monkey_true]['items'].append(new_item)
                    else:
                        self._monkeys[monkey_false]['items'].append(new_item)
                note['items'].clear()
        print(self._monkey_inspections)
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
    print(f'Monkey business if not too worried: {mka.inspect_items(20)}')
    print(f'Monkey business if too worried: {mka.inspect_items(10000, True)}')
