Feature: Google Search

  Scenario: Search for Behave
    Given I open Google
    When I search for "Behave BDD"
    Then the results should contain "behave"