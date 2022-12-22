from more_itertools import chunked


class CargoCrane:

    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._data = f.read().splitlines()
        self._stacks = self._get_stacks()
        self._instructions = self._get_instructions()
        self._move_crates()
        print(self._stacks)

    def _move_crates(self):
        pass

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

    def _get_instructions(self) -> dict:
        instruction_sentences = self._data[self._get_stack_endpoint_idx() + 2:]
        instructions = {
            'len': len(instruction_sentences),
            'move': [],
            'from': [],
            'to': []
        }
        for instruction_sentence in instruction_sentences:
            inst_spl = instruction_sentence.split()
            instructions['move'].append(int(inst_spl[inst_spl.index('move') + 1]))
            instructions['from'].append(int(inst_spl[inst_spl.index('from') + 1]))
            instructions['to'].append(int(inst_spl[inst_spl.index('to') + 1]))
        return instructions

    def _get_stack_endpoint_idx(self) -> int:
        for i, line in enumerate(self._data):
            if '1' in line:
                return i
        return 0

    @staticmethod
    def _pos_to_idx(pos: int) -> int:
        return pos - 1


if __name__ == '__main__':
    crane = CargoCrane('stacks_of_crates.txt')
