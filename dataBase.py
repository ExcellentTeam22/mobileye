from singleton import singleton

"""
    This class represent a data base that holds all the files contents and
    provide several searching methods.
"""


@singleton
class DataBase:
    def _init_(self):
        self.index
        self.path
        self.x
        self.y
        self.color
        self.label