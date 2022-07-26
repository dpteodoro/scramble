from service.utils import get_logger
from service.scrambled_reader import ScrambledReader

DICTIONARY_PATH = 'scramble/data/dictionary.txt'
INPUT_PATH = 'scramble/data/input.txt'

logger = get_logger("scrambled_words_finder")


def read_dictionary(path):
    # Reads a dictionary file with words separated by newline
    logger.debug(f"Reading dictionary file {path}")
    with open(path) as f:
        return (line.strip() for line in f.readlines())


if __name__ == '__main__':
    with open(INPUT_PATH) as file:
        index = 1
        for test_word in file:
            dictionary_matches = 0
            dict_words = read_dictionary(DICTIONARY_PATH)
            for dict_word in dict_words:
                scrambled_reader = ScrambledReader(dict_word, test_word)
                dictionary_matches += any(scrambled_reader.get_matches())
            logger.info(f"Case #{index}: {dictionary_matches}")
            index += 1
