import open_files
import re

def organize_original_dictionary(WORD_FILE_PATH):
    # --- get words from original dictionary
    words = open_files.get_words_from_original_dic(WORD_FILE_PATH)

    words_pt = []
    # --- filter the words to remove unecessary characters
    for w in words:
        print(w)
        # words_pt += re.findall("^([\wâáàãéêẽíóõôç'-]+)", w)
        words_pt += re.findall("^[0-9]+.\s+([\wâáàãéêẽíóõôç'-]+)", w)

    # --- save to new file dictionary
    with open("dic_freq (pt-pt).txt", "w") as text_file:
        print("\n".join(words_pt), file=text_file)

def remove_spaces_from_pdf(PDF_FILE_PATH):
    # ---- get string with text from pdf file
    extracted_text = open_files.text_from_pdf(PDF_FILE_PATH)
    extracted_text = extracted_text.replace(" ","")

    with open("output.md", "w") as text_file:
        print(extracted_text, file=text_file)

    # --- after this convert to .pdf using https://www.markdowntopdf.com/