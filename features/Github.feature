Feature: Github API Validation
  # Enter feature description here.

  Scenario: Session Management Check
    Given I have github credentials
    When I hit get repo API of Github
    Then Status Code of Response should be 401

