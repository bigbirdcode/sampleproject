# pragma pylint: disable=missing-docstring,redefined-outer-name

"""Feature tests."""

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

import mysw.main


@pytest.fixture
def context():
    return {}


scenarios('../features')


# @scenario('rot13.feature', 'Encrypt a text')
# def test_encrypt_text():
#     """Encrypt a text."""


# @scenario('rot13.feature', 'Decrypt a text')
# def test_decrypt_text():
#     """Decrypt a text."""


@given(parsers.parse('I have a text "{text}"'))
@given(parsers.parse('I have an encrypted text "{text}"'))
def i_have_encrypted_text(text, context):
    context['text'] = text


@when('I encrypt it')
@when('I decrypt it')
def i_en_de_crypt(context):
    context['ans'] = mysw.main.rot13(context['text'])


@then(parsers.parse('I get the answer "{ans}"'))
def i_get_answer(ans, context):
    assert context['ans'] == ans
