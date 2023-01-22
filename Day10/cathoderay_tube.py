class CathodeRayTube:

    _interesting_cycles = [20, 60, 100, 140, 180, 220]

    def __init__(self, program_file: str):
        self._cycles = 1
        self._x = 1
        self._strength_sum = 0
        self._screen = [[], [], [], [], [], [], []]
        self._row = 0
        with open(program_file, 'r') as f:
            self._program = f.read().splitlines()

    def compile_program_strength(self) -> int:
        for command in self._program:
            self._process_command(command)
        return self._strength_sum

    def render_image(self):
        for command in self._program:
            self._render_pixels(command)
        for line in self._screen:
            print(''.join(line))

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

    def _render_pixels(self, command: str):
        if command == 'noop':
            self._update_screen()
            self._next_cycle(render=True)
        else:
            v = int(command.split()[1])
            for _ in range(2):
                self._update_screen()
                self._next_cycle(render=True)
            self._x += v

    def _update_screen(self):
        if self._cycles in range(self._x, self._x + 3):
            self._screen[self._row].append('#')
        else:
            self._screen[self._row].append('.')

    def _next_cycle(self, render=False):
        if not render:
            self._cycles += 1
        else:
            print(self._cycles)
            self._cycles += 1
            if self._cycles > 40:
                self._cycles = self._cycles % 40
                self._row += 1

    def _check_interesting(self):
        if self._cycles in self._interesting_cycles:
            self._strength_sum += self._cycles * self._x


if __name__ == '__main__':
    tube1 = CathodeRayTube('program.txt')
    print(tube1.compile_program_strength())
    tube2 = CathodeRayTube('program.txt')
    tube2.render_image()
