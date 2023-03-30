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


def main():
    text = 'My name is Eugene. Are you crazy?! Mr. Vlad your ex. girlfriend get up at 6 p.m. and cook breakfast.' \
           'I am not fine... How are you doing? ' \
           'You love love you love my I am so much much love you am I am so much' \
           'much love you no fine you much love so much love...'

    print("amount of sentences in the text:", count_of_sent(text))
    print("amount of non-declarative sentences in the text:", count_of_non_dec_sent(text))
    print("average length of the sentence in characters:", average_len_of_sent(text))
    print("average length of the word in the text in characters:", average_len_of_word(text))
    answer = input(f"If you want to enter K, N values then enter \"yes\", to take the default values(K={K}, N={N}) then"
                   "enter something else: ")

    if answer == 'yes':
        k = input_check()
        n = input_check()
    else:
        k = K
        n = N

    print(f"top-{k} repeated {n}-grams in the text: ", top_rep_n_grams(text, k, n))


if __name__ == '__main__':
    main()
