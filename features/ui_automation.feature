Feature: UI Automation for Login and Product List

  Scenario: Navigate to Login Page
    Given I launch the browser and go to "https://rahulshettyacademy.com/loginpagePractise/"
    Then I should see the login form

  Scenario: Enter Valid Username
    Given I am on the login page
    When I enter "rahulshettyacademy" in the username field
    Then the username field value should be "rahulshettyacademy"

  Scenario: Enter Valid Password
    Given I am on the login page
    When I enter "learning" in the password field
    Then the password field value should be "learning"

  Scenario: Select Admin as User Type
    Given I am on the login page
    When I select the Admin radio button
    Then the Admin radio button should be selected

  Scenario: Select Role from Dropdown
    Given I am on the login page
    When I select "Student" from the dropdown list
    Then "Student" should be present in the dropdown

  Scenario: Agree to Terms and Conditions
    Given I am on the login page
    When I check the "I Agree to the terms and conditions" checkbox
    Then the checkbox should be checked

  Scenario: Submit the Login Form
    Given I am on the login page
    When I click the login button
    Then the login button should be present

  Scenario: Verify 'iphone X' in Product List
    Given I am logged in
    Then I should see "iphone X" in the product list

  Scenario: Verify 'Realme 9 pro' in Product List
    Given I am logged in
    Then I should see "Realme 9 pro" in the product list
