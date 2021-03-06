class Text:
    def __init__(self, file):
        self.__chars = 0
        self.__words = 0
        self.__sentences = 0
        self.__file = file

    def counter(self):
        import os
        if not os.path.isfile(self.__file):  # checking whether the specified path is an existing file or not
            raise OSError('Cannot open file')
        else:
            f = open(self.__file, 'r')
            text = f.read()
            self.__chars = len(text)
            self.__words = len(text.split())
            import re  # regular expressions module
            self.__sentences = len(re.findall(r'[.!?]+', text))

    def __str__(self):
        return f'Characters: {self.__chars} \nWords: {self.__words} \nSentences: {self.__sentences}'


if __name__ == "__main__":
    txt = Text('text.txt')
    txt.counter()
    print(txt)