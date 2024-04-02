
def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    letter_dictionary = count_letters(text)
    print_report(letter_dictionary, path, word_count)
    


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def print_report(letter_dict, path, word_count):
    dict_keys = letter_dict.keys()
    list_of_dict = []
    for key in dict_keys:
        dict = {"letter": key , "count":letter_dict[key] }
        list_of_dict.append(dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for dict in list_of_dict:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")


def sort_on(dict):
    return dict["count"]


        

main()
