############################################
# The solution is developed by Chengyao Xu #
# Student ID: 27133087                     #
############################################

import string

class Preprocessor:
    # init class constructor with empty book content
    def __init__(self):
        self.book_content = ''

    # redefine the toString function to print the book content
    def __str__(self):
        return self.book_content

    # clean function make clear out non english character and punctuation
    def clean(self):
        book_content_cleaned = ''
        # start clean process when book has content
        if len(self.book_content) != 0:
            for character in self.book_content:
                # clear out unwanted character only keep english character, number and required symbol
                if character in string.ascii_letters  or \
                        character.isnumeric() or \
                        character in ['-','_',' ',' '] or \
                        character == '\n':
                    if character in ['-','_',' ']:
                        book_content_cleaned += ' '
                    else:
                        book_content_cleaned += character.lower()
            self.book_content = book_content_cleaned
            return
        else:
            return 1

    # read the book content from file with utf 8 encoding
    def read_text(self, text_name):
        file = open(text_name, 'r', encoding= 'utf-8')
        lines = file.readlines()
        for line in lines:
            self.book_content += line
        return

    # getter for book content
    def get_content(self):
        return self.book_content
