from typing import Tuple


class RucksackRearranger:
    def __init__(self, rucksack_filename: str):
        with open(rucksack_filename, 'r') as f:
            elf_rucksacks = f.read().splitlines()
        self._elf_rucksacks = [[rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
                               for rucksack in elf_rucksacks]
        self._common_items = [self._get_common_item(*rucksack) for rucksack in self._elf_rucksacks]

    def sum_of_priorities(self):
        return sum([self._get_priority(item) for item in self._common_items])

    @staticmethod
    def _get_common_item(rucksack1: str, rucksack2: str) -> str:
        return list(set(rucksack1).intersection(rucksack2))[0]

    @staticmethod
    def _get_priority(letter: str) -> int:
        if letter.islower():
            return ord(letter) - 96
        else:
            return ord(letter) - 64 + 26


if __name__ == '__main__':
    rr = RucksackRearranger('rucksacks.txt')
    print(f'Sum of priorities: {rr.sum_of_priorities()}')
