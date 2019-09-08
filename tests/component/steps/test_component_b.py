# pragma pylint: disable=missing-docstring,redefined-outer-name

"""Component B tests."""

from ast import literal_eval
from pytest_bdd import scenarios, given, when, then, parsers

from mysw.b import B


scenarios('../features/component_b.feature')


@given('new instance of component B')
def component_b():
    return B()


@when(parsers.parse('I set the list "{text}"'))
def set_text(text, component_b):
    in_list = literal_eval(text)
    component_b.set(in_list)


@then(parsers.parse('I get the answer "{text}"'))
def get_list(text, component_b):
    expected = literal_eval(text)
    component_b.proc()
    assert component_b.get() == expected
