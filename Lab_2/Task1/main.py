from calculate_statistics import count_of_sent, count_of_non_dec_sent


def main():

    text = 'My name is Eugene. Are you crazy?! Mr. Vlad your ex. girlfriend get up at 6 p.m. and cook breakfast.' \
           'I am not fine... How are you doing? ' \
           'You love love you love my I am so much much love you am I am so much' \
           'much love you no fine you much love so much love...' \


    print("amount of sentences in the text:", count_of_sent(text))
    print("amount of non-declarative sentences in the text:", count_of_non_dec_sent(text))


if __name__ == '__main__':
    main()
