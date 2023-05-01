"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ Can be used to find a random word from a text file.
    >>> wf = WordFinder("/Users/student/words.txt")
        3 words read

    >>> wf.random()
        'cat'

    >>> wf.random()
        'cat'

    >>> wf.random()
        'porcupine'

    >>> wf.random()
        'dog'
        """

    def __init__(self, file):
        

        all_text = open(file)

        self.file = file

        self.words = self.parse(all_text)


    def parse(self, all_text):
        """Parse all_text -> list of words"""
        return [w.strip() for w in all_text]
    
    def random(self):
        """Return a random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Removes lines that start with # and returns a list
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    def parse(self, all_text):
       return [w.strip() for w in all_text if w.strip() and not w.startswith("#")]
