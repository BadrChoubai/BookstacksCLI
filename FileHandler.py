from Bookshelf import Shelf


class FileHandler:
    _file_path: str
    _file_ext: str

    def __init__(self, file_path: str, file_type: str = "csv"):
        self._file_path = file_path
        self._file_ext = file_path.split(".")[1]
        self.read = lambda ext=self._file_ext: {
            "csv": self.open_csv,
            "yml": self.open_yaml,
        }[self._file_ext]

    def open_csv(self, mode: str = "r"):
        with open(self._file_path, mode=mode) as csv_file:
            from csv import reader

            _reader = reader(csv_file)
            next(_reader, None)  # skip CSV Header
            return [row for row in _reader]

    def open_yaml(self, mode: str = "r"):
        with open(self._file_path, mode=mode) as yaml_file:
            from yaml import load, FullLoader

            _reader = load(yaml_file, Loader=FullLoader)
            return _reader
