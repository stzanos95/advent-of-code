def main():
    with open('elf_calories.txt', 'r') as f:
        calories_list = f.read().splitlines()
    elf_total_calories = []
    total_calories = 0
    for calories in calories_list:
        try:
            total_calories += int(calories)
        except ValueError:
            elf_total_calories.append(total_calories)
            total_calories = 0
    print(max(enumerate(elf_total_calories), key=lambda x: x[1])[1])


if __name__ == '__main__':
    main()
