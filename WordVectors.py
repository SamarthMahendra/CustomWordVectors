from TextParser import TextParser


class Word2Vec:

    def __init__(self, cn, tokens_dict):
        self.context_length = cn
        self.co_occurrence_matrix = [[0 for _ in range(len(tokens_dict))] for _ in range(len(tokens_dict))]
        self.tokens_dict = tokens


    def create_co_occurrence_matrix(self,tokens):
        # Loop over each sentence (tokens is a list of sentences)
        for sentence in tokens:
            for i, word in enumerate(sentence):
                if word in self.tokens_dict:
                    index_of_word = self.tokens_dict[word]

                    # Traverse backward within the context window
                    for j in range(max(i - self.context_length, 0), i):
                        neighbor_word = sentence[j]
                        if neighbor_word in self.tokens_dict:
                            index_of_neighbour_word = self.tokens_dict[neighbor_word]
                            self.co_occurrence_matrix[index_of_word][index_of_neighbour_word] += 1

                    # Traverse forward within the context window
                    for j in range(i + 1, min(i + self.context_length + 1, len(sentence))):
                        neighbor_word = sentence[j]
                        if neighbor_word in self.tokens_dict:
                            index_of_neighbour_word = self.tokens_dict[neighbor_word]
                            self.co_occurrence_matrix[index_of_word][index_of_neighbour_word] += 1


        return self.co_occurrence_matrix









obj = TextParser('data.txt')
tokens = obj.parse()
tokens_dict = obj.create_dictonary_tokens()
word_vec_obj = Word2Vec(3, tokens_dict)

co_occurrence_matrix = word_vec_obj.create_co_occurrence_matrix(tokens)

# Print a 5x5 slice of the co-occurrence matrix to verify
for row in co_occurrence_matrix[25:50]:
    print(row[25:50])




