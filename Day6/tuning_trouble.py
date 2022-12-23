class TuningDevice:

    header_size = 4
    message_size = 14

    def __init__(self, datastream_filename: str):
        with open(datastream_filename, 'r') as f:
            self._datastream = f.read()

    def get_first_endpos(self, packet: str):
        return self._get_header_endpoint() + 1 if packet == 'header' else self._get_message_endpoint() + 1

    def _get_message_endpoint(self) -> int:
        for i in range(self._get_header_endpoint() + self.message_size, len(self._datastream)):
            if self._is_interesting(self._datastream[i-(self.message_size-1):i+1], self.message_size):
                return i

    def _get_header_endpoint(self) -> int:
        for i in range(self.header_size - 1, len(self._datastream)):
            if self._is_interesting(self._datastream[i-(self.header_size-1):i+1], self.header_size):
                return i

    @staticmethod
    def _is_interesting(packet: str, packet_size: int) -> bool:
        return len(set(packet)) == packet_size


if __name__ == '__main__':
    tuner = TuningDevice('datastream.txt')
    print(f'The first header endpoint is the {tuner.get_first_endpos("header")}th charracter.')
    print(f'The first message endpoint is the {tuner.get_first_endpos("message")}th charracter.')
