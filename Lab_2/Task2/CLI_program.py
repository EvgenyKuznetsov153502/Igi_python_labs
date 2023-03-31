import pickle
import re


class Storage:
    """storage for unique elements"""
    def __init__(self):
        self.__cur_user: str = ""
        self.__cur_container: set = set()

    """prints all commands"""
    @staticmethod
    def print_help():
        print('add <key> [key, …] – add one or more elements to the container')
        print('remove <key> – delete key from container')
        print('find <key> [key, …] – check if the element is presented in the container, print each found or '
              '“No such elements” if nothing is')
        print('list – print all elements of container')
        print('grep <regex> – check the value in the container by regular expression,'
              ' print each found or “No such elements” if nothing is;')
        print('save/load – save container to file/load container from file')
        print('switch – switches to another user')
        print('stop- exit the program')

    @staticmethod
    def check_input_non_arg(len_list_of_words: int, name_of_com: str):
        if len_list_of_words != 1:
            print(f'Command \'{name_of_com}\' does not support arguments')
            return False
        else:
            return True

    @staticmethod
    def check_input_one_arg(len_list_of_words: int, name_of_com: str):
        if len_list_of_words > 2:
            print(f'Error. Command \'{name_of_com}\' сan takes only 1 argument. You entered {len_list_of_words - 1} '
                  f'arguments')
            return False
        if len_list_of_words == 1:
            print(f'Error. Argument not found. Command \'{name_of_com}\' should takes 1 argument')
            return False
        return True

    @staticmethod
    def check_input_many_arg(len_list_of_words: int, name_of_com: str):
        if len_list_of_words == 1:
            print(f'Error. Arguments not found. Command \'{name_of_com}\' takes 1 or more arguments')
            return False
        else:
            return True

    def run(self):
        print("Welcome to storage for unique items")
        self.log()
        print("To see the list of commands type help")
        print('To exit the program enter stop')

        while True:

            message = input('> ')
            list_of_words = message.split()
            len_list_of_words = len(list_of_words)

            if len_list_of_words == 0:
                print('Error empty input. Try again.')
                continue

            match list_of_words[0]:
                case 'add':
                    if self.check_input_many_arg(len_list_of_words, 'add'):
                        self.add(list_of_words[1:])

                case 'remove':
                    if self.check_input_one_arg(len_list_of_words, 'remove'):
                        self.remove(list_of_words[1])

                case 'find':
                    if self.check_input_many_arg(len_list_of_words, 'find'):
                        self.find(list_of_words[1:])

                case 'list':
                    if self.check_input_non_arg(len_list_of_words, 'list'):
                        self.list()
                        print("\nUserName:", self.__cur_user)

                case 'grep':
                    if self.check_input_one_arg(len_list_of_words, 'grep'):
                        self.grep(list_of_words[1])

                case 'save':
                    if self.check_input_non_arg(len_list_of_words, 'save'):
                        self.save()

                case 'load':
                    if self.check_input_non_arg(len_list_of_words, 'load'):
                        try:
                            self.load()
                        except FileNotFoundError:
                            print("Error, container does not exist")

                case 'switch':
                    if self.check_input_one_arg(len_list_of_words, 'switch'):
                        self.help_survey()
                        self.switch(list_of_words[1])

                case 'help':
                    if self.check_input_non_arg(len_list_of_words, 'help'):
                        self.print_help()

                case 'stop':
                    if self.check_input_non_arg(len_list_of_words, 'stop'):
                        self.help_survey()
                        print('Stop program')
                        break

                case _:
                    print('Error input. Try again')

    def add(self, arguments: list):
        for argument in arguments:
            self.__cur_container.add(argument)

    def remove(self, argument):
        if argument in self.__cur_container:
            self.__cur_container.remove(argument)
        else:
            print('Element not found')

    def find(self, arguments):
        flag = False
        for argument in arguments:
            if argument in self.__cur_container:
                print(argument)
                flag = True
        if not flag:
            print('No such elements')

    def list(self):
        if self.__cur_container:
            print('Container contains:')
            for arg in self.__cur_container:
                print(arg)
        else:
            print('Container is empty')

    def grep(self, reg_exp):
        flag = False
        for arg in self.__cur_container:
            if re.findall(reg_exp, arg):
                print(arg)
                flag = True
        if not flag:
            print('No such elements')

    def log(self):
        name = input("Enter username: \n>")

        while True:
            if len(name.split()) > 1:
                name = input('Error input. Username must not contain spaces. Try again\n> ')
            elif len(name.split()) == 0:
                name = input('Error input. Username must not be empty. Try again\n> ')
            else:
                break
        self.switch(name)

    def save(self):
        path = fr'/home/eugene/Studing/Igi_python_labs/Lab_2/DataBase/{self.__cur_user}' + '.pickle'

        try:
            with open(path, 'rb') as file:
                temp_set = self.__cur_container.union(pickle.load(file))
        except FileNotFoundError:
            temp_set = set()

        with open(path, 'wb') as file:
            pickle.dump(temp_set, file)

    def load(self):
        path = fr'/home/eugene/Studing/Igi_python_labs/Lab_2/DataBase/{self.__cur_user}' + '.pickle'

        with open(path, 'rb') as file:
            self.__cur_container = self.__cur_container.union(pickle.load(file))

    def switch(self, name: str):
        self.__cur_user = name
        self.__cur_container = set()
        print("Do you want to load the container ? Enter 'yes' or 'no'.")
        answer = input(">")
        while answer.lower() != 'yes' and answer.lower() != 'no':
            answer = input("Error input. Enter 'yes' or 'no\n>")

        if answer.lower() == 'yes':
            print(f'Loading a container named {name}')
            try:
                self.load()
                print("Download successful")
            except FileNotFoundError:
                print("Error, container does not exist")
                print('Creating a new container')
                self.__cur_container = set()
        else:
            print('Creating a new container')
            self.__cur_container = set()

    def help_survey(self):
        answer = input('Do you want to save past container? Enter \'yes\' or \'no\'\n>')
        while answer.lower() != 'yes' and answer.lower() != 'no':
            answer = input("Error input. Enter 'yes' or 'no\n>")

        if answer.lower() == 'yes':
            self.save()





