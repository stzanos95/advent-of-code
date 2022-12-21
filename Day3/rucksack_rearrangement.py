from more_itertools import chunked

class RucksackRearranger:
    def __init__(self, rucksack_filename: str):
        with open(rucksack_filename, 'r') as f:
            self._elf_rucksacks = f.read().splitlines()
        self._elf_rucksack_items = [[rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
                                    for rucksack in self._elf_rucksacks]
        self._common_items = [self._get_common_item(*rucksack) for rucksack in self._elf_rucksack_items]
        self._badges = [self._get_badge(*rucksack) for rucksack in chunked(self._elf_rucksacks, 3)]

    def sum_of_common_item_priorities(self):
        return sum([self._get_priority(item) for item in self._common_items])

    def sum_of_badge_priorities(self):
        return sum([self._get_priority(badge) for badge in self._badges])

    @staticmethod
    def _get_common_item(item1: str, item2: str) -> str:
        return list(set(item1).intersection(item2))[0]

    @staticmethod
    def _get_badge(rucksack1: str, rucksack2: str, rucksack3: str):
        return list(set(rucksack1).intersection(rucksack2).intersection(rucksack3))[0]

    @staticmethod
    def _get_priority(letter: str) -> int:
        if letter.islower():
            return ord(letter) - 96
        else:
            return ord(letter) - 64 + 26


if __name__ == '__main__':
    rr = RucksackRearranger('rucksacks.txt')
    print(f'Sum of priorities: {rr.sum_of_common_item_priorities()}')
    print(f'Sum of badge priorities: {rr.sum_of_badge_priorities()}')
