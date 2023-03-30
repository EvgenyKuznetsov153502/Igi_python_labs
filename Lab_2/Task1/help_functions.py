from calculate_statistics import count_of_sent, count_of_non_dec_sent, average_len_of_sent, average_len_of_word, \
    top_rep_n_grams
from constants import K, N


def input_check():
    while True:
        num = input("enter the number: ")
        if num.isdigit():
            return int(num)
        else:
            print("Input Error. Try again")


def input_info():
    message = " " + input("enter text: ")
    answer = input(f"If you want to enter K, N values then enter \"yes\", to take the default values(K={K}, N={N}) then"
                   " enter something else: ")

    if answer.lower() == 'yes':
        k = input_check()
        n = input_check()
    else:
        k = K
        n = N
    return message, k, n


def output_info(message: str, k: int, n: int):
    print("amount of sentences in the text:", count_of_sent(message))
    print("amount of non-declarative sentences in the text:", count_of_non_dec_sent(message))
    print("average length of the sentence in characters:", average_len_of_sent(message))
    print("average length of the word in the text in characters:", average_len_of_word(message))
    print(f"top-{k} repeated {n}-grams in the text: ", top_rep_n_grams(message, k, n))
