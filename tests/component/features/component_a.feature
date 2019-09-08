Feature: Component A

Scenario: Component A normal operation
    Given new instance of component A
    When I set the text "XYZ"
    Then I get the answer "[88, 89, 90]"

Scenario: Component A lowercase
    Given new instance of component A
    When I set the text "xyz"
    Then I get the answer "[88, 89, 90]"

Scenario: Component A other chars
    Given new instance of component A
    When I set the text ",./"
    Then I get the answer "[44, 46, 47]"
