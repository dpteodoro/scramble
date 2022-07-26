from service.scrambled_unit import ScrambledUnit


class ScrambledReader(object):
    """
    Evaluates if a dictionary word exists within a test word in its original or scrambled form

    Methods
    -------
    get_matches()
        :returns all occurrence of the dictionary_word, whether in original or scrambled form
    """

    def __init__(self, dict_word, test_word):
        self._test_word = test_word
        self._dict_word = dict_word
        self._matches = []
        self._len_word = len(dict_word)
        self._len_test = len(test_word)
        self._test_word_scrambled_unit = ScrambledUnit(self._test_word[0: self._len_word])
        self._dict_word_scrambled_unit = ScrambledUnit(self._dict_word)
        self._evaluate()

    def get_matches(self):
        """
        :return  all dictionary word matches in the test input:
        """
        return self._matches

    def _evaluate(self):
        self._evaluate_first_substring()
        for i in range(1, self._len_test - self._len_word):
            self._evaluate_subsequent_substrings(self._test_word[i: i + self._len_word])

    def _evaluate_first_substring(self):
        initial_test_substring = self._test_word[0: self._len_word]
        if self._test_word_scrambled_unit == self._dict_word_scrambled_unit:
            self._matches.append(initial_test_substring)

    def _evaluate_subsequent_substrings(self, test_substring):
        self._test_word_scrambled_unit.word = test_substring
        if self._test_word_scrambled_unit == self._dict_word_scrambled_unit:
            self._matches.append(test_substring)
