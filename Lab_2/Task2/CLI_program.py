
class Storage:
    """storage for unique elements"""
    def __init__(self):
        self.cur_user: str = ""
        self.cur_container: set = set()

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
                        print('add')

                case 'remove':
                    if self.check_input_one_arg(len_list_of_words, 'remove'):
                        print('remove')

                case 'find':
                    if self.check_input_many_arg(len_list_of_words, 'find'):
                        print('find')

                case 'list':
                    if self.check_input_non_arg(len_list_of_words, 'list'):
                        print('list')

                case 'grep':
                    if self.check_input_one_arg(len_list_of_words, 'grep'):
                        print('grep')

                case 'save':
                    if self.check_input_non_arg(len_list_of_words, 'save'):
                        print('save')

                case 'load':
                    if self.check_input_one_arg(len_list_of_words, 'load'):
                        print('load')

                case 'switch':
                    if self.check_input_one_arg(len_list_of_words, 'switch'):
                        print('switch')

                case 'help':
                    if self.check_input_non_arg(len_list_of_words, 'help'):
                        self.print_help()

                case 'stop':
                    if self.check_input_non_arg(len_list_of_words, 'stop'):
                        print('Stop program')
                        break

                case _:
                    print('Error input. Try again')




