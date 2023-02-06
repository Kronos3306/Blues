class Decor:

    def __init__(self):
        pass

    @staticmethod
    def plus_bold():
        return "\033[01;32m[+]\033[0m"

    @staticmethod
    def astk():
        return "\033[34m[*]\033[0m"