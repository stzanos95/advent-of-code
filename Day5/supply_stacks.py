from more_itertools import chunked


class CargoCrane:

    def __init__(self, filename: str, model='9000'):
        with open(filename, 'r') as f:
            self._data = f.read().splitlines()
        self._stacks = self._get_stacks()
        self._commands = self._get_commands()
        self._model = model
        self._move_crates()

    def _move_crates(self):
        for i in range(self._commands['len']):
            move_int = self._commands['move'][i]
            from_idx = self._commands['from'][i]-1
            to_idx = self._commands['to'][i]-1
            if self._model == '9000':
                for _ in range(move_int):
                    self._stacks[to_idx].append(self._stacks[from_idx].pop(-1))
            elif self._model == '9001':
                self._stacks[to_idx] += self._stacks[from_idx][-move_int:]
                self._stacks[from_idx] = self._stacks[from_idx][:-move_int]

    def get_top_crates(self) -> str:
        return ''.join([stack[-1] for stack in self._stacks])

    def _get_stacks(self) -> list:
        crate_rows = self._data[:self._get_stack_endpoint_idx()]
        crate_stacks = []
        for crate_row in crate_rows[::-1]:
            for i, crate in enumerate(chunked(crate_row, 4)):
                crate_letter = ''.join(crate).strip().replace('[', '').replace(']', '')
                if crate_letter != '':
                    try:
                        crate_stacks[i].append(crate_letter)
                    except IndexError:
                        crate_stacks.append([crate_letter])
        return crate_stacks

    def _get_commands(self) -> dict:
        command_sentences = self._data[self._get_stack_endpoint_idx() + 2:]
        commands = {
            'len': len(command_sentences),
            'move': [],
            'from': [],
            'to': []
        }
        for command_sentence in command_sentences:
            inst_spl = command_sentence.split()
            commands['move'].append(int(inst_spl[inst_spl.index('move') + 1]))
            commands['from'].append(int(inst_spl[inst_spl.index('from') + 1]))
            commands['to'].append(int(inst_spl[inst_spl.index('to') + 1]))
        return commands

    def _get_stack_endpoint_idx(self) -> int:
        for i, line in enumerate(self._data):
            if '1' in line:
                return i
        return 0


if __name__ == '__main__':
    crane1 = CargoCrane('stacks_of_crates.txt')
    print(f'Top crates 9000: {crane1.get_top_crates()}')
    crane2 = CargoCrane('stacks_of_crates.txt', model='9001')
    print(f'Top crates 9001: {crane2.get_top_crates()}')
