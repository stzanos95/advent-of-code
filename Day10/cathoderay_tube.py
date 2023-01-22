class CathodeRayTube:

    _interesting_cycles = [20, 60, 100, 140, 180, 220]

    def __init__(self, program_file: str):
        self._cycles = 1
        self._x = 1
        self._strength_sum = 0
        with open(program_file, 'r') as f:
            self._program = f.read().splitlines()

    def compile_program_strength(self) -> int:
        for command in self._program:
            self._process_command(command)
        return self._strength_sum

    def _process_command(self, command):
        if command == 'noop':
            self._check_interesting()
            self._next_cycle()
        else:
            v = int(command.split()[1])
            for _ in range(2):
                self._check_interesting()
                self._next_cycle()
            self._x += v

    def _next_cycle(self):
        self._cycles += 1

    def _check_interesting(self):
        if self._cycles in self._interesting_cycles:
            self._strength_sum += self._cycles * self._x


if __name__ == '__main__':
    tube = CathodeRayTube('program.txt')
    print(tube.compile_program_strength())
