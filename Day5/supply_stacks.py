from more_itertools import chunked


class CargoCrane:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._data = f.read().splitlines()
        self._stacks = self._get_stacks()
        self._commands = self._get_commands()
        self._move_crates()

    def top_crate_join(self):
        return ''.join([stack[-1] for stack in self._stacks])

    def _move_crates(self):
        for i in range(self._commands['len']):
            for _ in range(self._commands['move'][i]):
                self._stacks[self._commands['to'][i]-1].append(self._stacks[self._commands['from'][i]-1].pop(-1))

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
    crane = CargoCrane('stacks_of_crates.txt')
    print(f'Combination of top crates in each stack: {crane.top_crate_join()}')