
class Storage:
    """storage for unique elements"""

    def __init__(self):
        self.cur_user: str = ""
        self.cur_container: set = set()
        self.storage: dict[str, set] = dict[str, set]()

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
