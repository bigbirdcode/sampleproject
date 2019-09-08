"""Sample project, mysw

By BigBird who like to Code
https://github.com/bigbirdcode/sampleproject
"""

import os
import sys

# This file is the starting point of the sample project, mysw.
# Python has 2 types of calls:
#  - direct call, like: python main.py
#  - package call, like: python -m mysw
# Below quite ugly code will handle that
if __name__ == '__main__' and __package__ is None:
    # This was a direct call
    # package information is missing, and relative imports will fail
    # this hack imitates the package behavior and add outer dir to the path
    __package__ = "mysw"  # pylint: disable=redefined-builtin
    mysw_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # noqa: E501, pylint: disable=invalid-name

    if mysw_dir not in sys.path:
        sys.path.insert(0, mysw_dir)
    del mysw_dir  # clean up global name space

# Now relative import is ok
from . import a, b, c  # noqa: E402, pylint: disable=wrong-import-position


def rot13(text):
    """The rot13 function"""
    a_inst = a.A()
    b_inst = b.B()
    c_inst = c.C()
    a_inst.set(text)
    a_inst.proc()
    nums = a_inst.get()
    b_inst.set(nums)
    b_inst.proc()
    nums = b_inst.get()
    c_inst.set(nums)
    c_inst.proc()
    return c_inst.get()


def main():
    """Main function"""
    str_in = input("Type a word or sentence please: ")
    print(rot13(str_in))


if __name__ == '__main__':
    main()
