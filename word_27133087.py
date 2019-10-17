############################################
# The solution is developed by Chengyao Xu #
# Student ID: 27133087                     #
############################################


class WordAnalyser:

    # init class constructor with dictionary word count and word sum
    def __init__(self):
        self.word_counts = {}
        self.word_sum = 0
        return

    # Redefine the method to present the number of occurrences for each word in a string format.
    def __str__(self):
        info = ''
        for key, value in self.word_counts.items():
            info = info + key + ':' + str(value) + '\n'
        return info

    # This method  accept the cleaned book text as the argument, and attempt to count the
    # occurrences for each of the words.
    def analyse_words(self, book_text):
        for word in book_text.split():
            self.word_sum += 1
            if word in self.word_counts.keys():
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
        return

    # use the word count and sum to calculate word frequency
    def get_word_frequency(self):
        word_frequency = {}
        for key, value in self.word_counts.items():
            word_frequency[key] = value/self.word_sum
        return word_frequency
