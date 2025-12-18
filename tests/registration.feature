Feature: User Registration
  Scenario: Successful registration with valid details
    Given I am a new user on the registration page
    When I enter a valid name, email, and password
    And I submit the registration form
    Then my account should be created
    And I should be redirected to the welcome page

  Scenario: Registration with invalid email format
    Given I am a new user on the registration page
    When I enter a name and password
    And I enter an invalid email address
    And I submit the registration form
    Then I should see an error message indicating invalid email format
    And my account should not be created

  Scenario: Registration with weak password
    Given I am a new user on the registration page
    When I enter a name and valid email address
    And I enter a weak password
    And I submit the registration form
    Then I should see an error message indicating password strength requirements
    And my account should not be created
