Feature: Verify if collection is created using Postman API
  # Enter feature description here.

  @collection
  Scenario: Verify Add Collection functionality
    Given the Collection details which needs to be added
    When we execute Add Collection PostAPI method
    Then the collection should be successfully added
    And Status Code of Response should be 200

  @collection
  Scenario Outline: Verify Add Collection functionality
    Given the Collection details which <name> to be added
    When we execute Add Collection PostAPI method
    Then the collection should be successfully added
    Examples:
      | name |
      | New School |
      | Old School |


