class TuningDevice:

    def __init__(self, datastream_filename: str):
        with open(datastream_filename, 'r') as f:
            self._datastream = f.read()

    def get_header_idx(self) -> int:
        for i in range(3, len(self._datastream)):
            if self._is_header(self._datastream[i-3:i+1]):
                return i+1

    @staticmethod
    def _is_header(packet: str) -> bool:
        return len(set(packet)) == 4


if __name__ == '__main__':
    tuner = TuningDevice('datastream.txt')
    print(f'The first marker appears after the {tuner.get_header_idx()}th charracter arrives.')
