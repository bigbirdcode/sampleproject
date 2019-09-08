# pragma pylint: disable=missing-docstring,redefined-outer-name

import pytest

from mysw.b import B


@pytest.fixture
def b():
    return B()


def test_b_set(b):
    b.set([88])
    assert b.nums1 == [88]


def test_b_proc_simple_small(b):
    b.nums1 = [66]
    b.proc()
    assert b.nums2 == [79]


def test_b_proc_simple_big(b):
    b.nums1 = [88]
    b.proc()
    assert b.nums2 == [75]


def test_b_proc_simple_multi(b):
    b.nums1 = [65, 77, 78, 90]
    b.proc()
    assert b.nums2 == [78, 90, 65, 77]


def test_b_get(b):
    b.nums2 = [88]
    assert b.get() == [88]
