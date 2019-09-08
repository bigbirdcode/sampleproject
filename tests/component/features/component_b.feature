Feature: Component B

Scenario: Component B normal operation
    Given new instance of component B
    When I set the list "[88, 89, 90]"
    Then I get the answer "[75, 76, 77]"

Scenario: Component B non text
    Given new instance of component B
    When I set the list "[44, 46, 47]"
    Then I get the answer "[44, 46, 47]"

