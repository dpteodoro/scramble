from collections import Counter


class ScrambledUnit(object):
    """A scrambled unit is comprised of the word and its character frequency array.

    Parameters
    ----------
    word : str
        A word, not necessarily a valid English word. Should be composed of any of the 26 lowercase English
        alphabets only

    Attributes
    ----------
    frequency_array : Counter
        dictionary of characters and how often they appear in the word
    word: str
        the dictionary word or the substring of a test word that is being evaluated
    """

    def __init__(self, word):
        """
        Initialize a scrambled unit using a word
        :param word: str
            A lowercase English-alphabet-only word
        """
        self._word = word
        self._frequency_array = Counter(word)

    def __eq__(self, other):
        """Two scrambled units are deemed equal if they have the same beginning and ending letters,
        and are comprised of the same characters. The letters in the middle may be jumbled."""
        if self.word[0] == other.word[0] and self.word[-1] == other.word[-1]:
            return self.frequency_array and other.frequency_array
        return False

    @property
    def frequency_array(self):
        """Character frequency dictionary."""
        return self._frequency_array

    @frequency_array.setter
    def frequency_array(self, freq_array):
        self._frequency_array = freq_array

    @property
    def word(self):
        """If set, the frequency array will also be adjusted."""
        return self._word

    @word.setter
    def word(self, new_word):
        old_letter = self._word[0]
        new_letter = new_word[-1]
        self._adjust_frequency_array(old_letter, new_letter)
        self._word = new_word

    def _adjust_frequency_array(self, old_letter, new_letter):
        # Adjust frequency array. But to be efficient, we only want to decrease count for previous first letter
        # and increase count for new last letter. The rest of the letter frequencies will stay the same
        if self._frequency_array[old_letter] == 1:
            del self._frequency_array[old_letter]
        else:
            self._frequency_array[old_letter] -= 1
        self._frequency_array[new_letter] += 1
