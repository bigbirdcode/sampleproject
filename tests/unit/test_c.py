"""Unit level test of functions of component C"""

# pragma pylint: disable=missing-docstring,redefined-outer-name

import pytest

from mysw.c import C


@pytest.fixture
def c():
    """Fixture will return a component C for the tests"""
    return C()


def test_c_set(c):
    c.set([88])
    assert c.nums == [88]


def test_c_proc_simple(c):
    c.nums = [88]
    c.proc()
    assert c.txt == 'X'


def test_c_proc_multi(c):
    c.nums = [88, 89, 90]
    c.proc()
    assert c.txt == 'XYZ'


def test_c_get(c):
    c.txt = 'X'
    assert c.get() == 'X'
