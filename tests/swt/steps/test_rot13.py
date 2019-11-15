"""Software level or feature level tests of the entire sw app"""

# pragma pylint: disable=missing-docstring,redefined-outer-name

from collections import namedtuple

from pytest_bdd import scenarios, given, when, then, parsers

import mysw.main


scenarios('../features')

# Just an explanation, scenarios() call will create tests for each scenario,
# just like the below example codes

# @scenario('rot13.feature', 'Encrypt a text')
# def test_encrypt_text():
#     """Encrypt a text."""

# @scenario('rot13.feature', 'Decrypt a text')
# def test_decrypt_text():
#     """Decrypt a text."""


# Note: Scenario Outline use different mechanism with the <> signs.
# therefore if you use simple scenarios and scenario outlines then
# you need multiple step definitions.

@given('I have a text "<text_in>"')
@given('I have an encrypted text "<text_in>"')
@given(parsers.parse('I have a text "{text_in}"'))
@given(parsers.parse('I have an encrypted text "{text_in}"'))
def given_my_sw_io(text_in):
    """Given steps works as fixture, it will return a storage,
    simulating io for my_sw"""
    my_sw_io = namedtuple('MySwIo', ['text', 'ans'])
    my_sw_io.text = text_in
    my_sw_io.ans = ""
    return my_sw_io


@when('I encrypt it')
@when('I decrypt it')
def i_en_de_crypt(given_my_sw_io):
    given_my_sw_io.ans = mysw.main.rot13(given_my_sw_io.text)


@then('I get the answer "<text_out>"')
@then(parsers.parse('I get the answer "{text_out}"'))
def i_get_answer(text_out, given_my_sw_io):
    assert given_my_sw_io.ans == text_out
