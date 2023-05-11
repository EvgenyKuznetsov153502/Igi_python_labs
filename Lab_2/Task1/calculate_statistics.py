import re
from constants import REG_EXPR_TO_CALC_SENT, WORDS_CONTAIN_ONE_CHAR,  WORDS_CONTAIN_TWO_CHAR, WORDS_CONTAIN_THREE_CHAR,\
     REG_EXPR_TO_CALC_NON_DEC_SENT, REG_EXPR_TO_WORD, REG_EXPR_TO_NUM, K, N


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
    list_of_words = [word for word in re.findall(REG_EXPR_TO_WORD, message) if word not in re.findall(REG_EXPR_TO_NUM,
                                                                                                      message)]
    num_of_char = sum(len(word) for word in list_of_words)
    return round(num_of_char/count_of_sent(message), 2) if count_of_sent(message) != 0 else 0


def average_len_of_word(message: str):
    list_of_words = [word for word in re.findall(REG_EXPR_TO_WORD, message) if word not in re.findall(REG_EXPR_TO_NUM,
                                                                                                      message)]
    num_of_char = sum(len(word) for word in list_of_words)
    return round(num_of_char/len(list_of_words), 2) if len(list_of_words) != 0 else 0


def top_rep_n_grams(message: str, k=K, n=N):
    list_of_words = [word for word in re.findall(REG_EXPR_TO_WORD, message) if word not in re.findall(REG_EXPR_TO_NUM,
                                                                                                      message)]

    if len(list_of_words) < n:
        return f'Input error. N ({n}) is bigger than number of words({len(list_of_words)})'

    dictionary = {}
    for i in range(len(list_of_words) - n + 1):
        n_gram = " ".join(list_of_words[i:i+n])
        if n_gram not in dictionary.keys():
            dictionary[n_gram] = 1
        else:
            dictionary[n_gram] += 1

    if len(dictionary) <= k:
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0:k]
