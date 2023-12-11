import os


class WordLoader:
    """Class that provides an access to the dictionary"""

    words = None

    @classmethod
    def load_words(cls):
        cls.words = set()
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)

    @classmethod
    def get_word_set(cls):
        return cls.words
