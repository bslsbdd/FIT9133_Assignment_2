
############################################
# The solution is developed by Chengyao Xu #
# Student ID: 27133087                     #
############################################
import pandas as pd
import math
# allow it to print more data in data frame
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000000)


class IDFAnalyser:

    # init class constructor  Create an instance variable called data that is a Dataframe
    def __init__(self):
        self.data = pd.DataFrame()

    # Loads the frequency of a cleaned text into data with a title that corresponds to the
    # text the frequency was generated from.
    def load_frequency(self, book_frequency, book_title):
        # create new data frame with index on book title
        new_row = pd.DataFrame([book_frequency], index=[book_title])
        # append the new data frame to data
        self.data = self.data.append(new_row, sort=False)
        return

    # Obtains the IDF for the term provided and the documents loaded into data
    def get_IDF(self,term):
        if term not in self.data.keys():
            n = 0
        else:
            n = self.data.count()[term]
        d = len(self.data)
        idf = 1 + math.log(d/(1+n))
        return idf

    def get_data(self):
        return self.data

