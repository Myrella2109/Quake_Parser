class LogReader:
    """
    Responsável apenas por ler o arquivo.
    Não contém regra de negócio.
    """

    def __init__(self, path: str):
        self.path = path

    def read_lines(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return file.readlines()