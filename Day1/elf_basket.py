class ElfBasket:

    def __init__(self, basket_filename: str):
        with open(basket_filename, 'r') as f:
            self._calories_list = f.read().splitlines()
        self._elf_calories = []
        total_calories = 0
        for calories in self._calories_list:
            try:
                total_calories += int(calories)
            except ValueError:
                self._elf_calories.append(total_calories)
                total_calories = 0

    def max_calories(self) -> float:
        return max(enumerate(self._elf_calories), key=lambda x: x[1])[1]

    def sum_top_three(self) -> float:
        return sum(sorted(self._elf_calories)[-1:-4:-1])


if __name__ == '__main__':
    basket = ElfBasket('elf_calories.txt')
    print(f'Maximum calories: {basket.max_calories()} cal')
    print(f'Sum of top three gatherers: {basket.sum_top_three()} cal')
