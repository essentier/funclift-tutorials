class TextFile:

    @staticmethod
    def read(filename: str) -> str:
        with open(filename, "r") as file:
            return file.read()
    
    @staticmethod
    def write(filename: str, text: str) -> None:
        with open(filename, "w") as file:
            file.write(text)


def app():
    filename = 'hello.txt'
    TextFile.write(filename, 'Hello PyCon Latam')
    return TextFile.read(filename)


content = app()
print(content)

