# pragma pylint: disable=missing-docstring,invalid-name


class C:

    def __init__(self):
        self.txt = ''
        self.nums = []

    def set(self, values):
        self.nums = list(values)

    def proc(self):
        self.txt = ''.join(chr(c) for c in self.nums)

    def get(self):
        return self.txt
