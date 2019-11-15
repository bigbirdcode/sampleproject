"""Unit level test of functions of component A"""

# pragma pylint: disable=missing-docstring,redefined-outer-name

import pytest

from mysw.a import A


@pytest.fixture
def a():
    """Fixture will return a component A for the tests"""
    return A()


def test_a_set(a):
    a.set('x')
    assert a.txt == 'X'


def test_a_proc_simple(a):
    a.txt = 'X'
    a.proc()
    assert a.nums == [88]


def test_a_proc_multi(a):
    a.txt = 'XYZ'
    a.proc()
    assert a.nums == [88, 89, 90]


def test_a_get(a):
    a.nums = [88]
    assert a.get() == [88]
