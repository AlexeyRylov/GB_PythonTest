# Класс принтер, печает все что получает в консоль


class Printer:
    def __init__(self, strihgi):
        self.stringi = strihgi

    def prints(self):
        print(self.stringi)