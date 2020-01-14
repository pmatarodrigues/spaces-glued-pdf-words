
import pdftotext

import os, subprocess, re

from math import log
from fpdf import FPDF

import extra_functions
import open_files
from word_classification import Model


def separate_pontuation(text):
    print("[ --- Separating pontuation --- ] \n")

    # ---- NOT WORKING: hiffens maiores (ex: " all jobs - even those of seemingly little significance - are")
    isolated_sentences = re.findall(r"[\w']+|[.,!?:;()]", text)

    return isolated_sentences


def separate_words(WORD_FILE_PATH, extracted_text):
    print("[ --- Separating words --- ] \n")

    result = []
    # --- separate the full text by smaller sentences
    isolated_sentences = separate_pontuation(extracted_text)

    # --- get the value of each word (percentage by how high in the table is)
    # --- get the size of the bigger word
    wordcost, maxword = open_files.wordlist_file(WORD_FILE_PATH)

    model = Model(wordcost, maxword)
    # regexp_to_split = re.compile("[^\w0-9']+")

    for sentence in isolated_sentences:
        # --- don't count pontuation as a sentence but add to final result
        if len(sentence) < 2:
            result += sentence
            continue
        # --- do the split for all the other sentences
        result += model.split(sentence)

    return result


def main():
    PDF_FILE_PATH = 'pdfs/pt-pt_no_spaces.pdf'
    WORD_FILE_PATH = "dictionaries/dic_freq (pt-pt)"

    # --- get original dictionary and transform into organized words
    # extra_functions.organize_original_dictionary("output.md")

    # ---- get string with text from pdf file
    extracted_text = open_files.text_from_pdf(PDF_FILE_PATH)

    result = separate_words(WORD_FILE_PATH, extracted_text)

    print("[ --- RESULT --- ]")
    print(" ".join(result))



main()