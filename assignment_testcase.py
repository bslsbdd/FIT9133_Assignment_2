import preprocessor_27133087 as processor
import word_27133087 as word
import idf_27133087 as idf
import task4_27133087 as task4

def get_document_word_frequency(book_name):
    book = processor.Preprocessor()
    book.read_text(book_name)
    book.clean()
    cleaned_content = book.get_content()
    word_analysis = word.WordAnalyser()
    word_analysis.analyse_words(cleaned_content)
    word_frequency = word_analysis.get_word_frequency()
    return word_frequency

if __name__ == "__main__":
    idf_analyser = idf.IDFAnalyser()
    book_11_0_info = get_document_word_frequency('11-0.txt')
    book_84_0_info = get_document_word_frequency('84-0.txt')
    book_1342_0_info = get_document_word_frequency('1342-0.txt')
    book_1661_0_info = get_document_word_frequency('1661-0.txt')
    book_1952_0_info = get_document_word_frequency('1952-0.txt')
    book_pg16328_info = get_document_word_frequency('pg16328.txt')
    idf_analyser.load_frequency(book_11_0_info,'11-0')
    idf_analyser.load_frequency(book_84_0_info,'84-0')
    idf_analyser.load_frequency(book_1342_0_info,'1342-0')
    idf_analyser.load_frequency(book_1661_0_info,'1661-0')
    idf_analyser.load_frequency(book_1952_0_info,'1952-0')
    idf_analyser.load_frequency(book_pg16328_info,'pg16328')
    print(task4.choice('frankenstein',idf_analyser))
    print(task4.choice('sherlock',idf_analyser))
    print(task4.choice('the',idf_analyser))
    print(task4.choice('bird',idf_analyser))
    print(task4.choice('wallpaper',idf_analyser))
    print(task4.choice('\n',idf_analyser))

