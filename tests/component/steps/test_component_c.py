"""Component level tests of component C"""

# pragma pylint: disable=missing-docstring,redefined-outer-name

from ast import literal_eval
from pytest_bdd import scenarios, given, when, then, parsers

from mysw.c import C


scenarios('../features/component_c.feature')


@given('new instance of component C')
def component_c():
    """Given steps works as fixture, it will return a component C
    for the tests"""
    return C()


@when(parsers.parse('I set the list "{text}"'))
def set_text(text, component_c):
    in_list = literal_eval(text)
    component_c.set(in_list)


@then(parsers.parse('I get the answer "{text}"'))
def get_list(text, component_c):
    component_c.proc()
    assert component_c.get() == text
