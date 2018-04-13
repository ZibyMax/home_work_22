


import chardet
from chardet.universaldetector import UniversalDetector

def encode_file(file):
    detector = UniversalDetector()
    with open(file, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    return detector.result

def get_words_from_file(file_name, encode):
    words = []
    with open(file_name, 'r', encoding=encode['encoding']) as f:
        for line in f:
            new_words = line.strip().lower()
            words += new_words
    return words

def sort_by_value(key):
    return

def get_words_longer_6_char(words):
    words_longer_6 = []
    for word in words:
        if len(word) > 6:
            words_longer_6.append(word)
    return words_longer_6

def get_sorted_words_rating(words):
    words_rating = []
    set_words = set(words)
    for word in set_words:
        words_rating.append([word, words.count(word)])
    words_rating = sorted(words_rating, key=lambda i: i[1])
    return words_rating

def print_top10(words_rating, file_name):
    print('ТОП-10 слов файла новостей: {}', format(file_name))
    for i in range(10):
        print('{}, {}, {}', format(i, words_rating[i], words_rating[i]))







def home_work():
    files = ["newsafr.txt"] #, "newscy.txt", "newsfr.txt", "newsit.txt"]
    for file_name in files:
        encode = encode_file(file_name)
        words = get_words_from_file(file_name, encode)
        words = get_words_longer_6_char(words)
        words_rating = get_sorted_words_rating(words)
        #print_top10(words_rating, file_name)
        print(words_rating)

home_work()