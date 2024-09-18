from FileReader import FileReader


class TextParser:
    def __init__(self, path):
        self.path = path
        self.text = ''
        self.tokens = []
        self.file_reader = FileReader(self.path)

    def clean_text_and_tokenize_pipeline(self):
        import re
        # lower case
        self.text = self.text.lower()
        # split by . ?
        self.tokens = re.split(r'[.?!]\s*', self.text)
        # remove all non-alphanumeric characters
        for i in range(len(self.tokens)):
            self.tokens[i] = ''.join(e for e in self.text if e.isalnum() or e.isspace())

        return self.tokens



    def create_dictonary_tokens(self):
        # lower case
        self.text = self.text.lower()
        # remove all non-alphanumeric characters
        self.text = ''.join(e for e in self.text if e.isalnum() or e.isspace())
        # tokenize
        self.tokens = self.text.split()

        return list(set(self.tokens))

    def parse(self):
        self.text = self.file_reader.read()
        self.clean_text_and_tokenize_pipeline()
        return self.tokens

    def print_first_10_tokens(self):
        print(self.tokens[:10])

#
# obj = TextParser('data.txt')
# obj.parse()
# obj.print_first_10_tokens()

a = [1,2]
print(a.index(2))
