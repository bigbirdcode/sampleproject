Feature: Component C

Scenario: Component C normal operation
    Given new instance of component C
    When I set the list "[88, 89, 90]"
    Then I get the answer "XYZ"

Scenario: Component C special chars
    Given new instance of component C
    When I set the list "[44, 46, 47]"
    Then I get the answer ",./"
