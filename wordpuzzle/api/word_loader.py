import os


class WordLoader:
    """Class that provides an access to the dictionary.
       Updated to also include smaller dictionaries for testing purposes.
       Smaller dictionaries can be loaded using separate, distinct methods, 
       to avoid confusion on which dictionary is being loaded.
    """

    words = None

    @classmethod
    def load_words_small(cls):
        cls.words = set()
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/small_words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)
                
    @classmethod
    def load_words_medium(cls):
        cls.words = set()
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
    def get_word_set(cls):
        return cls.words