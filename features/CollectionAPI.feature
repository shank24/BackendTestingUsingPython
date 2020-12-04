Feature: Verify if collection is created using Postman API
  # Enter feature description here.

  Scenario: Verify Add Collection functionality
    Given the Collection details which needs to be added
    When we execute Add Collection PostAPI method
    Then the collection should be successfully added


