Feature: ROT13
    As a user I want rot-13 encryption

Scenario: Encrypt a text
    Given I have a text "DO NOT LOOK"
    When I encrypt it
    Then I get the answer "QB ABG YBBX"

Scenario: Decrypt a text
    Given I have an encrypted text "GBB ZNAL FRPERGF"
    When I decrypt it
    Then I get the answer "TOO MANY SECRETS"

Scenario: Decrypt another text
    Given I have an encrypted text "ZNAL FRPERGF"
    When I decrypt it
    Then I get the answer "MANY SECRETS"
