from unittest import TestCase, main
from calculate_statistics import count_of_sent, count_of_non_dec_sent, average_len_of_sent, average_len_of_word, \
    top_rep_n_grams


class TestCountOfSent(TestCase):
    def test_empty(self):
        self.assertEqual(count_of_sent(" "), 0)

    def test_abbreviation(self):
        self.assertEqual(count_of_sent("Wow, Mr. Max your ex. girlfriend get up at 6 p.m. and cook breakfast."), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_of_sent("Hello, my name is Eugene!! Are you crazy?! How are you doing???"
                                       "I'm not fine..."), 4)


class TestCountOfNonDecSent(TestCase):
    def test_empty(self):
        self.assertEqual(count_of_non_dec_sent(" "), 0)

    def test_abbreviation(self):
        self.assertEqual(count_of_non_dec_sent("Wow, Mr. Max your ex. girlfriend get up at 6 p.m. and cook food."), 0)

    def test_multiple_characters(self):
        self.assertEqual(count_of_non_dec_sent("Hello, my name is Eugene!! Are you crazy?! How are you doing???"
                                               "I'm not fine..."), 3)


class TestAverageLenOfSent(TestCase):
    def test_empty(self):
        self.assertEqual(average_len_of_sent(" "), 0)

    def test_abbreviation(self):
        self.assertEqual(average_len_of_sent("Wow, Mr. Max your ex. girlfriend get up at 6 p.m. and cook food."), 44)

    def test_multiple_characters(self):
        self.assertEqual(average_len_of_sent("Hello, my name is Eugene!! Are you crazy?! How are you doing???"
                                             "I'm not fine..."), 13.25)


class TestAverageLenOfWord(TestCase):
    def test_empty(self):
        self.assertEqual(average_len_of_word(" "), 0)

    def test_abbreviation(self):
        self.assertEqual(average_len_of_word("Wow, Mr. Max your ex. girlfriend get up at 6 p.m. and cook food."), 3.14)

    def test_multiple_characters(self):
        self.assertEqual(average_len_of_word("Hello, my name is Eugene!! Are you crazy?! How are you doing???"
                                             "I'm not fine..."), 3.31)


class TestTopRepNgrams(TestCase):
    def test_empty(self):
        self.assertEqual(top_rep_n_grams(' '), 'Input error. N (4) is bigger than number of words(0)')

    def test_text(self):
        self.assertEqual(top_rep_n_grams('Hi I am I am Eugene Hi I am. How are doing are doing How are I am', 4, 2),
                         [('I am', 4), ('Hi I', 2), ('How are', 2), ('are doing', 2)])

    def test_big_top(self):
        self.assertEqual(top_rep_n_grams('Hi I am I am Eugene Hi I am. How', 400),
                         [('Hi I am I', 1), ('I am I am', 1), ('am I am Eugene', 1),
                          ('I am Eugene Hi', 1), ('am Eugene Hi I', 1), ('Eugene Hi I am', 1),
                          ('Hi I am How', 1)])


if __name__ == '__main__':
    main()
