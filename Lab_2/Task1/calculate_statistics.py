import re
from constants import REG_EXPR_TO_CALC_SENT, WORDS_CONTAIN_ONE_CHAR,  WORDS_CONTAIN_TWO_CHAR, WORDS_CONTAIN_THREE_CHAR,\
     REG_EXPR_TO_CALC_NON_DEC_SENT, REG_EXPR_TO_WORD


def count_of_sent(message: str):
    num_of_sentences = len(re.findall(REG_EXPR_TO_CALC_SENT, message))

    for word in WORDS_CONTAIN_ONE_CHAR:
        num_of_sentences -= message.lower().count(word)

    for word in WORDS_CONTAIN_TWO_CHAR:
        num_of_sentences -= 2 * message.lower().count(word)

    for word in WORDS_CONTAIN_THREE_CHAR:
        num_of_sentences -= 3 * message.lower().count(word)

    return num_of_sentences if num_of_sentences > 0 else 0


def count_of_non_dec_sent(message: str):
    return len(re.findall(REG_EXPR_TO_CALC_NON_DEC_SENT, message))


def average_len_of_sent(message: str):
    list_of_words = re.findall(REG_EXPR_TO_WORD, message)
    num_of_char = sum(len(word) for word in list_of_words)
    return round(num_of_char/count_of_sent(message), 2) if count_of_sent(message) != 0 else 0


def average_len_of_word(message: str):
    list_of_words = re.findall(REG_EXPR_TO_WORD, message)
    num_of_char = sum(len(word) for word in list_of_words)
    return round(num_of_char/len(list_of_words), 2) if len(list_of_words) != 0 else 0