class FileHandler:
    def __init__(self, file_path: str = None, file_type: str = "csv") -> object:
        self.file_path = file_path
        self.file_type = file_type

    def open(self):
        return {"csv": self._handle_csv()}[self.file_type]

    def _handle_csv(self, handler: str = "r"):
        from csv import reader

        def __read():
            with open(self.file_path, "r") as _csv_file:
                _reader = reader(_csv_file)
                next(_reader, None)  # skip header
                return [row for row in _reader]

        def __write():
            pass

        return {"r": __read(), "w": __write()}[handler]
