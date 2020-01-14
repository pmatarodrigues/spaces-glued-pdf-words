import pdftotext
from math import log


def text_from_pdf(PDF_FILE_PATH):

    print("\n[ --- Loading text from pdf --- ] \n")

    # --- load file pdf
    with open(PDF_FILE_PATH, "rb") as f:
        pdf = pdftotext.PDF(f)

    # --- count number of pages in pdf (not used)
    number_of_pages = len(pdf)

    # --- read text to one string
    return "\n\n".join(pdf)

def get_words_from_original_dic(WORD_FILE_PATH):
    words = open(WORD_FILE_PATH).read().split("\n")

    return words

def wordlist_file(WORD_FILE_PATH):
    words = open(WORD_FILE_PATH).read().split()
    value_of_word = {}
    max_word_size = 0

    # --- set a value to each word from higher (most common) to lower (less common)
    for position, word in enumerate(words):
        value_of_word[word] = len(words)/(position+1)

    # --- check what is the size of the biggest word
    for x in words:
        if len(x) > max_word_size:
            max_word_size = len(x)

    return value_of_word, max_word_size