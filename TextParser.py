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
        import nltk
        from nltk.corpus import stopwords
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        self.text = ' '.join([word for word in self.text.split() if word not in stop_words])
        self.text = self.text.split('\n')
        self.text = ' . '.join(self.text)
        # split by . ?
        self.tokens = re.split(r'[.?!]\s*', self.text)
        # remove all non-alphanumeric characters
        for sentence in range(len(self.tokens)):


            self.tokens[sentence] = ''.join(e for e in self.tokens[sentence] if e.isalnum() or e.isspace()).split()


        return self.tokens



    def create_dictonary_tokens(self):
        token_dict = set()
        # lower case
        self.text = self.text.lower()
        # remove stop words
        import nltk
        from nltk.corpus import stopwords
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        self.text = ' '.join([word for word in self.text.split() if word not in stop_words])
        # remove \n
        self.text = self.text.replace('\n', ' ')
        # remove all non-alphanumeric characters
        self.text = ''.join(e for e in self.text if e.isalnum() or e.isspace())
        # tokenize
        self.tokens = self.text.split()

        for token in self.tokens:
            token_dict.add(token)
        return list(token_dict)

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
