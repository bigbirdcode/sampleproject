# pragma pylint: disable=missing-docstring,invalid-name


# example configuration
NUM = 13


class B:

    def __init__(self):
        self.nums1 = []
        self.nums2 = []

    def set(self, values):
        self.nums1 = list(values)

    def proc(self):
        self.nums2 = []
        for n in self.nums1:
            if 65 <= n <= 77:
                n = n + 13
            elif 78 <= n <= 90:
                n = n - 13
            self.nums2.append(n)

    def get(self):
        return list(self.nums2)
