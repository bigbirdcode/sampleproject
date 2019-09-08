# pragma pylint: disable=missing-docstring,invalid-name


class A:

    def __init__(self):
        self.txt = ''
        self.nums = []

    def set(self, txt):
        self.txt = txt.upper()

    def proc(self):
        self.nums = [ord(c) for c in self.txt]

    def get(self):
        return self.nums
