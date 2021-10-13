"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """ for finding random words from dictionary
    >>> wf = WordFinder("word.txt")
    235886 have been read
    >>> wf.random() in files
    True





    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""
        files = open(path)
        self.word = self.parse(files)
        print(f"{len(self.word)} have been read")

    def parse(self,files):
        """Parse files-> list of words"""
        return [words.strip()for words in files]

    def random(self):
        return random.choice(self.word)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments."""
    def parse(self,files):
        return [ words.strip() for words in files 
                if words.strip() and not words.startswith("#")]
