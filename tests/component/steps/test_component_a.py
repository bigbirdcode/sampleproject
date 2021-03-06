"""Component level tests of component A"""

# pragma pylint: disable=missing-docstring,redefined-outer-name

from ast import literal_eval
from pytest_bdd import scenarios, given, when, then, parsers

from mysw.a import A


scenarios('../features/component_a.feature')


@given('new instance of component A')
def component_a():
    """Given steps works as fixture, it will return a component A
    for the tests"""
    return A()


@when(parsers.parse('I set the text "{text}"'))
def set_text(text, component_a):
    component_a.set(text)


@then(parsers.parse('I get the answer "{text}"'))
def get_list(text, component_a):
    expected = literal_eval(text)
    component_a.proc()
    assert component_a.get() == expected
