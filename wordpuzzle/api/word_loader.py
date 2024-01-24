import os


class WordLoader:
    """Class that provides an access to the dictionary.
       Updated to also include smaller dictionaries for testing purposes.
       Smaller dictionaries can be accessed using separate, distinct methods, 
       to avoid confusion on which dictionary is being loaded.
    """

    words = None
    small_words = None
    medium_words = None

    @classmethod
    def load_words_small(cls):
        cls.small_words = set()
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/small_words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)
                
    @classmethod
    def load_words_medium(cls):
        cls.medium_words = set()
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/medium_words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)
    
    @classmethod
    def load_words(cls):
        cls.words = set()
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)

    @classmethod
    def get_word_set_small(cls):
        return cls.small_words

    @classmethod
    def get_word_set_medium(cls):
        return cls.medium_words

    @classmethod
    def get_word_set(cls):
        return cls.words